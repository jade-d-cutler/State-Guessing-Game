
import turtle
import pandas

screen = turtle.Screen()
screen.setup(800, 600)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    user_input = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()

    if user_input == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
    if user_input in all_states:
        guessed_states.append(user_input)
        tim = turtle.Turtle()
        tim.hideturtle()
        tim.penup()
        state_data = data[data.state == user_input]
        tim.goto(state_data.x.item(), state_data.y.item())
        tim.write(user_input)


screen.exitonclick()
