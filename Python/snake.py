# Ivan Rodriguez, Andrea Yela, Salomon Dabbah

"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to arrow keys.

"""

from turtle import *
from random import randrange, choice
from freegames import square, vector


food = vector(0, 0)
snake = [vector(8, 0)]
aim = vector(0, -10)
writer = Turtle(visible = False)
style = ('Courier', 30, 'bold')


def SnakeFruitColor():
    PosibleColors = ['black','green','blue','yellow']
    snakeColor = choice(PosibleColors)
    fruitColor = choice(PosibleColors)
    if fruitColor == snakeColor:
        while fruitColor == snakeColor:
            fruitColor = choice(colorOptions)
    return snakeColor,fruitColor

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190


def show():
    writer.undo()
    writer.write('Game Over', font = style, align = 'center')
    clear()

def move():
    "Move snake forward one segment."
    color=colors
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        show()
        update()
        
        return
        

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10

    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, color[0])

    square(food.x, food.y, 9, color[1])
    update()
    ontimer(move, 100)

def main(): 
    setup(420, 420, 370, 0)
    hideturtle()
    tracer(False)
    global colors
    colors = SnakeFruitColor()
    listen()
    onkey(lambda: change(10, 0), 'Right')
    onkey(lambda: change(-10, 0), 'Left')
    onkey(lambda: change(0, 10), 'Up')
    onkey(lambda: change(0, -10), 'Down')
    onkey(lambda: change(10, 0), 'd')
    onkey(lambda: change(-10, 0), 'a')
    onkey(lambda: change(0,10), 'w')
    onkey(lambda: change(0, -10), 's')
    move()
    done()


main()
