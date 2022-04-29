import matplotlib.pyplot as plt
import numpy as np

x = 0

def func(x):
    # лог по основанию 2 = np.log(x) / np.log(2). log натуральный
    y = (1/(np.power(np.e, np.sin(x)) + 1))/(5/4 + 1/(5*x))
    return np.log(y) / np.log(1 + x * x)

def func_1(x):
    a = (x**2 + 1) *np.exp((-1) * np.absolute(x)/10)
    b = 1 + np.tan(1/(1 + np.power(np.sin(x), 2)))
    return np.log(a)/np.log(b)

def func_6(x, a, b):
    n = np.arange(0, 10, 1)
    print(n)
    #return np.sum(np.power(b, n) * np.cos(np.power(a, n) * np.pi * x))

def exercise_1(array):
    y = [func(x) for x in array]
    print(np.log(array))
    print(y)

def exercise_2():
    x = np.arange(-10, 10.01, 0.01)
    plt.plot(x, x**2 - x - 6, x, x * 0)
    #plt.axis(plt.axis('equal'))
    plt.grid(True)
    plt.show()

def exercise_3():
    x = np.arange(-10, 10.01, 0.01)
    plt.plot(x, func_1(x))
    plt.grid(True)
    plt.show()

def exercise_4():
    with plt.xkcd():
        plt.pie([70, 10, 10, 10], labels=('В комментариях', 'В Ираке', 'В Сирии', 'В Афганистане'))
        plt.title('Где ведутся самые ожесточенные бои')
    plt.show()

def exercise_5():
    s = str(input())
    x = np.arange(-10, 10.01, 0.01)
    command = 'plt.plot(x, ' + s + ')'

    eval(command)
    plt.show()

def exercise_6():
    #print(func_6(3,3,3))
    x = np.arange(-1, 1.01, 0.01)
    plt.plot(x, func_6(x, 3, 0.5))
    plt.show()

def lesson_1(array):
    #exercise_1([1, 100, 1000])
    #exercise_2()
    #exercise_3()
    exercise_6()
print(func(1))