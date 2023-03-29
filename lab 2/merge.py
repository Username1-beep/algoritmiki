def m_sort(num_list, start, end):
    if end - start > 1:
        mid = (start + end)//2
        m_sort(num_list, start, mid)
        m_sort(num_list, mid, end)
        m_list(num_list, start, mid, end)
 
def m_list(num_list, start, mid, end):
    left = num_list[start:mid]
    right = num_list[mid:end]
    k = start
    i = 0
    j = 0
    while (start + i < mid and mid + j < end):
        if (left[i] <= right[j]):
            num_list[k] = left[i]
            i = i + 1
        else:
            num_list[k] = right[j]
            j = j + 1
        k = k + 1
    if start + i < mid:
        while k < end:
            num_list[k] = left[i]
            i = i + 1
            k = k + 1
    else:
        while k < end:
            num_list[k] = right[j]
            j = j + 1
            k = k + 1
 
 
num_list = input('Input the list of numbers: ').split()
num_list = [int(x) for x in num_list]
m_sort(num_list, 0, len(num_list))
print('Sorted list: ', end='')
print(num_list)
