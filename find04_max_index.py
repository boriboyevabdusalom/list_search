def find_max_index(data):
    """
    Given the list of numbers, return the index of maximum number in the list
    args:
        data: list of numbers
    returns: index of maximum number in the list
    """
    i = 0
    mx = data[0]
    while i < len(data):
        x = data[i]
        if x > mx:
            mx = x
        i += 1
    return data.index(mx)
print(find_max_index([1, 2, 3, 4, 5]))
print(find_max_index([6, 8, 7, 4, 0]))
