age = int(input("Введите возраст: "))
if age <= 1 and age >= 0:
    print("Младенец")
elif age > 1 and age < 13:
    print("Ребенок")
elif age >= 13 and age < 20:
    print("Подросток")
elif age >= 20:
    print("Взрослый")
else:
    print("Вы ввели отрицательное число")