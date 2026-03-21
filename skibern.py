import turtle

t = turtle.Turtle()
t.speed(8)
screen = turtle.Screen()
screen.setup(900,900)
screen.bgcolor("sky blue")   # Soft clean background EAF6FF 

def move(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

def circle_fill(color, r):
    t.color(color)
    t.begin_fill()
    t.circle(r)
    t.end_fill()

# HEAD (Sky Blue)
move(0,-230)
circle_fill("#33B5FF",230)

# FACE (White)
move(0,-190)
circle_fill("white",190)

# EYES
for x in [-60, 60]:
    move(x,170)
    t.color("white")
    t.begin_fill()
    t.circle(55)
    t.end_fill()

# Eye Balls
for x in [-25,25]:
    move(x,145)
    t.color("black") 
    t.begin_fill()
    t.circle(14)
    t.end_fill()

# NOSE
move(0,80)
circle_fill("red",30)

# Nose Line
t.color("black")
move(0,80)
t.setheading(-90)
t.pensize(4)
t.forward(150)

# MOUTH
move(-140,10)
t.setheading(-60)
t.circle(200,120)

# Whiskers
lines = [( -170,60,0,140 ),
         ( -170,10,0,140 ),
         ( -170,-40,0,140 ),
         ( 170,60,180,140 ),
         ( 170,10,180,140 ),
         ( 170,-40,180,140 )]

t.pensize(4)
for x,y,ang,len in lines:
    move(x,y)
    t.setheading(ang)
    t.forward(len)

# BODY BLUE
move(-150,-230)
t.color("#33B5FF")
t.begin_fill()
t.setheading(-90)
t.forward(260)
t.setheading(0)
t.forward(300)
t.setheading(90)
t.forward(260)
t.setheading(180)
t.forward(300)
t.end_fill()

# BELLY WHITE
move(-115,-230)
t.color("white")
t.begin_fill()
t.setheading(-90)
t.forward(200)
t.setheading(0)
t.forward(230)
t.setheading(90)
t.forward(200)
t.setheading(180)
t.forward(230)
t.end_fill()

# POCKET
move(-70,-300)
t.color("yellow") #yaha white the pahle 
t.begin_fill()
t.setheading(-90)
t.circle(80,180)
t.end_fill()

# BELL
move(0,-230)
circle_fill("yellow",25) 

t.hideturtle()
turtle.done() 

































