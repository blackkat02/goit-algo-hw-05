import timeit

# Алгоритм Боєра-Мура
def build_shift_table(pattern):
    table = {}
    length = len(pattern)
    for index, char in enumerate(pattern[:-1]):
        table[char] = length - index - 1
    table.setdefault(pattern[-1], length)
    return table

def boyer_moore_search(text, pattern):
    shift_table = build_shift_table(pattern)
    i = 0
    while i <= len(text) - len(pattern):
        j = len(pattern) - 1
        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1
        if j < 0:
            return i
        i += shift_table.get(text[i + len(pattern) - 1], len(pattern))
    return -1

# Алгоритм Кнута-Морріса-Пратта
def compute_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp_search(text, pattern):
    M = len(pattern)
    N = len(text)
    lps = compute_lps(pattern)
    i = j = 0
    while i < N:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == M:
            return i - j
        elif i < N and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1

# Алгоритм Рабіна-Карпа
def polynomial_hash(s, base=256, modulus=101):
    n = len(s)
    hash_value = 0
    for i, char in enumerate(s):
        power_of_base = pow(base, n - i - 1) % modulus
        hash_value = (hash_value + ord(char) * power_of_base) % modulus
    return hash_value

def rabin_karp_search(main_string, substring):
    substring_length = len(substring)
    main_string_length = len(main_string)
    base = 256
    modulus = 101
    substring_hash = polynomial_hash(substring, base, modulus)
    current_slice_hash = polynomial_hash(main_string[:substring_length], base, modulus)
    h_multiplier = pow(base, substring_length - 1) % modulus
    for i in range(main_string_length - substring_length + 1):
        if substring_hash == current_slice_hash:
            if main_string[i:i + substring_length] == substring:
                return i
        if i < main_string_length - substring_length:
            current_slice_hash = (current_slice_hash - ord(main_string[i]) * h_multiplier) % modulus
            current_slice_hash = (current_slice_hash * base + ord(main_string[i + substring_length])) % modulus
            if current_slice_hash < 0:
                current_slice_hash += modulus
    return -1

# Функція вимірювання часу
def measure_time(search_func, text, pattern):
    return timeit.timeit(lambda: search_func(text, pattern), number=100)

# Завантаження статей
with open('article1.txt', 'r', encoding='utf-8') as f1:
    text1 = f1.read()

with open('article2.txt', 'r', encoding='utf-8') as f2:
    text2 = f2.read()
    #print(text2)

# Підрядки для пошуку
existing_substring_1 = "Автори публiкації"
non_existing_substring = "небезпечний алгоритм"
existing_substring_2 = "Автори публiкації"

# Вимірювання часу для Статті 1
print("Стаття 1:")
print("Існуючий підрядок")
print(f"Боєр-Мур: {measure_time(boyer_moore_search, text1, existing_substring_1)} {boyer_moore_search(text1, existing_substring_1)}")
print(f"Кнут-Морріс-Пратт: {measure_time(kmp_search, text1, existing_substring_1)} {kmp_search(text1, existing_substring_1)}")
print(f"Рабін-Карп: {measure_time(rabin_karp_search, text1, existing_substring_1)} {rabin_karp_search(text1, existing_substring_1)}")
print("\nВигаданий підрядок")
print(f"Боєр-Мур: {measure_time(boyer_moore_search, text1, non_existing_substring)} {boyer_moore_search(text1, non_existing_substring)}")
print(f"Кнут-Морріс-Пратт: {measure_time(kmp_search, text1, non_existing_substring)} {kmp_search(text1, non_existing_substring)}")
print(f"Рабін-Карп: {measure_time(rabin_karp_search, text1, non_existing_substring)} {rabin_karp_search(text1, non_existing_substring)}")

# Вимірювання часу для Статті 2
print("\nСтаття 2:")
print("Існуючий підрядок")
print(f"Боєр-Мур: {measure_time(boyer_moore_search, text2, existing_substring_2)} {boyer_moore_search(text2, existing_substring_2)}")
print(f"Кнут-Морріс-Пратт: {measure_time(kmp_search, text2, existing_substring_2)} {kmp_search(text2, existing_substring_2)}")
print(f"Рабін-Карп: {measure_time(rabin_karp_search, text2, existing_substring_2)} {rabin_karp_search(text2, existing_substring_2)}")
print("\nВигаданий підрядок")
print(f"Боєр-Мур: {measure_time(boyer_moore_search, text2, non_existing_substring)} {boyer_moore_search(text2, non_existing_substring)}")
print(f"Кнут-Морріс-Пратт: {measure_time(kmp_search, text2, non_existing_substring)} {kmp_search(text2, non_existing_substring)}")
print(f"Рабін-Карп: {measure_time(rabin_karp_search, text2, non_existing_substring)} {rabin_karp_search(text2, non_existing_substring)}")
