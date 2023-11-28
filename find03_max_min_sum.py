def find_max_min_sum(data):
    """
    Given the list of numbers, return the sum of the maximum and minimum numbers in the list
    args:
        data: list of numbers
    returns: sum of the maximum and minimum numbers in the list
    """
    i = 0
    mx = data[0]
    min = data[0]
    while i < len(data):
        x = data[i]
        y = data[i]
        if x > mx:
            mx = x
        if y < min:
            min = y 
        i+=1

    return mx + min
print(find_max_min_sum([1, 2, 3, 4, 5]))
print(find_max_min_sum([2, 7, 3, 4, 9]))
