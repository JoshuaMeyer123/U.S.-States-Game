import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()
    if answer_state == 'Exit':
        break
    if answer_state in all_states and answer_state not in guessed_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        x_val = int(state_data.x)
        y_val = int(state_data.y)
        t.goto(x_val, y_val)
        t.write(answer_state)
        guessed_states.append(answer_state)

# Create a csv file that lists the states that were not guessed
remaining_states = [state for state in all_states if state not in guessed_states]
new_data = pandas.DataFrame(remaining_states)
new_data.to_csv("states_to_practise.csv")
