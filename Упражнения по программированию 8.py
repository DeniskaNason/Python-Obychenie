a = int(input("Введите количество людей, которые придут на пикник: "))
b = int(input("Введите количество хот-догов, которое будет предложено каждому участнику пикника: "))
c = a * b
if c % 10 != 0:
    min_package_sausages = c // 10 + 1
    exstra_sasuges =  min_package_sausages * 10 - c
else:
      min_package_sausages = c // 10
      exstra_sasuges = 0
if c % 8 != 0:
      min_package_buns = c // 8 + 1
      exstra_buns = min_package_buns * 8 - c
else:
       min_package_buns = c // 8
       exstra_buns = 0
print("Минимальное количество упаковок с сосисками:", min_package_sausages)
print("Количество оставшихся сосисок:", exstra_sasuges)
print("Минимальное количество упаковок с булочками:", min_package_buns )
print("Количество оставшихся булочек:", exstra_buns)