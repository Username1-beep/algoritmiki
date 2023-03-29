def bubble_sort(arr):
    n = len(arr)
    # Проходим по массиву n-1 раз
    for i in range(n - 1):
        # Для каждого прохода сравниваем два соседних элемента и, если они стоят в неправильном порядке, меняем их местами
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

arr = [12, 10, 95, 86, 34, 15, 43]

print(bubble_sort(arr))

# arr.sort()
# print("Sorted array:", arr)

