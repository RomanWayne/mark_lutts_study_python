import pygame
from pygame.draw import *

# После импорта библиотеки, необходимо её инициализировать:
pygame.init()

# И создать окно:
#screen = pygame.display.set_mode((300, 200))

# здесь будут рисоваться фигуры
# ...

# после чего, чтобы они отобразились на экране, экран нужно обновить:
#pygame.display.update()
# Эту же команду нужно будет повторять, если на экране происходят изменения.

#clock = pygame.time.Clock()
#clock.tick(30)

# Наконец, нужно создать основной цикл, в котором будут отслеживаться
# происходящие события.
# Пока единственное событие, которое нас интересует - выход из программы.
#while True:
#    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#            pygame.quit()


def exercise_1():
    pygame.init()

    FPS = 30
    screen = pygame.display.set_mode((400, 400))

    x1 = 100;
    y1 = 100
    x2 = 300;
    y2 = 200
    N = 10
    color = (255, 255, 255)
    rect(screen, color, (x1, y1, x2 - x1, y2 - y1), 2)
    h = (x2 - x1) // (N + 1)
    x = x1 + h
    for i in range(N):
        line(screen, color, (x, y1), (x, y2))
        x += h

    pygame.display.update()
    clock = pygame.time.Clock()
    finished = False

    pygame.draw.rect

'''    while not finished:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True'''

    pygame.quit()


exercise_1()
