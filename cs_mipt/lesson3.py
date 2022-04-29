import math
import turtle as tr



def tr_init():
    tr.shape('classic')
    tr.speed(5)
    tr.pendown()


#unit-длина поля цифры для написания почтового индекса
unit = 20
diag = math.sqrt(2 * unit**2)
gap = 5

"""
5---6
3---4
1---2
"""
def move_pos_5(init_x, init_y):
    tr.setpos(init_x, init_y + 2 * unit)

def move_pos_6(init_x, init_y):
    tr.setpos(init_x + unit, init_y + 2 * unit)

def move_pos_3(init_x, init_y):
    tr.setpos(init_x, init_y + unit)

def move_pos_4(init_x, init_y):
    tr.setpos(init_x + unit, init_y + unit)

def move_pos_1(init_x, init_y):
    tr.setpos(init_x, init_y)

def move_pos_2(init_x, init_y):
    tr.setpos(init_x + unit, init_y)

def draw_0(init_x, init_y):
    move_pos_5(init_x, init_y)
    move_pos_6(init_x, init_y)
    move_pos_2(init_x, init_y)
    move_pos_1(init_x, init_y)

def draw_1(init_x, init_y):
    tr.penup()
    move_pos_3(init_x, init_y)
    tr.pendown()
    move_pos_6(init_x, init_y)
    move_pos_2(init_x, init_y)

def draw_2(init_x, init_y):
    tr.penup()
    move_pos_5(init_x, init_y)
    tr.pendown()
    move_pos_6(init_x, init_y)
    move_pos_4(init_x, init_y)
    move_pos_1(init_x, init_y)
    move_pos_2(init_x, init_y)

def draw_3(init_x, init_y):
    move_pos_4(init_x, init_y)
    move_pos_3(init_x, init_y)
    move_pos_6(init_x, init_y)
    move_pos_5(init_x, init_y)

def draw_4(init_x, init_y):
    tr.penup()
    move_pos_5(init_x, init_y)
    tr.pendown()
    move_pos_3(init_x, init_y)
    move_pos_4(init_x, init_y)
    move_pos_6(init_x, init_y)
    move_pos_2(init_x, init_y)

def draw_5(init_x, init_y):
    move_pos_2(init_x, init_y)
    move_pos_4(init_x, init_y)
    move_pos_3(init_x, init_y)
    move_pos_5(init_x, init_y)
    move_pos_6(init_x, init_y)


def draw_6(init_x, init_y):
    move_pos_2(init_x, init_y)
    move_pos_4(init_x, init_y)
    move_pos_3(init_x, init_y)
    move_pos_6(init_x, init_y)
    move_pos_3(init_x, init_y)
    move_pos_1(init_x, init_y)


def draw_7(init_x, init_y):
    move_pos_3(init_x, init_y)
    move_pos_6(init_x, init_y)
    move_pos_5(init_x, init_y)


def draw_8(init_x, init_y):
    move_pos_2(init_x, init_y)
    move_pos_6(init_x, init_y)
    move_pos_5(init_x, init_y)
    move_pos_1(init_x, init_y)
    move_pos_3(init_x, init_y)
    move_pos_4(init_x, init_y)

def draw_9(init_x, init_y):
    move_pos_4(init_x, init_y)
    move_pos_3(init_x, init_y)
    move_pos_5(init_x, init_y)
    move_pos_6(init_x, init_y)
    move_pos_4(init_x, init_y)

tr_init()
#show_Brownian_motion()
#draw_1(0,0)
#tr.setpos(50, 50)
#tr.home()

postcode_list = [x for x in input()]

for i in range(len(postcode_list)):
    tr.penup()
    tr.home()
    init_x = i * (unit + gap)
    tr.setpos(init_x, 0)
    tr.pendown()
    print('draw_' + postcode_list[i] + '(' + str(init_x) + ', 0)')
    eval('draw_' + postcode_list[i] + '(' + str(init_x) + ', 0)')

tr.done()