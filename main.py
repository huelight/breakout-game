import turtle
import random
import time

# Set up the screen
wn = turtle.Screen()
wn.title("Breakout Game")
wn.bgcolor("black")
wn.setup(width=600, height=600)

# Paddle
paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

# Ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.speed(40)
ball.goto(0, 0)
ball.dx = 2
ball.dy = -2

# Bricks
bricks = []
for _ in range(5):
    brick = turtle.Turtle()
    brick.shape("square")
    brick.color("white")
    brick.penup()
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    brick.goto(x, y)
    bricks.append(brick)


# Paddle movement
def paddle_right():
    x = paddle.xcor()
    x += 20
    if x > 290:
        x = 290
    paddle.setx(x)


def paddle_left():
    x = paddle.xcor()
    x -= 20
    if x < -290:
        x = -290
    paddle.setx(x)


# Keyboard bindings
wn.listen()
wn.onkeypress(paddle_right, "Right")
wn.onkeypress(paddle_left, "Left")

# Main game loop
while True:
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.xcor() > 290 or ball.xcor() < -290:
        ball.dx *= -1

    if ball.ycor() > 290:
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.goto(0, 0)
        ball.dy *= -1

    # Paddle collision
    if (-240 > ball.ycor() > -250) and (
            paddle.xcor() - 50 < ball.xcor() < paddle.xcor() + 50):
        ball.dy *= -1

    # Brick collision
    for brick in bricks:
        if (brick.ycor() + 20 > ball.ycor() > brick.ycor() - 20) and (
                brick.xcor() - 20 < ball.xcor() < brick.xcor() + 20):
            brick.goto(1000, 1000)  # Move the brick out of the screen
            ball.dy *= -1

    # Update screen
    wn.update()
