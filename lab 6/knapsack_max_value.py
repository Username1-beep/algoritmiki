def knapsack_max_value(weights, values, total_weight, max_trips):
    n = len(weights)

    # Создаем таблицу для хранения результатов
    dp = [[0] * (total_weight + 1) for _ in range(max_trips + 1)]

    # Заполняем таблицу построчно
    for i in range(1, n + 1):
        for j in range(1, total_weight + 1):
            for k in range(min(j // weights[i - 1], max_trips) + 1):
                # Вычисляем максимальную сумму украденной ценности
                dp[k][j] = max(dp[k][j], dp[k - 1][j - k * weights[i - 1]] + k * values[i - 1])

    # Определяем, какие экспонаты были украдены
    stolen_items = []
    w = total_weight
    t = max_trips
    for i in range(n, 0, -1):
        while t > 0 and w >= weights[i - 1] and dp[t][w] == dp[t - 1][w - weights[i - 1]] + values[i - 1]:
            stolen_items.append(i)
            w -= weights[i - 1]
            t -= 1

    return dp[max_trips][total_weight], stolen_items[::-1]


# Пример использования
weights = [2, 3, 4, 5]  # Веса экспонатов
values = [3, 4, 8, 9]  # Ценности экспонатов
total_weight = 6  # Общая вместимость рюкзака в килограммах
max_trips = 2  # Количество заходов вора

max_total_value, stolen_items = knapsack_max_value(weights, values, total_weight, max_trips)

print("Максимальная сумма украденной ценности:", max_total_value)
print("Экспонаты, которые должен унести вор:", stolen_items)
