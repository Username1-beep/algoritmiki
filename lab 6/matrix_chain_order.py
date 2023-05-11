def matrix_chain_order(matrices):
    n = len(matrices)

    # Создаем таблицы для хранения результатов
    m = [[float('inf')] * n for _ in range(n)]
    s = [[0] * n for _ in range(n)]

    # Диагональные элементы (единичные матрицы) равны нулю
    for i in range(n):
        m[i][i] = 0

    # Заполняем таблицы по диагоналям
    for l in range(2, n + 1):  # Длина подцепочки матриц
        for i in range(n - l + 1):
            j = i + l - 1
            for k in range(i, j):
                # Вычисляем количество скалярных операций для данного разбиения
                cost = m[i][k] + m[k + 1][j] + matrices[i].shape[0] * matrices[k].shape[1] * matrices[j].shape[1]
                if cost < m[i][j]:
                    m[i][j] = cost
                    s[i][j] = k

    return m[0][n - 1], s


# Пример использования
import numpy as np

# Задаем последовательность матриц A, B, C, ..., Z
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
C = np.array([[9, 10], [11, 12]])
matrices = [A, B, C]

min_scalar_ops, optimal_parens = matrix_chain_order(matrices)

print("Минимальное количество скалярных операций:", min_scalar_ops)
print("Оптимальная расстановка скобок:", optimal_parens)
