import turtle
import time

wn = turtle.Screen()
wn.title("Pong by Ryan")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle A 
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("red")
paddle_a.shapesize(stretch_wid=5, stretch_len=0.5)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("blue")
paddle_b.shapesize(stretch_wid=5, stretch_len=0.5)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("yellow")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.15
ball.dy = 0.35 

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)

# Pop ups
pop_up = turtle.Turtle()
pop_up.speed(0)
pop_up.color("green")
pop_up.penup()
pop_up.hideturtle()
pop_up.goto(0, 100)
def point_message(player):
  pop_up.write(f"Point to player {player}!", align = "center", font = ("Courier", 24, "bold"))
def get_ready():
  pop_up.write("GET READY", align = "center", font = ("Courier", 24, "normal"))

# Scores
player_a_score = 0
player_b_score = 0
def write_scores():
  pen.write(f"Player A: {player_a_score}                      Player B: {player_b_score}", align = "center", font = ("Courier", 18, "normal"))

# Functions
def paddle_a_up():
  y = paddle_a.ycor()
  if y < 300:  
    y += 20
  paddle_a.sety(y)

def paddle_a_down():
  y = paddle_a.ycor()
  if y > -300:
    y -= 20
  paddle_a.sety(y)

def paddle_b_up():
  y = paddle_b.ycor()
  if y < 300:  
    y += 20
  paddle_b.sety(y)

def paddle_b_down():
  y = paddle_b.ycor()
  if y > -300:
    y -= 20
  paddle_b.sety(y)

# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
start = True
while True:
  pop_up.clear()
  if start == True:
    time.sleep(1)
    pop_up.clear()
    pen.clear()
    write_scores()
    get_ready()
    time.sleep(1)
    pop_up.clear()
    start = False

  wn.update()

  # Move the ball
  ball.setx(ball.xcor() + ball.dx)
  ball.sety(ball.ycor() + ball.dy)

  # Border checking
  if ball.ycor() > 290: 
    ball.sety(290)
    ball.dy *= -1
  
  if ball.ycor() < -290: 
    ball.sety(-290)
    ball.dy *= -1

  if ball.xcor() > 390:
    ball.goto(0,0)
    player_a_score += 1
    point_message("A")
    ball.dx *= -1
    wn.update()
    start = True
  
  if ball.xcor() < -390:
    ball.goto(0,0)
    player_b_score += 1
    point_message("B")
    ball.dx *= -1
    wn.update()
    start = True

  # Paddle and ball collisions
  if (ball.xcor() >= 340 and ball.xcor() < 345) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
    ball.setx(340)
    ball.dx *= -1
  if (ball.xcor() <= -340 and ball.xcor() > -345) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
    ball.setx(-340)
    ball.dx *= -1
