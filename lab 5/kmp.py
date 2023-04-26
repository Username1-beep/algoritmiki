def generate_fibonacci_string(length):
    fibonacci = [1, 1]
    for i in range(2, length):
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
    return "".join(str(x) for x in fibonacci)

def kmp_search(pattern, text):
    m = len(pattern)
    n = len(text)
    if m == 0:
        return 0
    if n == 0:
        return -1
    lps = [0] * m
    compute_lps(pattern, m, lps)
    i = 0
    j = 0
    count = 0
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == m:
            count += 1
            j = lps[j-1]
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
    return count

def compute_lps(pattern, m, lps):
    len = 0
    lps[0] = 0
    i = 1
    while i < m:
        if pattern[i] == pattern[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            if len != 0:
                len = lps[len-1]
            else:
                lps[i] = 0
                i += 1

def find_most_common_two_digit_numbers():
    fibonacci_string = generate_fibonacci_string(500)
    two_digit_numbers = [str(i) for i in range(10, 100)]
    counts = {}
    for number in two_digit_numbers:
        counts[number] = kmp_search(number, fibonacci_string)
    return sorted(counts.items(), key=lambda x: x[1], reverse=True)[:1]


if __name__ == "__main__":
    result = find_most_common_two_digit_numbers()
    print("The top most common two-digit number in the Fibonacci sequence is:")
    for item in result:
        print(item[0] + ": " + str(item[1]))
