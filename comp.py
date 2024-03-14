
import turtle
import time
import random

WIDTH, HEIGHT= 400,400
COLORS=['red','green', 'blue','pink', 'black','orange','yellow', 'purple','brown','cyan']
def get_number_of_racers():
    racers=0
    while True:
        racers=input('Enter the number of racers (2-10):')
        if racers.isdigit():
            racers=int(racers)
        else:
            print("Enter a numeric number... Try again")
            continue
        if 2<=racers<=10:
            return racers
        else:
            print("Number nt in range of 2 and 10: Try Again")

def race(colors):
    turtles=create_turtles(colors)

    while True:
        for racer in turtles:
            distance=random.randrange(1,20)
            racer.forward(distance)
            x,y=racer.pos()
            if y>=HEIGHT//2-10:
                return colors[turtles.index(racer)]

def create_turtles(colors):
    turtles= []
    spacingx=WIDTH // (len(colors)+1)
    for i, color in enumerate(colors):
        runner=turtle.Turtle()
        runner.color(color)
        runner.shape('turtle')
        runner.left(90)
        runner.penup()
        runner.setpos(-WIDTH//2+(i+1)*spacingx,-HEIGHT//2+20)
        runner.pendown()
        turtles.append(runner)
    return turtles

def init_turtle():
    screen=turtle.Screen()
    screen.setup(WIDTH,HEIGHT)
    screen.title("The Turtle Racing!")

racers=get_number_of_racers()
init_turtle()
random.shuffle(COLORS)
colors=COLORS[:racers]

winner = race(colors)
print("The winner is the turtle with Color: ", winner)
time.sleep(3)



