x = float(input("Введіть x: "))

# рахуємо верх і низ окремо
chyselnyk = (x - 1) * (x - 2)
znamennyk = x - 3

# костиль щоб не вибило помилку якщо ввести 3
if znamennyk == 0:
    print("На нуль ділити нє")
else:
    k = chyselnyk / znamennyk
    print("k =", k)




import math

x = float(input("Введіть x: "))

# рахуємо тангенс в квадраті
tan_kvadrat = math.tan(x) ** 2
# рахуємо косинус в квадраті
cos_kvadrat = math.cos(x) ** 2

# збираємо все до купи
v = tan_kvadrat + (1 / cos_kvadrat)

print("v =", v)






import math

x = float(input("Введіть x: "))

# рахуємо тангенс в квадраті
tan_kvadrat = math.tan(x) ** 2
# рахуємо косинус в квадраті
cos_kvadrat = math.cos(x) ** 2

# збираємо все до купи
v = tan_kvadrat + (1 / cos_kvadrat)

print("v =", v)









x = float(input("Введіть x: "))

if x < 0:
    y = x + 5
elif x >= 0 and x < 10:
    y = 2 * x
else:
    # це для варіанту коли x >= 10
    y = x - 10

print("y =", y)