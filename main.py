import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# def mouse_click_coordinate(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(mouse_click_coordinate)
# turtle.mainloop()

answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")
