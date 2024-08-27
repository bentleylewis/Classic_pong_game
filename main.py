from turtle import Turtle, Screen
from paddles import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

turtle = Turtle()
screen = Screen()
ball = Ball()
scoreboard = Scoreboard()

screen.setup(800, 600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)
l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))


screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")


while scoreboard.l_score < 5 and scoreboard.l_score < 5:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 400:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -400:
        ball.reset_position()
        scoreboard.r_point()

scoreboard.game_over()





screen.exitonclick()