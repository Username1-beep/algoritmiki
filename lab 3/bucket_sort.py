def bucket_sort(arr, bucket_size=5):
    if len(arr) == 0:
        return arr

    # Находим минимальное и максимальное значения в списке
    min_val, max_val = min(arr), max(arr)
    # Вычисляем количество блоков
    bucket_count = (max_val - min_val) // bucket_size + 1
    # Создаем пустые блоки
    buckets = [[] for _ in range(bucket_count)]

    # Распределяем элементы по блокам
    for num in arr:
        buckets[(num - min_val) // bucket_size].append(num)

    # Сортируем каждый блок и объединяем их
    sorted_arr = []
    for bucket in buckets:
        sorted_arr += sorted(bucket)

    return sorted_arr

if __name__ == '__main__':
    arr = [8, 2, 1, 4, 5, 9, 1, 5, 7, 3]
    sorted_arr = bucket_sort(arr, bucket_size=5)
    print(sorted_arr)