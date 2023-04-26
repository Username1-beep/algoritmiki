def partition(nums, low, high):

    point = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < point:
            i += 1

        j -= 1
        while nums[j] > point:
            j -= 1

        if i >= j:
            return j

        nums[i], nums[j] = nums[j], nums[i]

def quick_sort(nums):
    def _quick_sort(items, low, high):
        if low < high:
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)


list_of_nums = [88, 42, 30, 30, 1, 9, 39, 75]
quick_sort(list_of_nums)
print(list_of_nums)

if __name__ == '__main__':
    import timeit
    print(timeit.timeit("quick_sort([88, 42, 30, 30, 1, 9, 39, 75])", setup="from __main__ import quick_sort"))