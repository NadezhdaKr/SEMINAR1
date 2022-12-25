# Задача 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и выводит название этого дня недели.

g = int(input('Введите день: '))
if g == 1:
    print('Понедельник')
elif g == 2:
    print('Вторник')
elif g == 3:
    print('Среда')
elif g == 4:
    print('Четверг')
elif g == 5:
    print('Пятница')
elif g == 6:
    print('Суббота')
elif g == 7:
    print('Воскресенье')
else:
    print('Нет такого дня')


# Задача 2. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

def inputNumbers(x):
    xy = ['X', 'Y']
    a = []
    for i in range(x):
        is_OK = False
        while not is_OK:
            try:
                number = int(input(f'Введите координаты по {xy[i]}: '))
                a.append(number)
                is_OK = True
            except ValueError:
                print('Вводить надо целые числа')
    return a


def calculateLengthSegment(a, b):
    lengthSegment = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** (0.5)
    return lengthSegment


print('Введите координаты точки А:')
pointA = inputNumbers(2)
print('Введите координаты точки В:')
pointB = inputNumbers(2)

print(f"Длина отрезка: {format(calculateLengthSegment(pointA, pointB), '.2f')}")


