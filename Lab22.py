import random

print("--- ЛАБОРАТОРНА №22: ВАРІАНТИ 1-20 ---")

# Варіант 1: Сума додатних (10 цілих) 
a1 = [random.randint(-10, 10) for _ in range(10)]
s1 = 0
for x in a1:
    if x > 0: s1 += x
print(f"1. Список: {a1}\n   Сума додатних: {s1}")

# Варіант 2: Добуток від'ємних (12 дійсних) 
a2 = [round(random.uniform(-5, 5), 1) for _ in range(12)]
p2 = 1
exists2 = False
for x in a2:
    if x < 0:
        p2 *= x
        exists2 = True
print(f"2. Список: {a2}\n   Добуток від'ємних: {p2 if exists2 else 0}")

# Варіант 3: Кількість парних (15 цілих) 
a3 = [random.randint(1, 100) for _ in range(15)]
c3 = 0
for x in a3:
    if x % 2 == 0: c3 += 1
print(f"3. Список: {a3}\n   Кількість парних: {c3}")

# Варіант 4: Індекс максимального (8 цілих) 
a4 = [random.randint(1, 50) for _ in range(8)]
m4 = a4[0]
idx4 = 0
for i in range(len(a4)):
    if a4[i] > m4:
        m4 = a4[i]
        idx4 = i
print(f"4. Список: {a4}\n   Індекс макс: {idx4}")

# Варіант 5: Середнє арифметичне тих, що > 5 (10 дійсних) 
a5 = [round(random.uniform(1, 10), 1) for _ in range(10)]
sub5 = [x for x in a5 if x > 5]
avg5 = sum(sub5)/len(sub5) if sub5 else 0
print(f"5. Список: {a5}\n   Середнє (>5): {avg5}")

# Варіант 6: Скільки разів зустрічається число (20 цілих) 
a6 = [random.randint(1, 5) for _ in range(20)]
key6 = 3 # шукаємо трійку
count6 = 0
for x in a6:
    if x == key6: count6 += 1
print(f"6. Список: {a6}\n   Число {key6} зустрілось: {count6} разів")

# Варіант 7: Паліндром чи ні (16 цілих) 
a7 = [1, 2, 3, 4, 5, 6, 7, 8, 8, 7, 6, 5, 4, 3, 2, 1] # зробимо ручками для тесту
is_pal = True
for i in range(len(a7)//2):
    if a7[i] != a7[len(a7)-1-i]:
        is_pal = False
        break
print(f"7. Список: {a7}\n   Паліндром: {is_pal}")

# Варіант 8: Різниця між max та min (14 дійсних) 
a8 = [round(random.uniform(0, 100), 1) for _ in range(14)]
diff8 = max(a8) - min(a8)
print(f"8. Різниця max-min: {diff8}")

# Варіант 9: Замінити від'ємні на модулі (18 цілих) 
a9 = [random.randint(-20, 20) for _ in range(18)]
print(f"9. Було: {a9}")
for i in range(len(a9)):
    if a9[i] < 0: a9[i] = abs(a9[i])
print(f"   Стало: {a9}")

# Варіант 10: Видалити нулі (11 цілих) 
a10 = [0, 5, 0, 3, 0, 1, 8, 0, 9, 0, 4]
res10 = []
for x in a10:
    if x != 0: res10.append(x)
print(f"10. Без нулів: {res10}")

# Варіант 11: Сума з непарними індексами (13 дійсних) 
a11 = [round(random.uniform(1, 10), 1) for _ in range(13)]
s11 = 0
for i in range(1, len(a11), 2):
    s11 += a11[i]
print(f"11. Сума елементів на інд. 1, 3, 5...: {s11}")

# Варіант 12: Друге за величиною число (9 цілих) 
a12 = list(set([random.randint(1, 50) for _ in range(9)]))
a12.sort()
print(f"12. Список: {a12}\n    Друге за величиною: {a12[-2]}")

# Варіант 13: Циклічний зсув вправо на 2 (17 цілих) 
a13 = list(range(1, 18))
for _ in range(2):
    last = a13.pop()
    a13.insert(0, last)
print(f"13. Зсув вправо на 2: {a13}")

# Варіант 14: Сортування за спаданням вибором (15 дійсних) 
a14 = [round(random.uniform(1, 50), 1) for _ in range(15)]
for i in range(len(a14)):
    max_idx = i
    for j in range(i+1, len(a14)):
        if a14[j] > a14[max_idx]: max_idx = j
    a14[i], a14[max_idx] = a14[max_idx], a14[i]
print(f"14. Відсортовано: {a14}")

# Варіант 15: Прості числа (10 цілих) 
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True
a15 = [random.randint(1, 50) for _ in range(10)]
primes = [x for x in a15 if is_prime(x)]
print(f"15. Список: {a15}\n    Прості: {primes}")

# Варіант 16: Квадрати елементів (12 цілих) 
a16 = [random.randint(1, 10) for _ in range(12)]
sq16 = [x**2 for x in a16]
print(f"16. Квадрати: {sq16}")

# Варіант 17: Чи є зростаючою (20 цілих) 
a17 = sorted([random.randint(1, 100) for _ in range(20)])
is_inc = True
for i in range(len(a17)-1):
    if a17[i] >= a17[i+1]:
        is_inc = False
        break
print(f"17. Список: {a17}\n    Зростаюча: {is_inc}")

# Варіант 18: Видалити елемент за індексом (8 дійсних) 
a18 = [round(random.uniform(1, 10), 1) for _ in range(8)]
target_idx = 3
print(f"18. Було: {a18}")
del a18[target_idx]
print(f"    Після видалення інд.{target_idx}: {a18}")

# Варіант 19: Вставити 100 після кожного парного (14 цілих) 
a19 = [random.randint(1, 10) for _ in range(14)]
res19 = []
for x in a19:
    res19.append(x)
    if x % 2 == 0: res19.append(100)
print(f"19. Зі вставками 100: {res19}")

# Варіант 20: Медіана (16 дійсних) 
a20 = sorted([round(random.uniform(1, 100), 1) for _ in range(16)])
mid = len(a20) // 2
med = (a20[mid] + a20[mid-1]) / 2
print(f"20. Відсортовано: {a20}\n    Медіана: {med}")