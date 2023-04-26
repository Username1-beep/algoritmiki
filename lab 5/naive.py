

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

array = []

fib = generate_fibonacci(500)
for i in range(500):
        array.append(str(fib[i]))
        
string = ''.join(array)
most_common, max_count = find_most_common_substring(string, 2)

print("Наиболее часто встречающиеся двузначные числа:", most_common)
print("Количество их вхождений:", max_count)
