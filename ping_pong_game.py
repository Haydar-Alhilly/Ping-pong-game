import turtle

# setting up the screen
box = turtle.Screen()
box.title("Ping Pong")
box.bgcolor("black")
box.setup(width=800, height=600)
box.tracer(0)

# setting up the first rocket
rocket1 = turtle.Turtle()
rocket1.speed(0)
rocket1.shape("square")
rocket1.color("blue")
rocket1.shapesize(stretch_wid=5, stretch_len=1)
rocket1.penup()
rocket1.goto(350, 0)
score1 = 0

# setting up the second rocket
rocket2 = turtle.Turtle()
rocket2.speed(0)
rocket2.shape("square")
rocket2.color("red")
rocket2.shapesize(stretch_wid=5, stretch_len=1)
rocket2.penup()
rocket2.goto(-350, 0)
score2 = 0

# setting up the ball
ball = turtle.Turtle()
ball.speed(1)
ball.shape("circle")
ball.color("green")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = 0.2

# setting up the score text
Score1 = turtle.Turtle()
Score1.speed(0)
Score1.color("blue")
Score1.penup()
Score1.hideturtle()
Score1.goto(100, 250)

Score2 = turtle.Turtle()
Score2.speed(0)
Score2.color("red")
Score2.penup()
Score2.hideturtle()
Score2.goto(-100, 250)


def rock1_move_up():
    y = rocket1.ycor()
    if y <= 240:
        y += 25
        rocket1.sety(y)


def rock1_move_down():
    y = rocket1.ycor()
    if y >= -230:
        y -= 25
        rocket1.sety(y)


def rock2_move_up():
    y = rocket2.ycor()
    if y <= 240:
        y += 25
        rocket2.sety(y)


def rock2_move_down():
    y = rocket2.ycor()
    if y >= -230:
        y -= 25
        rocket2.sety(y)


def borders():
    if ball.ycor() >= 290:
        ball.dy *= -1
    if ball.ycor() <= -290:
        ball.dy *= - 1


def if_goal():
    global score1, score2
    if ball.xcor() >= 390:
        score2 += 1
        Score2.clear()
        Score2.write("player2: {}".format(score2), align="center", font=("Courier", 20, "normal"))
        ball.goto(0, 0)
        ball.dx = -0.1
    if ball.xcor() <= -390:
        score1 += 1
        Score1.clear()
        Score1.write("player1: {}".format(score1), align="center", font=("Courier", 20, "normal"))
        ball.goto(0, 0)
        ball.dx = 0.1


def if_hit():
    if (340 >= ball.xcor() >= 330) and (
            rocket1.ycor() + 55 >= ball.ycor() >= rocket1.ycor() - 55):
        ball.dx *= -1
    if (-340 <= ball.xcor() <= -330) and (
            rocket2.ycor() + 55 >= ball.ycor() >= rocket2.ycor() - 55):
        ball.dx *= -1


# the main game loop
while True:
    box.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    box.onkeypress(rock1_move_up, "Up")
    box.onkeypress(rock1_move_down, "Down")
    box.onkeypress(rock2_move_up, "w")
    box.onkeypress(rock2_move_down, "s")
    box.listen()
    borders()
    if_goal()
    if_hit()
