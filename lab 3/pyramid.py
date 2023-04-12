def heap_sort(nums):
    build_max_heap(nums)
    for i in range(len(nums) - 1, 0, -1):
        nums[0], nums[i] = nums[i], nums[0]
        max_heapify(nums, index=0, size=i)
 
def parent(i):
    return (i - 1)//2
 
def left(i):
    return 2*i + 1
 
def right(i):
    return 2*i + 2
 
def build_max_heap(nums):
    length = len(nums)
    start = parent(length - 1)
    while start >= 0:
        max_heapify(nums, index=start, size=length)
        start = start - 1
 
def max_heapify(nums, index, size):
    l = left(index)
    r = right(index)
    if (l < size and nums[l] > nums[index]):
        largest = l
    else:
        largest = index
    if (r < size and nums[r] > nums[largest]):
        largest = r
    if (largest != index):
        nums[largest], nums[index] = nums[index], nums[largest]
        max_heapify(nums, largest, size)
 
list_of_nums = [88, 42, 30, 30, 1, 9, 39, 75]
heap_sort(list_of_nums)
print(list_of_nums)