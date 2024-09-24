import sorting_algoritims

array = []

with open("Sorting_data.txt", "r") as f:
    lines = f.read().splitlines()
    for lines in lines: 
        array.append(int(lines))

def linear_search(x):
    i = 0
    while i < len(array):
        if array[i] == x:
            return i
        i += 1
        

def binary_search(x):
    sorting_algoritims.bubble_sort(array)
    max = len(array)    
    min = 0
    result = -1
    while min < max:
        middle = round((min + max) / 2)
        if array[middle] == x:
            result = middle
            min = max
        elif array[middle] > x:
            max = middle -1
        else:
            min = middle + 1
    return result


print(linear_search(726338682)) # Return 9930
print(binary_search(898946953)) # Return 39
# 9008
# for i in array:
#     print(i)
