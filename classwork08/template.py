import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
def task1():
    a = int(input())
    b = int(input())
    print(a ** 2 + b ** 2)

def task2():
    a = input()
    n = 0
    for i in a:
        if ord(i) < 65 or (ord(i) > 90 and ord(i) < 97) or ord(i) > 122:
            n += 1
    print(n)

def task3():
    a = input().split()
    c = 0
    for i in a:
        if len(i) >= 3:
            if i[0:3] == 'Abo':
                c += 1
    print(c)

def task4(generator):
    # TODO: четвертое задание

def task5(list_of_smth):
    print(list_of_smth[5:(len(list_of_smth)-2):2])

def task6(list1, list2, list3, list4):
    a = (set(list1) & set(list2)) | (set(list3) & set(list4))
    print(a)

def task7():
    np.random.seed(11)
    array = np.random.randint(49, size=49)
    matrix = array.reshape(7, 7)
    matrix = np.delete(matrix, 6, 0)
    matrix = np.delete(matrix, 6, 1)
    print(matrix)
    print(np.linalg.det(matrix))

def task8(f, min_x, max_x, N, min_y, max_y):
    plt.minorticks_on()
    plt.grid(b=True, which='major', axis='both', alpha=1)
    plt.grid(b=True, which='minor', axis='both', alpha=0.5)
    x = np.linspace(min_x, max_x, N)
    y = f(x)
    # y_d = np.diff(y) / np.diff(x)
    plt.yscale('log')
    ax = plt.gca()
    ax.set_ylim([min_y, max_y])
    plt.plot(x, y, color='r')
    # plt.plot(x,y_d)
    plt.savefig('function.jpeg')

def task9(data, x_array, y_array, threshold):
    # TODO: ...

def task10(list_of_smth, n):
    # TODO: ...

def task11(filename="infile.csv"):
    # TODO: ...

def task12(f="video-games.csv"):
    d = dict()
    n_games = f.shape[0]
    d["n_games"] = n_games
    by_years = f.groupby("year").count()
    d["by_years"] = by_years
    mean_price = f[f.publisher == "EA"].price.mean()
    d["mean_price"] = mean_price
    age_max_price = f.groupby("age_raiting").price.max()
    d["age_max_price"] = age_max_price
    mean_raiting_1_2 = f[(f.max_players == 1) | (f.max_players == 2)].review_raiting.mean()
    d["mean_raiting_1_2"] = mean_raiting_1_2
    min_max_price = f["age_raiting", "price"].groupby("age_raiting").price.max()
    #min_max_price["min"] = f["age_raiting", "price"].groupby("age_raiting").price.min().iloc[:, 2:2]
