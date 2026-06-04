print("Вводь 10 чисел:")

suma = 0
kilkist = 0

# цикл на 10 разів
for i in range(10):
    x = int(input("Давай число: "))
    # перевіряємо чи в діапазоні від 10 до 20
    if x >= 10 and x <= 20:
        suma = suma + x
        kilkist = kilkist + 1

# костиль шоб не поділити на нуль якщо таких чисел не ввели
if kilkist > 0:
    serednye = suma / kilkist
    print("Середнє арифметичне:", serednye)
else:
    print("Нема чисел в діапазоні від 10 до 20")


# перше 



print("Вводь числа по черзі (щоб зупинити, введи 0):")

# беремо перше число окремо, шоб було з чим порівнювати
pershe = int(input("число: "))
max_chyslo = pershe
min_chyslo = pershe

x = pershe

# крутимо цикл поки не введуть нуль
while x != 0:
    if x > max_chyslo:
        max_chyslo = x
    if x < min_chyslo:
        min_chyslo = x
        
    x = int(input("число: "))

# рахуємо різницю
riznytsya = max_chyslo - min_chyslo

print("Найбільше:", max_chyslo)
print("Найменше:", min_chyslo)
print("Різниця між ними:", riznytsya)