from typing import List
import random

def find_length(nums: List[int]) -> int:
    if not nums:
            return 0

    ret = 1
    i = 1
    while i < len(nums):
        cur = 1
        seq = [nums[i-1]]
        while i < len(nums) and (nums[i] > nums[i-1]):
            cur += 1
            i += 1
            seq.append(nums[i-1])
                 
        i += 1
        ret = max(ret, cur)

    return (ret, seq)

n = int(input('Введите число элементов: '))
n_list = [random.randrange(-100, 101, 1) for i in range(n)]
print( n_list)
print(find_length(n_list))