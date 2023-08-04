from turtle import Turtle

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10 #Setting the initial horizontal and vertical movement direction
        self.y_move = 10
        self.move_speed = 0.1 #Initial ball update speed
    
    #Defining the ball movement pattern
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    #Setting the ball vertical direction change 
    def bounce_y(self):
        self.y_move *= -1 

    #Setting the ball horizontal direction and movement speed changes
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9
    
    #Reset the ball position
    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()