print("--- Сортування вибором (по спаданню) ---")
arr = []

print("Вводь 10 дійсних чисел:")
for i in range(10):
    chislo = float(input(f"Число {i+1}: "))
    arr.append(chislo)

# Сортування вибором (шукаємо максимальний і кидаємо на початок)
for i in range(9): # 10 - 1
    max_idx = i
    for j in range(i + 1, 10):
        if arr[j] > arr[max_idx]:
            max_idx = j
            
    # міняємо місцями через тимчасову змінну (шоб викладач бачив шо ти шариш логіку)
    temp = arr[i]
    arr[i] = arr[max_idx]
    arr[max_idx] = temp

print("Відсортований список:", arr)

# Після сортування по спаданню: макс - це перший елемент, мін - останній
maksymum = arr[0]
minimum = arr[-1] # або arr[9]

riznytsia = maksymum - minimum
print("Різниця між max і min:", riznytsia)









print("\n--- Бінарний пошук ---")
arr2 = []

# По умові список має бути вже відсортований, тому просто вводимо по зростанню
print("Вводь 12 дійсних чисел (ВВОДЬ ВЖЕ ПО ЗРОСТАННЮ!):")
for i in range(12):
    chislo = float(input(f"Елемент {i+1}: "))
    arr2.append(chislo)

shukane = float(input("Яке число шукаємо? "))

livi = 0
pravi = 11
znajshov = False
kilkist_porivnyan = 0

while livi <= pravi:
    kilkist_porivnyan = kilkist_porivnyan + 1
    seredyna = (livi + pravi) // 2
    
    if arr2[seredyna] == shukane:
        znajshov = True
        break
    elif arr2[seredyna] < shukane:
        livi = seredyna + 1
    else:
        pravi = seredyna - 1

if znajshov:
    print("Число знайшли на позиції (індексі):", seredyna)
else:
    print("Такого числа в списку нема :(")

print("Кількість порівнянь:", kilkist_porivnyan)






print("--- Додаткова 1: Бульбашка ---")
arr = []
for i in range(8):
    chislo = int(input(f"Введіть число {i+1}: "))
    arr.append(chislo)

# Сортування бульбашкою (найбільші спливають в кінець)
for i in range(7):
    for j in range(7 - i):
        if arr[j] > arr[j+1]:
            # міняємо місцями
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp

print("Відсортований список:", arr)

# Сума перших трьох (найменших, бо по зростанню)
suma_tryoh = arr[0] + arr[1] + arr[2]
print("Сума перших трьох елементів:", suma_tryoh)


# ==========================================
# ЗАДАЧА 1: Бульбашка (сума перших трьох)
# ==========================================
print("--- Додаткова 1: Бульбашка ---")
arr1 = []
print("Введіть 8 цілих чисел:")
for i in range(8):
    arr1.append(int(input(f"Число {i+1}: ")))

for i in range(7):
    for j in range(7 - i):
        if arr1[j] > arr1[j+1]:
            temp = arr1[j]
            arr1[j] = arr1[j+1]
            arr1[j+1] = temp

print("Відсортований список:", arr1)
suma_tryoh = arr1[0] + arr1[1] + arr1[2]
print("Сума перших трьох елементів:", suma_tryoh)
print("\n")


# ==========================================
# ЗАДАЧА 2: Сортування вибором (по спаданню)
# ==========================================
print("--- Додаткова 2: Вибором ---")
arr2 = []
print("Введіть 6 дійсних чисел:")
for i in range(6):
    arr2.append(float(input(f"Число {i+1}: ")))

for i in range(5):
    max_idx = i
    for j in range(i + 1, 6):
        if arr2[j] > arr2[max_idx]:
            max_idx = j
            
    temp = arr2[i]
    arr2[i] = arr2[max_idx]
    arr2[max_idx] = temp

print("Відсортовано по спаданню:", arr2)

kilkist = 0
for x in arr2:
    if x > 10:
        kilkist = kilkist + 1

print("Кількість чисел, більших за 10:", kilkist)
print("\n")


# ==========================================
# ЗАДАЧА 3: Бульбашка і парні числа
# ==========================================
print("--- Додаткова 3: Бульбашка і парні ---")
arr3 = []
print("Введіть 10 цілих чисел:")
for i in range(10):
    arr3.append(int(input(f"Число {i+1}: ")))

for i in range(9):
    for j in range(9 - i):
        if arr3[j] > arr3[j+1]:
            temp = arr3[j]
            arr3[j] = arr3[j+1]
            arr3[j+1] = temp

print("Відсортований список:", arr3)
print("Парні числа з нього:")
for x in arr3:
    if x % 2 == 0:
        print(x)
print("\n")


# ==========================================
# ЗАДАЧА 4: Лінійний пошук мінімуму
# ==========================================
print("--- Додаткова 4: Пошук мінімуму ---")
arr4 = []
print("Введіть 7 цілих чисел:")
for i in range(7):
    arr4.append(int(input(f"Число {i+1}: ")))

min_chislo = arr4[0]
for i in range(1, 7):
    if arr4[i] < min_chislo:
        min_chislo = arr4[i]

print("Найменше число у списку:", min_chislo)
print("\n")


# ==========================================
# ЗАДАЧА 5: Лінійний пошук (сума додатних)
# ==========================================
print("--- Додаткова 5: Сума додатних ---")
arr5 = []
print("Введіть 10 дійсних чисел:")
for i in range(10):
    arr5.append(float(input(f"Число {i+1}: ")))

suma_dodatnih = 0
for x in arr5:
    if x > 0:
        suma_dodatnih = suma_dodatnih + x

print("Сума всіх додатних чисел:", suma_dodatnih)
print("\n")


# ==========================================
# ЗАДАЧА 6: Бінарний пошук
# ==========================================
print("--- Додаткова 6: Бінарний пошук ---")
arr6 = []
print("Введіть 8 чисел СУВОРО ПО ЗРОСТАННЮ:")
for i in range(8):
    arr6.append(int(input(f"Число {i+1}: ")))

shukane = int(input("Яке число будемо шукати? "))

livi = 0
pravi = 7
znajshov = False

while livi <= pravi:
    seredyna = (livi + pravi) // 2
    
    if arr6[seredyna] == shukane:
        znajshov = True
        break
    elif arr6[seredyna] < shukane:
        livi = seredyna + 1
    else:
        pravi = seredyna - 1

if znajshov:
    print("Є таке число! Знайшли.")
else:
    print("Такого числа немає в списку.")