import math

def task_1():
    print("\n--- Завдання #1 ---")
    a = float(input("Сторона трикутника: "))
    h = float(input("Висота: "))
    print(f"Площа: {0.5 * a * h:.2f}")

def task_2():
    print("\n--- Завдання #2 ---")
    r = float(input("Радіус клумби: "))
    print(f"Периметр: {2 * math.pi * r:.2f}, Площа: {math.pi * r**2:.2f}")

def task_3():
    print("\n--- Завдання #3 ---")
    a = float(input("Катет: "))
    alpha = float(input("Гострий кут (у градусах), прилеглий до катета: "))
    alpha_rad = math.radians(alpha)
    b = a * math.tan(alpha_rad)
    c = a / math.cos(alpha_rad)
    print(f"Периметр: {a + b + c:.2f}, Площа: {0.5 * a * b:.2f}")

def task_4():
    print("\n--- Завдання #4 ---")
    d = float(input("Діаметр: "))
    r = d / 2
    print(f"Довжина кола: {math.pi * d:.2f}, Площа: {math.pi * r**2:.2f}")

def task_5():
    print("\n--- Завдання #5 ---")
    a = float(input("Основа 1 трапеції: "))
    b = float(input("Основа 2 трапеції: "))
    c = float(input("Бічна сторона: "))
    h = math.sqrt(c**2 - ((a - b) / 2)**2)
    print(f"Периметр: {a + b + 2*c:.2f}, Площа: {(a + b) / 2 * h:.2f}")

def task_6():
    print("\n--- Завдання #6 ---")
    a = float(input("Катет a: "))
    b = float(input("Катет b: "))
    print(f"Гіпотенуза: {math.hypot(a, b):.2f}")

def task_7():
    print("\n--- Завдання #7 ---")
    price1 = float(input("Ціна 1-го товару: "))
    price2 = float(input("Ціна 2-го товару: "))
    p = float(input("Відсоток зростання (p): "))
    print(f"Нова ціна 1: {price1 * (1 + p/100):.2f}, Нова ціна 2: {price2 * (1 + p/100):.2f}")

def task_8():
    print("\n--- Завдання #8 ---")
    s1 = float(input("Площа поля 1 (га) для 36 т/га: "))
    s2 = float(input("Площа поля 2 (га) для 40 т/га: "))
    s3 = float(input("Площа поля 3 (га) для 44 т/га: "))
    w1, w2, w3 = s1 * 36, s2 * 40, s3 * 44
    print(f"Зібрано з полів: 1 - {w1} т, 2 - {w2} т, 3 - {w3} т. Разом: {w1+w2+w3} т")

def task_9():
    print("\n--- Завдання #9 ---")
    day = 24 * 3600
    week = 7 * day
    year = 365 * day
    print(f"Секунд у добі: {day}, у тижні: {week}, у не високосному році: {year}")

def task_10():
    print("\n--- Завдання #10 ---")
    v = 299792 # км/с
    h = v * 3600
    print(f"Відстань за годину: {h} км, за добу: {h * 24} км")

def task_11():
    print("\n--- Завдання #11 ---")
    r = float(input("Радіус сфери: "))
    print(f"Площа поверхні: {4 * math.pi * r**2:.2f}, Об'єм: {(4/3) * math.pi * r**3:.2f}")

def task_12():
    print("\n--- Завдання #12 ---")
    a = float(input("Ребро куба: "))
    print(f"Об'єм: {a**3:.2f}, Площа бічної поверхні: {4 * a**2:.2f}")

def task_13():
    print("\n--- Завдання #13 ---")
    p1 = float(input("Продуктивність 1 труби (л/год): "))
    p2 = float(input("Продуктивність 2 труби (л/год): "))
    p3 = float(input("Продуктивність 3 труби (л/год): "))
    t = float(input("Час роботи (год): "))
    print(f"Набрано води: {(p1 + p2 + p3) * t:.2f} л")

def task_14():
    print("\n--- Завдання #14 ---")
    S = float(input("Площа круга: "))
    r = math.sqrt(S / math.pi)
    a = 2 * r # сторона квадрата
    print(f"Периметр квадрата: {4 * a:.2f}, Площа квадрата: {a**2:.2f}")

def task_15():
    print("\n--- Завдання #15 ---")
    g = 9.81
    print(f"Шлях після 1 сек: {g * 1**2 / 2:.2f} м")
    print(f"Шлях після 2 сек: {g * 2**2 / 2:.2f} м")

def task_16():
    print("\n--- Завдання #16 ---")
    c1, t1 = float(input("Вартість (коп/хв) 1: ")), float(input("Час (хв) 1: "))
    c2, t2 = float(input("Вартість (коп/хв) 2: ")), float(input("Час (хв) 2: "))
    c3, t3 = float(input("Вартість (коп/хв) 3: ")), float(input("Час (хв) 3: "))
    sum1, sum2, sum3 = c1*t1, c2*t2, c3*t3
    print(f"До оплати: 1 розмова - {sum1} коп, 2 - {sum2} коп, 3 - {sum3} коп.")
    print(f"Всього: {sum1 + sum2 + sum3} коп.")

def task_17():
    print("\n--- Завдання #17 ---")
    d = float(input("Діагональ квадрата: "))
    a = d / math.sqrt(2)
    print(f"Сторона: {a:.2f}, Площа: {d**2 / 2:.2f}")

def task_18():
    print("\n--- Завдання #18 ---")
    h = float(input("Висота конуса h: "))
    l = float(input("Твірна l: "))
    r = float(input("Радіус основи r: "))
    print(f"Площа бічної поверхні: {math.pi * r * l:.2f}, Об'єм: {math.pi * r**2 * h / 3:.2f}")

def task_19():
    print("\n--- Завдання #19 ---")
    v1, t1 = float(input("Швидкість 1: ")), float(input("Час 1: "))
    v2, t2 = float(input("Швидкість 2: ")), float(input("Час 2: "))
    v3, t3 = float(input("Швидкість 3: ")), float(input("Час 3: "))
    s1, s2, s3 = v1*t1, v2*t2, v3*t3
    print(f"Шляхи: S1={s1}, S2={s2}, S3={s3}. Весь шлях: {s1+s2+s3}")

def task_20_to_39():
    print("\n--- Завдання #20-39 (Про трикутник) ---")
    i = int(input("Введіть ваш номер варіанта за списком (від 1 до 39): "))
    
    Ax, Ay = 0, 0
    Bx, By = i, i - 1
    Cx, Cy = -i, i + 1
    
    a = math.dist((Bx, By), (Cx, Cy)) # BC
    b = math.dist((Ax, Ay), (Cx, Cy)) # AC
    c = math.dist((Ax, Ay), (Bx, By)) # AB
    
    p = (a + b + c) / 2
    S = math.sqrt(p * (p - a) * (p - b) * (p - c))
    
    print("\n--- РЕЗУЛЬТАТИ ВАШОГО ВАРІАНТА ---")
    print(f"Довжини сторін: a={a:.2f}, b={b:.2f}, c={c:.2f}")
    print(f"Площа трикутника: {S:.2f}")
    
    # Висоти
    print(f"Висота ha = {(2 * S) / a:.2f}")
    print(f"Висота hb = {(2 * S) / b:.2f}")
    print(f"Висота hc = {(2 * S) / c:.2f}")
    
    # Медіани
    print(f"Медіана ma = {0.5 * math.sqrt(2 * b**2 + 2 * c**2 - a**2):.2f}")
    print(f"Медіана mb = {0.5 * math.sqrt(2 * a**2 + 2 * c**2 - b**2):.2f}")
    print(f"Медіана mc = {0.5 * math.sqrt(2 * a**2 + 2 * b**2 - c**2):.2f}")
    
    # Бісектриси
    print(f"Бісектриса Wa = {(2 * math.sqrt(b * c * p * (p - a))) / (b + c):.2f}")
    print(f"Бісектриса Wb = {(2 * math.sqrt(a * c * p * (p - b))) / (a + c):.2f}")
    print(f"Бісектриса Wc = {(2 * math.sqrt(a * b * p * (p - c))) / (a + b):.2f}")
    
    # Радіуси
    print(f"Радіус вписаного кола r = {S / p:.2f}")
    print(f"Радіус описаного кола R = {(a * b * c) / (4 * S):.2f}")
    print("-----------------------------------")
    print("Просто випиши ті два значення, які вимагаються у твоєму варіанті (20-39)!")

def main():
    while True:
        print("\n" + "="*40)
        print("МЕНЮ ЗАВДАНЬ ЛАБОРАТОРНОЇ РОБОТИ №16")
        print("="*40)
        print("Введіть число від 1 до 19, щоб запустити відповідне завдання.")
        print("Введіть 20 (або будь-яке до 39), щоб відкрити універсальний блок для трикутника.")
        print("Введіть 0 для виходу.")
        
        choice = input("\nВаш вибір (#): ")
        
        if choice == '0':
            print("Виходимо... Успішного захисту!")
            break
            
        try:
            task_num = int(choice)
            if 1 <= task_num <= 19:
                # Виклик функції за її назвою (наприклад task_1, task_5)
                globals()[f"task_{task_num}"]()
            elif 20 <= task_num <= 39:
                task_20_to_39()
            else:
                print("Немає такого завдання. Введіть число від 1 до 39.")
        except ValueError:
            print("Будь ласка, введіть число!")
        except Exception as e:
            print(f"Сталася помилка: {e}")

if __name__ == "__main__":
    main()