a = input('Будет ли на ужине вегетарианец? ')
b = input('Будет ли на ужине веганец? ')
c = input('Будет ли на ужине приверженец безглютеновой диеты? ')
q1 = 'Изысканные гамбургеры от Джо'
q2 = 'Центральная пиццерия'
q3 = 'Кафе за углом'
q4 = 'Блюда от итальянской мамы'
q5 = 'Кухня шеф-повара'
if a == "да" and b == 'да' and c == 'да':
    print(q3, q5, sep ="           ")
elif a == "нет" and b == 'нет' and c == 'нет':
    print(q1, q2, q3, q4, q5, sep ="           ")
elif a == "да" and b == 'да' and c == 'нет':
    print(q3, q5, sep ="           ")
elif a == "да" and b == 'нет' and c == 'нет':
    print(q2, q3, q4, q5, sep ="           ")
elif a == "да" and b == 'нет' and c == 'да':
    print(q2, q3, q5, sep ="           ")
elif a == "нет" and b == 'да' and c == 'да':
    print(q3, q5, sep ="           ")
elif a == "нет" and b == 'нет' and c == 'да':
    print(q2, q3, q5, sep ="           ")
elif a == "нет" and b == 'да' and c == 'нет':
    print(q3, q4, q5, sep ="           ")