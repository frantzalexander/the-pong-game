# the-pong-game
## Project Overview
This project is to create the classic game of Pong. 

This is a two player game where each player controls a paddle. 

The goal is to bounce the ball and force the opposing player to miss. 

## Objectives
- Create the screen.
- Create the body for each slider.
- Create the ability to control each slider independently.
- Create a second slider.
- Create & move the ball where it moves constantly.
- Detect the collision between the ball and each slider.
- Detect the collision between the ball and each wall.
- Detect when the slider misses the ball.
- Create the scoreboard.

## Results
The speed of the ball increases each time it bounces off a paddle.

As the game progresses, it becomes more difficult to bounce the ball back.


The graphical user interface:


![2023-08-04](https://github.com/frantzalexander/the-pong-game/assets/128331579/cb4551f0-c0fa-4ddf-86ae-917691d705d4)


## Process
The project is separated into the following 4 modules:
- Ball
- Paddle
- Scoreboard
- Main

### Project Flowchart
```mermaid
flowchart TD
    start(((START)))
    ball{Ball Module}
    paddle{Paddle Module}
    scoreboard{Scoreboard Module}
    maingame{Main Game Module}
    ballattr[Ball Attributes: Color, Shape & Movement Speed]
    paddleattr[Paddle Attributes: Color, Shape, Size & Initial Position]
    scoreboardattr[Scoreboard Attributes: Text Color & Set Initial Score to Zero]
    defball[Define: Ball Direction Changes, Ball Movement Speed Increases & Reset Positioning]
    defpaddle[Define the Paddle Upward & Downward Movement]
    defscore[Define Positioning & Font]
    scoreupdate[Score Update When a Player Scores]
    screen[Set the Screen]
    paddlepos[Set Initial Paddle Positions]
    keyboard[Create Keyboard Interactions for Paddles]
    setgame[Set Game Conditions]
    finish(((END)))
    start --> ball
    start --> paddle
    start --> scoreboard
    ball --> ballattr
    ballattr --> defball
    paddle --> paddleattr
    paddleattr --> defpaddle
    scoreboard --> scoreboardattr
    scoreboardattr --> defscore
    defscore --> scoreupdate
    defball --> maingame
    defpaddle --> maingame
    scoreupdate --> maingame
    maingame --> screen
    screen --> paddlepos
    paddlepos --> keyboard
    keyboard --> setgame
    setgame --> finish
