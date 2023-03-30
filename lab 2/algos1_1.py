def binary_search(arr, target):
    """
    Функция бинарного поиска, принимает на вход упорядоченный массив arr и число target,
    которое нужно найти в массиве. Возвращает количество шагов, которое потребуется,
    чтобы найти число target в массиве.
    """
    steps = 0  # инициализация счетчика шагов
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2  # находим средний элемент
        steps += 1  # увеличиваем счетчик шагов
        if arr[mid] == target:
            return steps  # возвращаем количество шагов
        elif arr[mid] < target:
            left = mid + 1  # идем в правую половину
        else:
            right = mid - 1  # идем в левую половину
    return -1  # если элемент не найден, возвращаем -1
# Пример использования
arr = [1, 3, 5, 7, 9]
target = 5
steps = binary_search(arr, target)
print("Number of steps to find a number {}: {}".format(target, steps))