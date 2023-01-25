import numpy as np
from numpy import exp, sqrt
from tkinter import *
from itertools import permutations
import math

# Пока самая ррабочая пррогррамма

# находит самый короткий путь при заданной вершине
global apex, way, routes, X, Y, n, matrix, count, maindict, otsechenie, maindict2
way = []
a = 0
X = [32, 64, 7, 79, 7, 34, 12, 65, 25, 2]
Y = [65, 89, 95, 29, 41, 8, 37, 17, 56, 1]
n = len(X)
maindict = {}


# метод ближайшей вершины
def nearest_homie():
    global apex, way, routes, X, Y, n, maindict
    print('------------------------------------')
    s = []
    minS = []
    for ib in np.arange(0, n, 1):
        M = np.zeros([n, n])
        for i in np.arange(0, n, 1):
            for j in np.arange(0, n, 1):
                if i != j:
                    M[i, j] = (sqrt((X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2)).round(2)
                else:
                    M[i, j] = float('inf')
        way = []
        print(M)
        way.append(ib)
        for i in np.arange(1, n, 1):
            s = []
            for j in np.arange(0, n, 1):
                s.append(M[way[i - 1], j])
            way.append(s.index(min(s)))
            for j in np.arange(0, i, 1):
                M[way[i], way[j]] = float('inf')
                M[way[i], way[j]] = float('inf')
        S = sum([sqrt((X[way[i]] - X[way[i + 1]]) ** 2 + (Y[way[i]] - Y[way[i + 1]]) ** 2) for i in
                 np.arange(0, n - 1, 1)]) + sqrt((X[way[n - 1]] - X[way[0]]) ** 2 + (Y[way[n - 1]] - Y[way[0]]) ** 2)

        minS.append(S.round(2))
        maindict[str(way)] = S.round(2)

    for key, value in maindict.items():
        print("{0}: {1}".format(key, value))
    print('Кратчайший путь:', min(maindict, key=maindict.get), min(minS))


def brutal_force():
    def main():
        X = [32, 64, 7, 79, 7, 34, 12, 65, 25, 2]
        Y = [65, 89, 95, 29, 41, 8, 37, 17, 56, 1]
        cities = np.array([list(a) for a in zip(X, Y)])
        # подсчёт пути
        path, length = algorithm(cities)
        print('------------------------------------')
        print(path)

        print("Кратчайший путь", (round(length, 2)))

    def algorithm(cities):
        min_length = calc_length(cities, range(len(cities)))
        min_path = range(len(cities))

        for path in permutations(range(len(cities))):
            length = calc_length(cities, path)
            if length < min_length:
                min_length = length
                min_path = path

        return min_path, min_length

    def dist_squared(c1, c2):
        t1 = c2[0] - c1[0]
        t2 = c2[1] - c1[1]

        return math.sqrt(t1 ** 2 + t2 ** 2)

    def calc_length(cities, path):
        length = 0
        for i in range(len(path)):
            length += dist_squared(cities[path[i - 1]], cities[path[i]])

        return length

    if __name__ == "__main__":
        main()


def brunch_m():
    def main():
        X = [32, 64, 7, 79, 7, 34, 12, 65, 25, 2]
        Y = [65, 89, 95, 29, 41, 8, 37, 17, 56, 1]
        cities = np.array([list(a) for a in zip(X, Y)])
        # подсчёт пути

        path, length = algorithm(cities)
        print('------------------------------------')
        print(path)

        print("Кратчайший путь", (round(length, 2)))

    def algorithm(cities):
        new_lst = []
        count = 0
        min_length = calc_length(cities, range(len(cities)))
        min_path = range(len(cities))
        for path in permutations(range(len(cities))):
            length = calc_length(cities, path)
            if length < min_length:
                min_length = length
                min_path = path

            print('Путь: ', path, 'Длинна: ', round(length, 2))
            count += 1
            if count == 20:
                break
        return min_path, min_length

    def dist_squared(c1, c2):
        t1 = c2[0] - c1[0]
        t2 = c2[1] - c1[1]

        return math.sqrt(t1 ** 2 + t2 ** 2)

    def calc_length(cities, path):
        length = 0
        # length2 = 0
        length_lst = []
        for i in range(len(path)):
            length += dist_squared(cities[path[i - 1]], cities[path[i]])
            # length2 = dist_squared(cities[path[i - 1]], cities[path[i]])
            # добавляем путь в список
            length_lst.append(round(length, 2))
        # print('------------------------------------')
        # print('Длинна между городами:', length_lst)
        return length

    if __name__ == "__main__":
        main()


root = Tk()
root.title("Лаба 5")
# root.geometry("100x100")
Button(text='Метод ближайшего соседа', command=nearest_homie).grid(row=0, column=1)
Button(text='Метод ветвей и границ', command=brunch_m).grid(row=2, column=1)
Button(text='Метод полного перебора', command=brutal_force).grid(row=1, column=1)
root.mainloop()
