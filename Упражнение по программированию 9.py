a = int(input('Введите число строго от 0 до 36: '))
b = a % 2
if a == 0:
    print("Зеленый")
elif (a >= 1 and a <= 10) and b != 0:
    print('Красный')
elif (a >= 1 and a <= 10) and b != 1:
    print('Черный')
elif (a >= 11 and a <= 18) and b != 0:
    print('Черный')
elif (a >= 11 and a <= 18) and b != 1:
    print('Красный')
elif (a >= 19 and a <= 28) and b != 0:
    print('Красный')
elif (a >= 19 and a <= 28) and b != 1:
    print('Черный')
elif (a >= 29 and a <= 36) and b != 0:
    print('Черный')
elif (a >= 29 and a <= 36) and b != 1:
    print('Красный')
else:
    print("Ошибка")