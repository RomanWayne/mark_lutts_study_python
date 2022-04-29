# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# f = open('data.txt', 'w')
# f.write('Hello, epta')
# f.close()

print(hex(75))
print(oct(75))
print(bin(75))
import sys

b = """ублюдок
мать твою
а ну иди сюда"""
# l=list()
# print(help(l.m))

import random


def saper():
    dim = [int(i) for i in input().split()]
    coor = []
    for i in range(0, dim[2]):
        # coor.append(tuple(int(j) for j in input().split()))
        coor.append((random.randint(0, dim[0] - 1), random.randint(0, dim[1] - 1)))
    print(coor)
    field = []
    line = []
    for i in range(0, dim[0]):
        for j in range(0, dim[1]):
            if (i, j) in coor:
                line.append('*')
            else:
                line.append(0)
        field.append(line[:])
        line.clear()
    for i in range(0, dim[0]):
        for j in range(0, dim[1]):
            if field[i][j] == '*':
                continue
            if i - 1 >= 0:
                if field[i - 1][j] == '*':
                    field[i][j] = field[i][j] + 1
                if j - 1 >= 0:
                    if field[i - 1][j - 1] == '*':
                        field[i][j] = field[i][j] + 1
                if j + 1 <= dim[1] - 1:
                    if field[i - 1][j + 1] == '*':
                        field[i][j] = field[i][j] + 1

            if i + 1 <= dim[0] - 1:
                if field[i + 1][j] == '*':
                    field[i][j] = field[i][j] + 1
                if j - 1 >= 0:
                    if field[i + 1][j - 1] == '*':
                        field[i][j] = field[i][j] + 1
                if j + 1 <= dim[1] - 1:
                    if field[i + 1][j + 1] == '*':
                        field[i][j] = field[i][j] + 1
            if j - 1 >= 0:
                if field[i][j - 1] == '*':
                    field[i][j] = field[i][j] + 1
            if j + 1 <= dim[1] - 1:
                if field[i][j + 1] == '*':
                    field[i][j] = field[i][j] + 1
    for line in field:
        print(line)

def stepik_task_2_6_10():
    line = ''
    matrix = []
    new_matrix = []
    while True:
        line = input()
        #[int(i) for i in input().split(' ')]
        if line != 'end':
            matrix.append([int(i) for i in line.split(' ')])
            new_matrix.append([int(0) for i in line.split(' ')])
        else:
            break
    n = len(matrix)
    m = len(matrix[0])
    for i in range(0, n):
        for j in range(0, m):
            if j - 1 >= 0:
                new_matrix[i][j] = new_matrix[i][j] + matrix[i][j - 1]
            else:
                new_matrix[i][j] = new_matrix[i][j] + matrix[i][m - 1]
            if j + 1 < m:
                new_matrix[i][j] = new_matrix[i][j] + matrix[i][j + 1]
            else:
                new_matrix[i][j] = new_matrix[i][j] + matrix[i][0]

            if i - 1 >= 0:
                new_matrix[i][j] = new_matrix[i][j] + matrix[i - 1][j]
            else:
                new_matrix[i][j] = new_matrix[i][j] + matrix[n - 1][j]
            if i + 1 < n:
                new_matrix[i][j] = new_matrix[i][j] + matrix[i + 1][j]
            else:
                new_matrix[i][j] = new_matrix[i][j] + matrix[0][j]
    for i in range(0, n):
        for j in range(0, m):
            print(new_matrix[i][j], end=' ')
        print()

def stepik_task_2_6_11():
    line = []
    matrix = []
    n = int(input())
    for i in range(n):
        for j in range(n):
            line.append(0)
        matrix.append(line[:])
        line.clear()
    direction = {0: [0, 1], 90: [1, 0], 180: [0, -1], 270: [-1, 0]}
    angle = 0
    current_row = 0
    current_col = 0
    for i in range(0, n ** 2):
        matrix[current_row][current_col] = i + 1
        if current_row + direction.get(angle % 360)[0] >= n or current_col + direction.get(angle%360)[1] >= n:
            angle = angle + 90
        elif matrix[current_row + direction.get(angle % 360)[0]][current_col + direction.get(angle%360)[1]] != 0:
            angle = angle + 90
        current_row = current_row + direction.get(angle % 360)[0]
        current_col = current_col + direction.get(angle % 360)[1]

    for i in range(0, n):
        for j in range(0, n):
            print(matrix[i][j], end=' ')
        print()



def modify_list_stepik_task_3_1_9(l):
    for i in range(len(l) - 1, -1, -1):
        print(i)
        if l[i] % 2 == 0:
            l[i] = int(l[i] / 2)
        else:
            l.pop(i)

def update_dictionary_stepik_task_3_2_7(d, key, value):
    if key in d.keys():
        d.get(key).append(value)
    else:
        # s = d.setdefault(key, list(value))
        # if s is not None:
        #     s.append(value)
        if key * 2 in d.keys():
            d.get(key * 2).append(value)
        else:
            d[key * 2] = [value]

def update_dictionary_stepik_task_3_2_7():
    d = {}
    s = [s.lower() for s in input().split(' ')]
    for i in s:
        cnt = d.setdefault(i, 0)
        d[i] = d[i] + 1
    for key, value in d.items():
        print(str(key) + ' ' + str(value))


def update_dictionary_stepik_task_3_2_8():
    d = {}
    n = int(input())
    for i in range(n):
        x = int(input())
        if x in d.keys():
            print(d.get(x))
        else:
            fx = 1231
            d[x] = fx
            print(fx)

#with open('data.txt', 'r') as inf:
#    s = inf.readline().strip()


def decode_stepik_task_3_4_2():
    line = input().strip() + '\t'
    result = ''
    #for i in range(0, len(line)):
    i = 0
    of = 1
    cnt_ch = ''
    while True:
        ch = line[i]
        while True:
            if 48 <= ord(line[i + of]) <= 57:
                cnt_ch = cnt_ch + line[i + of]
                of += 1
            else:
                cnt = int(cnt_ch)
                cnt_ch = ''
                i = i + of
                of = 1
                break
        c = ch * cnt
        result = result + c
        if line[i] == '\t':
            break
    print(result)

def decode_stepik_task_3_4_3():
    line = [s.lower() for s in input().replace('\r\n', ' ').split(' ')]
    word_dict = {}
    print(line)
    idx_max = ''
    maxima = 1
    for word in line:
        if word in word_dict.keys():
            if word_dict[word] + 1 > maxima or word_dict[word] + 1 == maxima and word_dict[word] < word_dict[idx_max]:
                idx_max = word
                maxima = word_dict[word] + 1
            word_dict[word] = word_dict[word] + 1
        else:
            word_dict[word] = 1
    print(idx_max + ' ' + str(word_dict[idx_max]))

def decode_stepik_task_3_4_4():
    dct = {}
    lst = []
    student_cnt = 0
    with open('data.txt', 'r') as inp:
        for line in inp:
            lst = line.strip().split(';')
            dct[lst[0]] = lst[1:4]
            student_cnt += 1
    sum_grade = [0, 0, 0]

    with open('out.txt', 'w') as out:
        for i in dct.keys():
            print((int(dct[i][0]) + int(dct[i][1]) + int(dct[i][2])) / 3)
            out.write(str((int(dct[i][0]) + int(dct[i][1]) + int(dct[i][2])) / 3))
            out.write('\n')
            sum_grade[0] = sum_grade[0] + int(dct[i][0])
            sum_grade[1] = sum_grade[1] + int(dct[i][1])
            sum_grade[2] = sum_grade[2] + int(dct[i][2])

        for i in sum_grade:
            out.write(str(i / student_cnt))
            out.write(' ')


def decode_stepik_task_3_6_3():
    import requests
    r = requests.get('https://stepic.org/media/attachments/course67/3.6.3/699991.txt')
    while (r.text.split(' ') != 'We'):
        print('https://stepic.org/media/attachments/course67/3.6.3/' + r.text)
        r = requests.get('https://stepic.org/media/attachments/course67/3.6.3/' + r.text)
    print(len(r.text))

def decode_stepik_task_3_7_1():
    teams = {}
    n = int(input())
    for i in range(0, n):
        inp = input().split(';')
        team1 = inp[0]
        team2 = inp[2]
        score1 = int(inp[1])
        score2 = int(inp[3])

        if team1 not in teams.keys():
            teams[team1] = [0, 0, 0, 0, 0]
        if team2 not in teams.keys():
            teams[team2] = [0, 0, 0, 0, 0]
        if score1 > score2:
            teams[team1] = [teams[team1][0] + 1, teams[team1][1] + 1, teams[team1][2], teams[team1][3], teams[team1][4] + 3]
            teams[team2] = [teams[team2][0] + 1, teams[team2][1], teams[team2][2], teams[team2][3] + 1, teams[team2][4]]
        elif score1 < score2:
            teams[team2] = [teams[team2][0] + 1, teams[team2][1] + 1, teams[team2][2], teams[team2][3], teams[team2][4] + 3]
            teams[team1] = [teams[team1][0] + 1, teams[team1][1], teams[team1][2], teams[team1][3] + 1, teams[team1][4]]
        elif score1 == score2:
            teams[team1] = [teams[team1][0] + 1, teams[team1][1], teams[team1][2] + 1, teams[team1][3], teams[team1][4] + 1]
            teams[team2] = [teams[team2][0] + 1, teams[team2][1], teams[team2][2] + 1, teams[team2][3], teams[team2][4] + 1]

    for i in teams:
        print(i, end=':')
        for j in teams.get(i):
            print(j, end = ' ')
        print()


def decode_stepik_task_3_7_2():
    src = input()
    dst = input()
    ccode = {}
    deccode = {}

    for i in range(0, len(src)):
        ccode[src[i]] = dst[i]
        deccode[dst[i]] = src[i]

    word_to_code = input()
    word_to_decode = input()
    for c in word_to_code:
        print(ccode.get(c), end='')
    print()

    for c in word_to_decode:
        print(deccode.get(c), end='')

def decode_stepik_task_3_7_3():
    dict_correct = {}
    dict_incorrect = {}
    d = int(input())
    for i in range(d):
        dict_correct[input().lower()] = 1

    l = int(input())
    for i in range(l):
        words = input().lower().split(' ')
        for word in words:
            if word not in dict_correct:
                dict_incorrect[word] = 1

    for i in dict_incorrect.keys():
        print(i)

def decode_stepik_task_3_7_4():
    rules = {'север': [0, 1], 'юг': [0, -1], 'восток': [1, 0], 'запад': [-1, 0]}
    coor = [0, 0]
    n = int(input())
    for i in range(n):
        comanda = input().split()
        coor[0] = coor[0] + rules[comanda[0]][0] * int(comanda[1])
        coor[1] = coor[1] + rules[comanda[0]][1] * int(comanda[1])
    print(str(coor[0]) + ' ' + str(coor[1]))

def decode_stepik_task_3_7_4():
    d = {}
    with open('dataset_3380_5.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            lst = line.split('\t')
            print(lst)
            if lst[0] not in d:
                d[lst[0]] = [int(lst[2])]
            else:
                d.get(lst[0]).append(int(lst[2]))
    
    for i in range(1, 12):
        if str(i) not in d.keys():
            print(str(i) + ' -')
        else:
            print(str(i) + ' ' + str(sum(d.get(str(i))) / len(d.get(str(i)))))


# with open('sql.txt', 'r', encoding="utf8") as inp:
#     for line in inp:
#         print(line, end = '')

#списковое включение
s = [1,2,3, 3,4]
h = [1,2,3, 3, 3 ]
a = 'abc'
b = 'ab'
x = 1
y = 2
x, y = 2, 1
print(x, y)

def intersect(f1, f2):
    lst = []
    for i in f1:
        for j in f2:
            if i == j:
                lst.append(j)
    return lst
def rr():
    b='ss'
    print(b)
rr()
print(b)

print(intersect('huesos','fuck you'))


X = 5
def setX(x):
    global X
    def setPlusX(x):
        print(x)
        nonlocal S
        S = x + 1
    S = 0
    setPlusX(x)
    X = S

def tester(start):
    state = start
    def nested(label):
        print(label, state)
    return nested()


def sumtree(L):
    tot = 0
    for x in L:
        if not isinstance(x, list):
            tot += x
        else:
            tot += sumtree(x) # рекурсия стек вызовов LIFO
    return tot

def sumtree_1(L): #Явная очередь с обходом в ширину FIFO
    tot = 0
    items = list(L)
    while items:
        front = items.pop(0) #удаление и возврат первого элта
        if not isinstance(front, list):
            tot += front
        else:
            items.extend(front) #добавление в конец списка
    return tot

def sumtree_2(L): #Явная стек с обходом в глубину LIFO
    tot = 0
    items = list(L)
    while items:
        front = items.pop(0) #удаление и возврат первого элта
        if not isinstance(front, list):
            tot += front
        else:
            items = front + items[:]
    return tot

def echo(msg):
    print(msg)

echo('direct')
x = echo
x('indirect')

def indirect(func, arg):
    func(arg)

indirect(echo, 'argument call')

#первоклассная объектная модель
def make(label):
    i = 0
    def echo(msg):
        nonlocal i
        i += 1
        print('Вызов ' + str(i) + ' процедуры ' + label + ': ' + msg)
    return echo

f = make('helloworld')
f('russia')
f('china')
f('usa')

def my_map(func, l):
    ret = []
    for i in l:
        ret.append(func(i))
    return ret

def my_filter(func, l):
    ret = []
    for i in l:
        if func(l):
            ret.append(i)
    return ret

#my_map(echo, [1,3, 'fffff'])

#my_filter(echo, [1,2,3])

print(sys.path)


