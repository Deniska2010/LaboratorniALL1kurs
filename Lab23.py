import math
import random

# --- ЗАВДАННЯ 1: Магазин (Знижка 10% при сумі > 1000) ---
# Умова: Обчислити суму до сплати[cite: 32, 91].
def task_1():
    print("\n--- Завдання 1: Магазин ---")
    try:
        price = float(input("Введіть ціну товару: "))
        quantity = int(input("Введіть кількість: "))
        total = price * quantity
        if total > 1000:
            total *= 0.9  # знижка 10%
            print("Надано знижку 10%!")
        print(f"Загальна вартість: {round(total, 2)} грн")
    except ValueError:
        print("Помилка: введіть числа!")

# --- ЗАВДАННЯ 2: Прості числа ---
# Умова: Визначити, чи є натуральне число простим[cite: 45, 91].
def task_2():
    print("\n--- Завдання 2: Прості числа ---")
    try:
        n = int(input("Введіть натуральне число: "))
        if n < 2:
            print("Число не є простим")
        else:
            is_prime = True
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    is_prime = False
                    break
            if is_prime:
                print(f"{n} — просте число")
            else:
                print(f"{n} — складене число")
    except ValueError:
        print("Помилка: введіть ціле число!")

# --- ЗАВДАННЯ 3: Квадратне рівняння ---
# Умова: Розв'язати $ax^2 + bx + c = 0$[cite: 91].
def task_3():
    print("\n--- Завдання 3: Квадратне рівняння ---")
    try:
        a = float(input("Введіть a: "))
        b = float(input("Введіть b: "))
        c = float(input("Введіть c: "))
        if a == 0:
            print("Це не квадратне рівняння.")
            return
        d = b**2 - 4*a*c
        if d > 0:
            x1 = (-b + math.sqrt(d)) / (2*a)
            x2 = (-b - math.sqrt(d)) / (2*a)
            print(f"Два корені: x1 = {round(x1, 2)}, x2 = {round(x2, 2)}")
        elif d == 0:
            x = -b / (2*a)
            print(f"Один корінь: x = {round(x, 2)}")
        else:
            print("Коренів немає (D < 0)")
    except ValueError:
        print("Помилка введення!")

# --- ЗАВДАННЯ 4: Температура ---
# Умова: Перевести C в F або навпаки[cite: 91].
def task_4():
    print("\n--- Завдання 4: Температура ---")
    try:
        print("1: Цельсій -> Фаренгейт\n2: Фаренгейт -> Цельсій")
        choice = int(input("Ваш вибір: "))
        temp = float(input("Введіть значення: "))
        if choice == 1:
            res = (temp * 9/5) + 32
            print(f"{temp}°C = {round(res, 2)}°F")
        elif choice == 2:
            res = (temp - 32) * 5/9
            print(f"{temp}°F = {round(res, 2)}°C")
        else:
            print("Неправильний вибір.")
    except ValueError:
        print("Помилка введення!")

# --- ЗАВДАННЯ 5: Площа трикутника (Герон) ---
# Умова: Обчислити площу за трьома сторонами[cite: 91].
def task_5():
    print("\n--- Завдання 5: Площа трикутника ---")
    try:
        a = float(input("Сторона a: "))
        b = float(input("Сторона b: "))
        c = float(input("Сторона c: "))
        if a + b > c and a + c > b and b + c > a:
            p = (a + b + c) / 2
            area = math.sqrt(p * (p - a) * (p - b) * (p - c))
            print(f"Площа трикутника: {round(area, 2)}")
        else:
            print("Трикутник з такими сторонами не існує")
    except ValueError:
        print("Помилка: введіть числа!")

# --- ЗАВДАННЯ 6: Високосний рік ---
# Умова: Визначити, чи є рік високосним[cite: 91].
def task_6():
    print("\n--- Завдання 6: Високосний рік ---")
    try:
        year = int(input("Введіть рік: "))
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print(f"{year} — високосний рік")
        else:
            print(f"{year} — не високосний")
    except ValueError:
        print("Введіть коректний рік!")

# --- ЗАВДАННЯ 7: Сума цифр ---
# Умова: Знайти суму цифр цілого числа[cite: 91].
def task_7():
    print("\n--- Завдання 7: Сума цифр ---")
    try:
        num = abs(int(input("Введіть ціле число: ")))
        s = sum(int(digit) for digit in str(num))
        print(f"Сума цифр: {s}")
    except ValueError:
        print("Помилка: потрібно ціле число!")

# --- ЗАВДАННЯ 8: Паліндром ---
# Умова: Перевірити рядок на паліндром[cite: 91].
def task_8():
    print("\n--- Завдання 8: Паліндром ---")
    text = input("Введіть рядок: ")
    clean_text = "".join(text.lower().split()) # Видалення пробілів та регістру [cite: 91]
    if clean_text == clean_text[::-1]:
        print("Це паліндром")
    else:
        print("Це не паліндром")

# --- ЗАВДАННЯ 9: НСД (Алгоритм Евкліда) ---
# Умова: Знайти найбільший спільний дільник[cite: 91].
def task_9():
    print("\n--- Завдання 9: НСД ---")
    try:
        a = abs(int(input("Перше число: ")))
        b = abs(int(input("Друге число: ")))
        while b:
            a, b = b, a % b
        print(f"Найбільший спільний дільник (НСД): {a}")
    except ValueError:
        print("Помилка: введіть цілі числа!")

# --- ЗАВДАННЯ 10: Факторіал ---
# Умова: Обчислити факторіал циклом[cite: 91].
def task_10():
    print("\n--- Завдання 10: Факторіал ---")
    try:
        n = int(input("Введіть число n: "))
        if n < 0:
            print("Факторіал від'ємного числа не існує.")
        else:
            res = 1
            for i in range(1, n + 1):
                res *= i
            print(f"{n}! = {res}")
    except ValueError:
        print("Помилка: введіть ціле число!")

# --- ЗАПУСК УСІХ ЗАВДАНЬ ПО ЧЕРЗІ ---
if __name__ == "__main__":
    tasks = [task_1, task_2, task_3, task_4, task_5, task_6, task_7, task_8, task_9, task_10]
    for task in tasks:
        task()
        print("-" * 30)