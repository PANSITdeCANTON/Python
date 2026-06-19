import turtle
import time 

sc = turtle.Screen()
sc.title("Pong Game")
sc.bgcolor("white")
sc.setup(width=1000, height=600)

#left paddle (player)
left_pad = turtle.Turtle()
left_pad.speed(0)
left_pad.shape("square")
left_pad.color("black")
left_pad.shapesize(stretch_wid=6, stretch_len=2)
left_pad.penup()
left_pad.goto(-400, 0)

#right paddle (AI)
right_pad = turtle.Turtle()
right_pad.speed(0)
right_pad.shape("square")
right_pad.color("black")
right_pad.shapesize(stretch_wid=6, stretch_len=2)
right_pad.penup()
right_pad.goto(400, 0)

#ball of circle shape
hit_ball = turtle.Turtle()
hit_ball.speed(20)
hit_ball.shape("circle")
hit_ball.color("black")
hit_ball.penup()
hit_ball.goto(0,0)
hit_ball.dx = 5
hit_ball.dy = -5

#scores
left_player = 0
right_player = 0

#display scores
sketch = turtle.Turtle()
sketch.speed(0)
sketch.color("Blue")
sketch.penup()
sketch.hideturtle()
sketch.goto(0,200)
sketch.write("Left Player: 0           Right Player: 0", align="center", font=("Courier", 24, "normal"))

#func to move paddle
def paddleaup():
    y = left_pad.ycor()
    if y < 250:
        y+=20
        left_pad.sety(y)
def paddleadown():
    y = left_pad.ycor()
    if y > -240:  # Limit paddle movement
        y -= 20
        left_pad.sety(y)

sc.listen()
sc.onkeypress(paddleaup, "w")
sc.onkeypress(paddleadown, "s")

# AI config: capped speed so the player can still win rallies
AI_SPEED = 5          # max y movement per frame, lower than the ball's effective dy
AI_REACT_ZONE = 0     # x-coordinate past which AI starts reacting (0 = always reacts)
AI_DEADZONE = 10       # ignore differences smaller than this to reduce jitter

def move_ai_paddle():
    # Only chase the ball when it's moving toward the AI side, for a more human feel
    if hit_ball.dx <= 0:
        return

    target_y = hit_ball.ycor()
    current_y = right_pad.ycor()
    diff = target_y - current_y

    if abs(diff) < AI_DEADZONE:
        return

    step = AI_SPEED if diff > 0 else -AI_SPEED
    new_y = current_y + step

    # Keep within the same bounds as the player paddle
    if new_y > 250:
        new_y = 250
    if new_y < -240:
        new_y = -240

    right_pad.sety(new_y)

# Main game loop
while True:
    sc.update()
    time.sleep(0.01)  # Add delay to make game smoother

    hit_ball.setx(hit_ball.xcor() + hit_ball.dx)
    hit_ball.sety(hit_ball.ycor() + hit_ball.dy)

    move_ai_paddle()

    # Checking borders
    if hit_ball.ycor() > 280:
        hit_ball.sety(280)
        hit_ball.dy *= -1

    if hit_ball.ycor() < -280:
        hit_ball.sety(-280)
        hit_ball.dy *= -1

    if hit_ball.xcor() > 500:
        hit_ball.goto(0, 0)
        hit_ball.dy *= -1
        left_player += 1
        sketch.clear()
        sketch.write("Left_player : {}    Right_player: {}".format(
            left_player, right_player), align="center",
            font=("Courier", 24, "normal"))

    if hit_ball.xcor() < -500:
        hit_ball.goto(0, 0)
        hit_ball.dy *= -1
        right_player += 1
        sketch.clear()
        sketch.write("Left_player : {}    Right_player: {}".format(
            left_player, right_player), align="center",
            font=("Courier", 24, "normal"))

    # Paddle ball collision
    if (hit_ball.xcor() > 360 and hit_ball.xcor() < 370) and \
            (hit_ball.ycor() < right_pad.ycor() + 50 and hit_ball.ycor() > right_pad.ycor() - 50):
        hit_ball.setx(360)
        hit_ball.dx *= -1

    if (hit_ball.xcor() < -360 and hit_ball.xcor() > -370) and \
            (hit_ball.ycor() < left_pad.ycor() + 50 and hit_ball.ycor() > left_pad.ycor() - 50):
        hit_ball.setx(-360)
        hit_ball.dx *= -1