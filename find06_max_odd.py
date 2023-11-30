def find_max_odd(data):
    """
    Given the list of numbers, Find the maximum odd number in the list
    args:
        data: list of numbers
    returns: maximum odd number in the list
    """
    i=0
    mx=data[0]
    while i<len(data):
        x=data[i]
        if x > mx:
            mx=x
        i+=1
    return mx



print(find_max_odd([1, 8, 3, 8, 5]))
print(find_max_odd([11, 7, 5, 4, 9]))