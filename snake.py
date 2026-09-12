import turtle
import time
import random

screen = turtle.Screen()
screen.title("Snake - Python edition")
screen.bgpic("./images/bg.png")
screen.setup(width=600, height=600)
screen.tracer(0)

screen.register_shape("./images/apple.gif")
screen.register_shape("./images/snake_head.gif")
screen.register_shape("./images/snake_body.gif")


head = turtle.Turtle()
head.speed(0)
head.shape("./images/snake_head.gif")
head.penup()
head.goto(0, 0)
head.direction = "stop"

food = turtle.Turtle()
food.speed(0)
food.shape("./images/apple.gif")
food.penup()
food.goto(0, 100)

segments = []

score = 0
high_score = 0

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("blue")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Счёт: 0 Рекорд: 0", align="center", font=("Courier", 22, "bold"))


def go_up():
    if head.direction != "down":
        head.direction = "up"
        
def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"
        
def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    if head.direction == "down":
            head.sety(head.ycor() - 20)
    if head.direction == "left":
            head.setx(head.xcor() - 20)
    if head.direction == "right":
            head.setx(head.xcor() + 20)

screen.listen()
screen.onkeypress(go_up, "Up")
screen.onkeypress(go_down, "Down")
screen.onkeypress(go_left, "Left")
screen.onkeypress(go_right, "Right")

while True:
    screen.update()
    
    if(
        head.xcor() > 290
        or head.xcor() < -290
        or head.ycor() > 290
        or head.ycor() < -290
    ):
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        
        for segment in segments:
            segment.goto(1000, 1000)
        segment.clear()
        
        score = 0
        pen.clear()
        pen.write(
            f"Счёт: {score} Рекорд: {high_score}", align="center", font=("Courier", 22, "bold"),
        )

    if head.distance(food) < 20:
        x = random.randint(-14, 14) * 20
        y = random.randint(-14, 14) * 20
        food.goto(x, y)
        
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("./images/snake_body.gif")
        new_segment.penup()
        segments.append(new_segment)
        
        score += 1
        
        if score > high_score:
            high_score = score
        
        pen.clear()
        pen.write(
            f"Счёт: {score} Рекорд: {high_score}", align="center", font=("Courier", 22, "bold"),
        )
        
        
    for index in range(len(segments) -1, 0, -1):
        x = segments[index -1].xcor()
        y = segments[index -1].ycor()
        segments[index].goto(x, y)
        
    if len(segments) > 0:
        segments[0].goto(head.xcor(), head.ycor()) 
        
    move()
    
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            
            score = 0
            pen.clear()
            pen.write(
                f"Счёт: {score} Рекорд: {high_score}", align="center", font=("Courier", 22, "bold"),
            )
            
    time.sleep(0.1)