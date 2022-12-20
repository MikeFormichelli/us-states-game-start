import turtle
import pandas
from writing_turtle import WritingTurtle
from time import sleep

# Screen set up
number_correct = 0
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# writing set up:
# w_turtle = turtle.Turtle()
# w_turtle.hideturtle()
# w_turtle.penup()
w_t = WritingTurtle()

DATA = pandas.read_csv("50_states.csv")
STATE_LIST = DATA["state"].to_list()
GAME_ON = True

while GAME_ON:
    answer_state = \
        screen.textinput(title=f"{number_correct}/50 correct", prompt="What's another state's name?").title()

    for i in range(len(STATE_LIST)):
        if STATE_LIST[i] == answer_state:
            state = DATA[DATA["state"] == answer_state]
            x_coord = float(state.x.values)
            y_coord = float(state.y.values)
            coordinates = (x_coord, y_coord)
            w_t.setpos(coordinates)
            # print(w_t.pos())
            w_t.write(answer_state)
            sleep(0.1)
            number_correct += 1
    if number_correct == 50:
        GAME_ON = False

# print(answer_state)

# This code would be used to build the csv database
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)


# mainloop is an alternative to the screen.exitonclick()
turtle.mainloop()
