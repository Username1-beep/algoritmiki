def comb_sort(nums):
    gap = len(nums)
    swaps = True
    while gap > 1 or swaps:
        gap = max(1, int(gap / 1.247331))
        swaps = False
        for i in range(len(nums) - gap):
            j = i+gap
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                swaps = True

list_of_nums = [88, 42, 30, 30, 1, 9, 39, 75]
comb_sort(list_of_nums)
print(list_of_nums)

if __name__ == '__main__':
    import timeit
    print(timeit.timeit("comb_sort([88, 42, 30, 30, 1, 9, 39, 75])", setup="from __main__ import comb_sort"))