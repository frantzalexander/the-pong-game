from turtle import Screen, Turtle
from paddle import Paddle


screen = Screen()
screen.bgcolor("black")
screen.setup(
    width = 800,
    height = 600
)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

def go_up():
    new_y = Paddle.ycor() + 20
    Paddle.goto(Paddle.xcor(), new_y)

def go_down():
    new_y = Paddle.ycorr() - 20
    Paddle.goto(Paddle.xcor(), new_y)

screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")

game_is_on = True
while game_is_on:
    screen.update()


screen.exitonclick()