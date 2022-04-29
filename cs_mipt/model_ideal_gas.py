import turtle


class Particle:
    dt = 1

    def __init__(self, x, y, vx, vy):
        self.turtle = turtle.Turtle()
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.turtle.penup()
        self.turtle.setpos(self.x, self.y)
        self.turtle.pendown()

    def move(self):
        self.x = self.x + self.dt * self.vx
        self.y = self.y + self.dt * self.vy
        self.turtle.setpos(self.x, self.y)


def turtle_pool():
    from random import randint
    import turtle

    number_of_turtles = 10
    steps_of_time_number = 100

    pool = [Particle(randint(-20, 20), randint(-20, 20), randint(-1, 1), randint(-1, 1)) for i in range(number_of_turtles)]

    for i in range(steps_of_time_number):
        for unit in pool:
            unit.move()


turtle_pool()
turtle.done()
