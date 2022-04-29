from random import *
import math
import turtle
import this


#tr = turtle.Turtle()

def draw_s():
    turtle.shape('turtle')
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)


def tr_init():
    turtle.shape('turtle')
    turtle.speed(5)
    turtle.pendown()



def draw_regular_polygon(n, side_len):
    for i in range(n):
        turtle.forward(side_len)
        turtle.left(360 / n)


def draw_nested_squares(n):
    for i in range(n):
        draw_regular_polygon(4, (i + 1) * n)
        turtle.penup()
        turtle.right(90)
        turtle.forward(n / 2)
        turtle.right(90)
        turtle.forward(n / 2)
        turtle.left(180)
        turtle.pendown()


def draw_circle(r):
    num_fr = 50
    draw_regular_polygon(num_fr, 2 * r * math.pi / num_fr)


def draw_spider(n, leg_length):
    for i in range(n):
        turtle.forward(leg_length)
        turtle.clone()
        turtle.left(180)
        turtle.forward(leg_length)
        turtle.left(180 - (360 / n))


def draw_spider(n, leg_length):
    for i in range(n):
        turtle.forward(leg_length)
        turtle.clone()
        turtle.left(180)
        turtle.forward(leg_length)
        turtle.left(180 - (360 / n))

def draw_spiral(n, length = 3, a = 0.1, b = 0.002):
    """Draws an Archimedian spiral starting at the origin.
        Args:
          n: how many line segments to draw
          length: how long each segment is
          a: how loose the initial spiral starts out (larger is looser)
          b: how loosly coiled the spiral is (larger is looser)
        http://en.wikipedia.org/wiki/Spiral
        """
    theta = 0.0
    for i in range(n):
        turtle.fd(length)
        dtheta = 1 / (a + b * theta)

        turtle.lt(dtheta)
        theta += dtheta

def draw_square_spiral(n, a, initial_length = 5):
    """Draws an square spiral starting at the origin.
        Args:
          n: how many lines in spiral
          a: gap between parralel lines
        """
    for i in range(n):
        turtle.forward((initial_length + i * a / 2))
        turtle.left(90)

def calc_param(n, leg_length):
    print(math.tan(180/(n+1)), math.sin(180/n))
    new_leg_length = 2 * math.tan(math.pi/(n+1)) * leg_length / (2 * math.sin(math.pi/n))
    delta_r = new_leg_length / (2 * math.sin(math.pi/(n+1))) - leg_length / (2 * math.sin(math.pi/n))
    return new_leg_length, delta_r

def draw_nested_polygons():
    leg_length = 100
    for i in range(3, 10):
        turtle.left(360 / i + (180 - (360 / i)) / 2)
        draw_regular_polygon(i, leg_length)
        turtle.right(360 / i + (180 - (360 / i)) / 2)
        turtle.penup()
        leg_length, delta_r = calc_param(i, leg_length)
        turtle.forward(delta_r)
        turtle.pendown()


def draw_flower(n, r):
    for i in range(n):
        draw_circle(r)
        turtle.left(360 / n)


def draw_butterfly(n, radius):
    for i in range(n):
        draw_circle(radius)
        turtle.left(180)
        draw_circle(radius)
        radius += 10


def draw_spring(n, big_radius, small_radius):
    turtle.left(90)
    for i in range(n):
        turtle.circle(big_radius, 180)
        turtle.circle(small_radius, 180)


def draw_star(n, leg):
    for i in range(n):
        turtle.forward(leg)
        turtle.right(180 - (180 / n))


def draw_Brownian_motion(turtle):
    move_cnt = randint(100, 200)
    for i in range(move_cnt):
        turtle.forward(randint(1, 50) * 1.0)
        turtle.left(360 * random())


def draw_bouncing_ball(vx, vy, g = -9.81, dt = 0.1):
    x = y = 0
    prev_x = prev_y = -1
    while abs(x-prev_x) > 1 or y - prev_y != 0:
        prev_x = x
        prev_y = y

        # уравнение движения
        x = x + vx * dt
        vy = vy + g * dt
        y = y + vy * dt + g * dt**2/2

        if y <= 0:
            vy = (-0.8) * vy #неупругий удар
            y = 0

        #горизонтальная скорость тоже уменьшается
        vx = 0.999 * vx

        turtle.setpos(x, y)

#def turtle_




#tr_init()
#draw_nested_polygons()
#draw_flower(5, 50)
#draw_butterfly(4, 50)
#draw_spring(6, 50, 10)
#draw_star(11, 100)
#draw_bouncing_ball(10,50)

turtle_pool()
turtle.done()