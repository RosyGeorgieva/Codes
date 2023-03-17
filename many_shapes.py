import turtle
import random

turtle.Screen().bgcolor('light steel blue')
t = turtle.Turtle()
t.pensize(3)

def random_square(lenth, sides):    # Създава многоъгълникa
      for i in range(sides):
            t.fd(lenth)
            t.lt(360/sides)

def goto(x, y):                     # Позиция на фигурата
      t.up()
      t.goto(x, y)
      t.down()

for i in range(50):
    color = ['magenta','yellow','green', 'blue', 'orange', 'indigo','red', 'purple','cyan', 'deep pink']
    t.pencolor(color[i % 10])
    random_square(random.randint(10, 50), random.randint(3, 12))
    goto(random.randint(-250, 250), random.randint(-250, 250))

    if t.pos()[0] >= 250 or t.pos()[0] <= -250 :
        goto(t.pos()[0]-100, t.pos()[1]-100)
        continue
    elif t.pos()[1] >= 250 or t.pos()[1] <= -250:
        goto(t.pos()[0]-100, t.pos()[1]- 100)
        continue
# Write your code here :-)
