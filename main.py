from turtle import * 
from random import *
from time import *

tank_a = Turtle()
tank_b = Turtle()
shell = Turtle()
shell.ht()
shell.shape('circle')


def draw_landscape():
  box = Turtle()
  box.ht()
  box.speed(100)
  box.color('gray')
  box.penup()
  box.goto(-500,-200)
  box.pendown()
  for i in range(0,20):
    box.forward(50)
    box.left(90)
    box.forward(10)
    box.forward(-10)
    box.right(90)
    if i == 9:
      wall_h = randint(80,200)
      box.pensize(10)
      box.left(90)
      box.forward(wall_h)
      box.forward(-wall_h)
      box.right(90)
      box.pensize(1)
  return wall_h
    
def place_tank_a():
  tank_a.color('red')
  tank_a.speed(100)
  tank_a.shape('square')
  tank_a.penup()
  x = randint(-480,-100)
  tank_a.goto(x,-190)

def place_tank_b():
  tank_b.color('blue')
  tank_b.speed(100)
  tank_b.shape('square')
  tank_b.penup()
  x = randint(100,480)
  tank_b.goto(x,-190)


def launch(name, my_tank, enemy_tank, shell, barrier, side):
  import math
  shell.speed(10)
  shell.penup()

  if side == 'left':
    shell.pencolor('red')
    p = 1
  else:
    shell.pencolor('blue')
    p = -1
  
  speed = int(input(name + ' enter speed 1-100: '))
  angle = int(input(name + ' enter angle 1-90: '))
  move = int(input(name + ' enter a movement 1-1000(Moving Forward) -1 - -1000(Moving Backwards): '))
  x_offset = my_tank.xcor()
  y_offset = my_tank.ycor()
  shell.goto(x_offset, y_offset)
  if my_tank == tank_a:
    my_tank.goto(my_tank.xcor() + 0. + move, my_tank.ycor())
  if my_tank == tank_b:
    my_tank.goto(my_tank.xcor() + -0. + move, my_tank.ycor())
  shell.st()
  t = 0
  x = 0
  y = 0
  shell.pendown()
  target_hit = False
  while y> -5 and target_hit == False:
    t += 0.1
    x = p* speed * math.cos(math.radians(angle))*t
    y = speed * math.sin(math.radians(angle))*t - 5*t**2
    shell.goto(x + x_offset , y + y_offset)
    if abs(x+x_offset) < 10 and y + y_offset < barrier-190:
      print('BARRIER HIT')
      break
    if abs(shell.xcor() - enemy_tank.xcor()) <10:
      if abs(shell.ycor() - enemy_tank.ycor()) <10:
        target_hit = True
        print('TARGET HIT!')
        print(name + ' is the WINNER!!!')
        break
  shell.penup()

  if target_hit:
    return False
  else:
    return True


if tank_a.xcor()  <= -500:
  tank_a.goto(-499, tank_a.ycor())

if tank_b.xcor()  <= -500:
  tank_b.goto(-499, tank_b.ycor())


def menu(h):
  print(h)
  t1 = input('Team 1 enter your name: ')
  t2 = input('Team 2 enter your name: ')
  turn = choice([t1,t2])
  gameOn = True
  while gameOn:
    if turn == t1:
      gameOn = launch(t1, tank_a, tank_b, shell, h, 'left')
      sleep(3)
      if tank_a.xcor()  <= -500:
        tank_a.goto(-499, tank_a.ycor())
      turn = t2
    else:
      gameOn = launch(t2, tank_b, tank_a, shell, h, 'right')
      sleep(3)
      if tank_b.xcor()  <= -500:
        tank_b.goto(-499, tank_b.ycor())
      turn = t1
    
h = draw_landscape()
place_tank_a()
place_tank_b()
menu(h)