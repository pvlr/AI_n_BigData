import numpy as np
import math


# Возвращает случайную матрицу 3х3 с значениями от 1 до 20
def getRandomMatrix():
    return np.random.randint(1, 20, size = (3, 3))


# Возвращает определитель переданной матрицы
def getDet(matrix):
    return np.linalg.det(matrix)


# Возвращает округленные значения синуса от -П до П с переданным шагом
def getSinValues(step):
    return [round(math.sin(x), 2) for x in  np.arange(-math.pi, math.pi, step)]


# Переводит RGB в HSL. Принимает три параметра - (R, G, B)
def convertRGBtoHSL(R, G, B):
    # Делим все значения на 255, чтобы они укладывались в диапозон 0..1
    R /= 255
    G /= 255
    B /= 255

    # Определяем максимальный и минимальный цвета в сочетании
    Cmax = max(R, G, B)
    Cmin = min(R, G, B)
    # Вычисляем разницу между ними
    diff = Cmax - Cmin

    # Сразу получаем яркость
    L = (Cmax + Cmin) / 2

    # Если разницы нет, значит переданный цвет - оттенок серого. Для него
    # можем сразу задать оттенок и насыщенность равные 0
    if diff == 0:
        H = S = 0
    else:
        # Здесь происходит преобразование по формуле, больше я ничего не знаю
        if Cmax == R:
            H = (G - B) / diff + (6 if G < B else 0)
        elif Cmax == G:
            H = (B - R) / diff + 2
        else:
            H = (R - G) / diff + 4

        H /= 6
        H *= 360
        S = diff / (1 - abs(2 * L - 1)) if diff != 0 else 0

    # Возвращает округленные значения оттенка, насыщенности и яркости
    return {"Hue": round(H, 1), "Saturation": round(S, 1), "Lightness": round(L, 1)}



if __name__ == '__main__':
    # Получаем случайную матрицу
    random_matrix = getRandomMatrix()
    # Получаем определитель этой матрицы
    det = getDet(random_matrix)
    # Получаем список значений синусов с шагом 0.1
    sin_values = getSinValues(0.1)

    # Выводим в консоль всё что получили
    print(
        f'Определитель случайной матрицы: {det}\n\n'
        f'Значения синуса с шагом 0.1: {sin_values}\n'
    )

    # Принимаем от пользователя цвет RGB
    R = int(input("R: "))
    G = int(input("G: "))
    B = int(input("B: "))
    # Выводим в консоль конвертированный в HSL цвет
    print(f'HSL: {convertRGBtoHSL(R, G, B)}')
