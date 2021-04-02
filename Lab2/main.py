import random as rand
import math
variant = 113
m = 5
y_max = (30 - variant) * 10
y_min = (20 - variant) * 10
x1_min, x1_max, x2_min, x2_max = -15, 30, 5, 40
xn = [[-1, -1],
      [1, -1],
      [-1, 1]]
def sredniyY(list):
    avY = []
    for i in range(len(list)):
        s = 0
        for j in list[i]:
            s += j
        avY.append(s / len(list[i]))
    return avY
def dispersia(list):
    disp = []
    for i in range(len(list)):
        s = 0
        for j in list[i]:
            s += (j - sredniyY(list)[i]) * (j - sredniyY(list)[i])
        disp.append(s / len(list[i]))

    return disp

def fuv(u, v):
    if u >= v:
        return u / v
    else:
        return v / u
def discriminant(x11, x12, x13, x21, x22, x23, x31, x32, x33):
    return x11 * x22 * x33 + x12 * x23 * x31 + x32 * x21 * x13 - x13 * x22 * x31 - x32 * x23 * x11 - x12 * x21 * x33


y = [[rand.randint(y_min, y_max) for j in range(6)] for i in range(3)]
srY = sredniyY(y)


sigmaTeta = math.sqrt((2 * (2 * m - 2)) / (m * (m - 4)))

Fuv = []
teta = []
Ruv = []


Fuv.append(fuv(dispersia(y)[0], dispersia(y)[1]))
Fuv.append(fuv(dispersia(y)[2], dispersia(y)[0]))
Fuv.append(fuv(dispersia(y)[2], dispersia(y)[1]))

teta.append(((m - 2) / m) * Fuv[0])
teta.append(((m - 2) / m) * Fuv[1])
teta.append(((m - 2) / m) * Fuv[2])

Ruv.append(abs(teta[0] - 1) / sigmaTeta)
Ruv.append(abs(teta[1] - 1) / sigmaTeta)
Ruv.append(abs(teta[2] - 1) / sigmaTeta)


print('Нормована матриця планування експерименту:')
for i in range(3):
        print(xn[i])
print('Матриця планування для m =', m)
for i in range(3):
        print(y[i])
print('Середне значення У :',
      round(srY[0], 4), round(srY[1], 4), round(srY[2], 4))
print("Дисперсія : ", ["{0:.4f}".format(dispersia(y)[0]), "{0:.4f}".format(dispersia(y)[1]),
                        "{0:.4f}".format(dispersia(y)[2])])
print('Основне відхилення: ', "{0:.4f}".format(sigmaTeta))
print('Експериментальні значення критерію Романовського:')
# Перевіримо на однорідність дисперсію
Rkr = 1


if Ruv[0] > Rkr or Ruv[1] > Rkr or Ruv[2] > Rkr:
        print('Помилка, ця дисперсія неоднорідна,починаємо з початку')
        def sredniyY(list):
            avY = []
            for i in range(len(list)):
                s = 0
                for j in list[i]:
                    s += j
                avY.append(s / len(list[i]))
            return avY


        def dispersia(list):
            disp = []
            for i in range(len(list)):
                s = 0
                for j in list[i]:
                    s += (j - sredniyY(list)[i]) * (j - sredniyY(list)[i])
                disp.append(s / len(list[i]))

            return disp


        def fuv(u, v):
            if u >= v:
                return u / v
            else:
                return v / u


        def discriminant(x11, x12, x13, x21, x22, x23, x31, x32, x33):
            return x11 * x22 * x33 + x12 * x23 * x31 + x32 * x21 * x13 - x13 * x22 * x31 - x32 * x23 * x11 - x12 * x21 * x33


        y = [[rand.randint(y_min, y_max) for j in range(6)] for i in range(3)]
        srY = sredniyY(y)

        sigmaTeta = math.sqrt((2 * (2 * m - 2)) / (m * (m - 4)))

        Fuv = []
        teta = []
        Ruv = []

        Fuv.append(fuv(dispersia(y)[0], dispersia(y)[1]))
        Fuv.append(fuv(dispersia(y)[2], dispersia(y)[0]))
        Fuv.append(fuv(dispersia(y)[2], dispersia(y)[1]))

        teta.append(((m - 2) / m) * Fuv[0])
        teta.append(((m - 2) / m) * Fuv[1])
        teta.append(((m - 2) / m) * Fuv[2])

        Ruv.append(abs(teta[0] - 1) / sigmaTeta)
        Ruv.append(abs(teta[1] - 1) / sigmaTeta)
        Ruv.append(abs(teta[2] - 1) / sigmaTeta)

        print('Нормована матриця планування експерименту:')
        for i in range(3):
            print(xn[i])
        print('Матриця планування для m =', m)
        for i in range(3):
            print(y[i])
        print('Середне значення У :',
              round(srY[0], 4), round(srY[1], 4), round(srY[2], 4))
        print("Дисперсія : ", ["{0:.4f}".format(dispersia(y)[0]), "{0:.4f}".format(dispersia(y)[1]),
                               "{0:.4f}".format(dispersia(y)[2])])
        print('Основне відхилення: ', "{0:.4f}".format(sigmaTeta))
        print('Експериментальні значення критерію Романовського:')
        # Перевіримо на однорідність дисперсію
        Rkr = 2
        mx1 = (xn[0][0] + xn[1][0] + xn[2][0]) / 3
        mx2 = (xn[0][1] + xn[1][1] + xn[2][1]) / 3
        my = (srY[0] + srY[1] + srY[2]) / 3

        a1 = (xn[0][0] ** 2 + xn[1][0] ** 2 + xn[2][0] ** 2) / 3
        a2 = (xn[0][0] * xn[0][1] + xn[1][0] * xn[1][1] + xn[2][0] * xn[2][1]) / 3
        a3 = (xn[0][1] ** 2 + xn[1][1] ** 2 + xn[2][1] ** 2) / 3

        a11 = (xn[0][0] * srY[0] + xn[1][0] * srY[1] + xn[2][0] * srY[2]) / 3
        a22 = (xn[0][1] * srY[0] + xn[1][1] * srY[1] + xn[2][1] * srY[2]) / 3

        b0 = discriminant(my, mx1, mx2, a11, a1, a2, a22, a2, a3) / discriminant(1, mx1, mx2, mx1, a1, a2, mx2, a2, a3)
        b1 = discriminant(1, my, mx2, mx1, a11, a2, mx2, a22, a3) / discriminant(1, mx1, mx2, mx1, a1, a2, mx2, a2, a3)
        b2 = discriminant(1, mx1, my, mx1, a1, a11, mx2, a2, a22) / discriminant(1, mx1, mx2, mx1, a1, a2, mx2, a2, a3)

        y_pr1 = b0 + b1 * xn[0][0] + b2 * xn[0][1]
        y_pr2 = b0 + b1 * xn[1][0] + b2 * xn[1][1]
        y_pr3 = b0 + b1 * xn[2][0] + b2 * xn[2][1]

        dx1 = abs(x1_max - x1_min) / 2
        dx2 = abs(x2_max - x2_min) / 2
        x10 = (x1_max + x1_min) / 2
        x20 = (x2_max + x2_min) / 2

        koef0 = b0 - (b1 * x10 / dx1) - (b2 * x20 / dx2)
        koef1 = b1 / dx1
        koef2 = b2 / dx2

        yP1 = koef0 + koef1 * x1_min + koef2 * x2_min
        yP2 = koef0 + koef1 * x1_max + koef2 * x2_min
        yP3 = koef0 + koef1 * x1_min + koef2 * x2_max

        for i in range(3):
            print("{0:.4f}".format(Ruv[i]))
        print('Натуралізовані коефіцієнти: \na0 =', round(koef0, 4), 'a1 =', round(koef1, 4), 'a2 =', round(koef2, 4))
        print('У практичний ', round(y_pr1, 4), round(y_pr2, 4), round(y_pr3, 4), )
        print('У практичний норм.', round(yP1, 4), round(yP2, 4), round(yP3, 4))


else:
        mx1 = (xn[0][0] + xn[1][0] + xn[2][0]) / 3
        mx2 = (xn[0][1] + xn[1][1] + xn[2][1]) / 3
        my = (srY[0] + srY[1] + srY[2]) / 3

        a1 = (xn[0][0] ** 2 + xn[1][0] ** 2 + xn[2][0] ** 2) / 3
        a2 = (xn[0][0] * xn[0][1] + xn[1][0] * xn[1][1] + xn[2][0] * xn[2][1]) / 3
        a3 = (xn[0][1] ** 2 + xn[1][1] ** 2 + xn[2][1] ** 2) / 3

        a11 = (xn[0][0] * srY[0] + xn[1][0] * srY[1] + xn[2][0] * srY[2]) / 3
        a22 = (xn[0][1] * srY[0] + xn[1][1] * srY[1] + xn[2][1] * srY[2]) / 3

        b0 = discriminant(my, mx1, mx2, a11, a1, a2, a22, a2, a3) / discriminant(1, mx1, mx2, mx1, a1, a2, mx2, a2, a3)
        b1 = discriminant(1, my, mx2, mx1, a11, a2, mx2, a22, a3) / discriminant(1, mx1, mx2, mx1, a1, a2, mx2, a2, a3)
        b2 = discriminant(1, mx1, my, mx1, a1, a11, mx2, a2, a22) / discriminant(1, mx1, mx2, mx1, a1, a2, mx2, a2, a3)

        y_pr1 = b0 + b1 * xn[0][0] + b2 * xn[0][1]
        y_pr2 = b0 + b1 * xn[1][0] + b2 * xn[1][1]
        y_pr3 = b0 + b1 * xn[2][0] + b2 * xn[2][1]

        dx1 = abs(x1_max - x1_min) / 2
        dx2 = abs(x2_max - x2_min) / 2
        x10 = (x1_max + x1_min) / 2
        x20 = (x2_max + x2_min) / 2

        koef0 = b0 - (b1 * x10 / dx1) - (b2 * x20 / dx2)
        koef1 = b1 / dx1
        koef2 = b2 / dx2

        yP1 = koef0 + koef1 * x1_min + koef2 * x2_min
        yP2 = koef0 + koef1 * x1_max + koef2 * x2_min
        yP3 = koef0 + koef1 * x1_min + koef2 * x2_max

        for i in range(3):
            print("{0:.4f}".format(Ruv[i]))
        print('Натуралізовані коефіцієнти: \na0 =', round(koef0, 4), 'a1 =', round(koef1, 4), 'a2 =', round(koef2, 4))
        print('У практичний ', round(y_pr1, 4), round(y_pr2, 4), round(y_pr3, 4), )
        print('У практичний норм.', round(yP1, 4), round(yP2, 4), round(yP3, 4))





