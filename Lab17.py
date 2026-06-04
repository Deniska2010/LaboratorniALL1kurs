x_str = input("Введіть значення x: ")
x = float(x_str)

# звичайні іфи, як у методичці
if x <= -6:
    Y = 27 * x + 3
elif x > -6 and x < 3:
    Y = (x ** 3) - 1
else:
    Y = (x ** 2) + 1

print("Y =", Y)


# Це було перше завдання






import math

x = float(input("Координата x: "))
y = float(input("Координата y: "))

# похибка з умови
eps = 0.001

# рахуємо саму функцію f(x)
fx = 6 * (math.cos(x) ** 2) - 0.25 * (x ** 5) + 3.2 * (x ** 2) - 2.7

# модуль різниці
riznytsia = abs(fx - y)

if riznytsia < eps:
    print("Точка належить кривій")
else:
    print("Точка НЕ належить кривій")







# Це було друге завдання





import math

x = float(input("Координата x: "))
y = float(input("Координата y: "))

# похибка з умови
eps = 0.001

# рахуємо саму функцію f(x)
fx = 6 * (math.cos(x) ** 2) - 0.25 * (x ** 5) + 3.2 * (x ** 2) - 2.7

# модуль різниці
riznytsia = abs(fx - y)

if riznytsia < eps:
    print("Точка належить кривій")
else:
    print("Точка НЕ належить кривій")