def searchMax(array):
    max = array[0]
    for index in range(len(array)):
        if array[index] > max:
            max = array[index]
    return max

def searchMin(array):
    min = array[0]
    for index in range(len(array)):
        if array[index] < min:
            min = array[index]
    return min
