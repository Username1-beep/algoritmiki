def generate_fibonacci(n):
    fib = [1, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

def find_most_common_substring(string, n):
    counts = {}
    for i in range(len(string)-n+1):
        sub = string[i:i+n]
        if sub.isdigit() and int(sub) > 9 and int(sub) < 100:
            if sub in counts:
                counts[sub] += 1
            else:
                counts[sub] = 1
    max_count = 0
    most_common = []
    for sub, count in counts.items():
        if count > max_count:
            max_count = count
            most_common = [sub]
        elif count == max_count:
            most_common.append(sub)
    return most_common, max_count

def boyer_moore_search(text, pattern):
    m = len(pattern)
    n = len(text)
    last_occurrence = dict()
    for k in range(m):
        last_occurrence[pattern[k]] = k
    i = m - 1
    while i < n:
        j = m - 1
        while text[i] == pattern[j]:
            if j == 0:
                return i
            i -= 1
            j -= 1
        if text[i] not in last_occurrence:
            i += m
        else:
            lo = last_occurrence[text[i]]
            i += max(m - lo - 1, 1)

def count_frequent_numbers(text):
    # создаем словарь для хранения частоты каждого числа
    freq_dict = {}
    # цикл по всем возможным двузначным числам
    for i in range(10, 100):
        # преобразуем число в строку и ищем его в строке text
        pattern = str(i)
        index = boyer_moore_search(text, pattern)
        # если число найдено, добавляем его в словарь
        if index != None:
            if pattern in freq_dict:
                freq_dict[pattern] += 1
            else:
                freq_dict[pattern] = 1
    # находим наиболее часто встречающееся число (или числа)
    max_freq = max(freq_dict.values())
    most_frequent = [num for num, freq in freq_dict.items() if freq == max_freq]
    return most_frequent, max_freq

array = []
fib = generate_fibonacci(500)
for i in range(500):
        array.append(str(fib[i]))

string = ''.join(array)
most_common, max_count = find_most_common_substring(string, 2)

print("Наиболее часто встречающиеся двузначные числа:", most_common)
print("Количество их вхождений:", max_count)
