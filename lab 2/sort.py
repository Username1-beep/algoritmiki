def find_max(array):
    max_element = array[0]
    for i in range(1, len(array)):
        if array[i] > max_element:
            max_element = array[i]
    return max_element
