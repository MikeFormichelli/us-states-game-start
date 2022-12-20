from turtle import Turtle, Screen

screen = Screen()
screen.screensize(400, 400)
#screen.tracer(0)

# list = ["hiya", "fuckit", "damn"]
# user_input = input("name it: ")
#
# def find_item():
#         if user_input in list:
#             print("this is it")
#         else:
#             return "fuck"
#
# find_item()


class ExperimentalTurtle(Turtle):

    def __int__(self):
        super().__init__()
        self.shape("circle")
        self.hideturtle()
        self.goto(50, 50)
        print(self.pos())

    def goto_place(self):
        self.goto(100, 100)
        print(self.pos())


t = ExperimentalTurtle()

#screen.update()

screen.exitonclick()
