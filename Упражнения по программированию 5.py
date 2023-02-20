a = float(input("Введите массу тела в кг: "))
weight = a * 9.8
if weight >= 500:
    print("Тело слишком тяжелое")
elif weight <= 100:
    print("Тело слишком легкое")
else:
    print(f'{weight:.2f}')