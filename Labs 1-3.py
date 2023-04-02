import math # lab2, lab3

# программу невозможно дописать так как синтаксис в приведённом задании
# не соответствует ни одному из стандартов PEP,
# а следовательно не является частью кода на языке Python
def lab1() -> bool:
    return not bool(int(input('Введите число:\n')) % 2)

def lab2() -> tuple:
    r = int(input('Введите число:\n'))
    S = round(math.pi * r**2, 4) # площадь окружности
    C = round(math.pi * 2 * r, 4) # длина окружности
    return (S, C)

def lab3(init_velocity = 80, angle = 60, time = 20) -> list:
    rad_angle = math.radians(angle) # угол в радианах
    list = [[0, 0, 0]]
    for t in range(1, time+1):
        x = round(init_velocity * math.cos(rad_angle) * t, 4)
        y = round(init_velocity * math.sin(rad_angle) * t - 0.5 * 9.80665 * t**2, 4) # за g взято значение 9.80665
        list.append([t, x, y])
    return list

while True:
    inpt = input("Выберите одну из лабораторных работ вводом её номера. Или отправьте 0 для выхода.\n")
    try:
        inpt = int(inpt)
    except:
        print("Значение должно быть числовым.\n")
        continue
    if inpt == 0:
        break
    elif inpt == 1:
        print("Ответ:", lab1())
    elif inpt == 2:
        print("Ответ:", lab2())
    elif inpt == 3:
        for i in lab3():
            print(i)
    else:
        print("Введено неверное значение. Попробуйте ещё раз.\n")