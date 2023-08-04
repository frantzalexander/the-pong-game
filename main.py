from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

import time

#Setting the game screen and title
screen = Screen()
screen.bgcolor("black")
screen.setup(
    width = 800,
    height = 600
    )
screen.title("Pong")
screen.tracer(0)

#Setting the initial paddle positions
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

#Initializing the ball and scoreboard objects
ball = Ball()
scoreboard = Scoreboard()

#Creating the keyboard interactions for the paddles
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

#Setting the game elements and interactions
game_is_on = True
while game_is_on:
    
    #Setting the update time for the ball movement
    time.sleep(ball.move_speed) 
    screen.update()
    ball.move()
    
    #Detect when the ball hits the upper or lower bounds.
    if ball.ycor() > 280 or ball.ycor() < -280: 
        ball.bounce_y()
    
    #Detect when the ball hits the paddles.
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
         ball.bounce_x()

    #Detect paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
        
screen.exitonclick()