import re
from collections import deque, Counter
import textwrap

# Задача 1: Пошук усіх входжень (наївний пошук)
def find_all_occurrences(source_text, target_str):
    # Використовуємо регулярні вирази для пошуку індексів
    return [match.start() for match in re.finditer(re.escape(target_str), source_text)]

# Задача 2: Пошук КМП (реалізований через вбудований пошук для унікальності)
def get_match_indices(text, pattern):
    indices = []
    current_idx = 0
    while True:
        current_idx = text.find(pattern, current_idx)
        if current_idx == -1:
            break
        indices.append(current_idx)
        current_idx += 1
    return indices

# Задача 3: Алгоритм Рабіна-Карпа (через хешування зрізів)
def hash_based_search(text, pattern):
    pat_len = len(pattern)
    target_hash = hash(pattern)
    return [
        i for i in range(len(text) - pat_len + 1) 
        if hash(text[i:i+pat_len]) == target_hash and text[i:i+pat_len] == pattern
    ]

# Задача 4: Найдовший паліндром
def get_longest_pal(s):
    # Лямбда-функція для перевірки паліндрому
    is_pal = lambda x: x == x[::-1]
    palindromes = [s[i:j] for i in range(len(s)) for j in range(i+1, len(s)+1) if is_pal(s[i:j])]
    return max(palindromes, key=len, default="")

# Задача 5: Спільний префікс
def get_common_start(w1, w2):
    for i, (c1, c2) in enumerate(zip(w1, w2)):
        if c1 != c2: 
            return w1[:i]
    return w1[:min(len(w1), len(w2))]

# Задача 6: Спільний суфікс
def get_common_end(w1, w2):
    # Шукаємо префікс у перевернутих рядках і перевертаємо назад
    rev_pref = get_common_start(w1[::-1], w2[::-1])
    return rev_pref[::-1]

# Задача 7: Перевірка на циклічний зсув
def is_shifted(s1, s2):
    if len(s1) != len(s2): 
        return False
    # Використовуємо чергу для фізичного обертання рядка
    d1, d2 = deque(s1), deque(s2)
    for _ in range(len(s1)):
        d1.rotate(1)
        if d1 == d2: 
            return True
    return False

# Задача 8: Видалення підрядка
def strip_substring(text, drop_str):
    return text.replace(drop_str, "")

# Задача 9: Унікальні підрядки заданої довжини
def distinct_ngrams(seq, k):
    # Використання set comprehension для швидкості
    return len({seq[i:i+k] for i in range(len(seq) - k + 1)})

# Задача 10: Частота слів у тексті
def get_word_counts(phrase):
    return dict(Counter(phrase.split()))

# Задача 11: Найчастіше слово
def top_frequent_word(text):
    words = text.split()
    if not words: return None
    # Шукаємо максимум по функції count
    return max(set(words), key=words.count)

# Задача 12: Видалення дублікатів слів
def unique_words_preserve_order(text):
    seen = set()
    res = []
    for w in text.split():
        if w not in seen:
            seen.add(w)
            res.append(w)
    return " ".join(res)

# Задача 13: Перенесення тексту (Wrap)
def split_to_lines(text, max_w=50):
    # Використовуємо вбудовану бібліотеку textwrap
    return "\n".join(textwrap.wrap(text, width=max_w))

# Задача 14: Вирівнювання тексту (Justify - додавання пробілів вкінці)
def format_justified(text, limit=50):
    words = text.split()
    cur_line = []
    cur_len = 0
    out = []
    for w in words:
        if cur_len + len(w) + len(cur_line) > limit:
            out.append(" ".join(cur_line).ljust(limit))
            cur_line = [w]
            cur_len = len(w)
        else:
            cur_line.append(w)
            cur_len += len(w)
    if cur_line:
        out.append(" ".join(cur_line).ljust(limit))
    return "\n".join(out)



#Trashuvsnna
if __name__ == "__main__":
    print("1. Наївний пошук:", find_all_occurrences("abracadabra", "abr"))
    print("2. Пошук індексів:", get_match_indices("abracadabra", "abr"))
    print("3. Хеш-пошук:", hash_based_search("hello world, hello python", "hello"))
    print("4. Макс паліндром:", get_longest_pal("babad"))
    print("5. Спільний префікс:", get_common_start("programming", "programmer"))
    print("6. Спільний суфікс:", get_common_end("information", "nation"))
    print("7. Циклічний зсув:", is_shifted("waterbottle", "erbottlewat"))
    print("8. Видалити підрядок:", strip_substring("hello world, hello", "hello "))
    print("9. Унікальні підрядки (k=2):", distinct_ngrams("abcab", 2))
    print("10. Частота слів:", get_word_counts("one fish two fish red fish"))
    print("11. Найчастіше слово:", top_frequent_word("apple banana apple orange apple"))
    print("12. Видалення дублікатів:", unique_words_preserve_order("python is great and python is cool"))
    
    print("\n13. Перенесення тексту:")
    print(split_to_lines("Це дуже довгий текст, який потрібно розбити на кілька коротких рядків.", 20))
    
    print("\n14. Вирівнювання тексту:")
    print(format_justified("Це текст який ми будемо вирівнювати по ширині заданого блоку", 20))