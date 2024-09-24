array = []

with open("sorting_data_2.txt", "r") as f:
    lines = f.read().splitlines()
    for lines in lines: 
        array.append(int(lines))

def bubble_sort(array):
    for i in array:
        x = 0
        y = 1
        while y != len(array):
            if array[y] < array[x]: # If array[y] is bigger, switch places 
                temp = array[x]
                array[x] = array[y]
                array[y] = temp
            x += 1
            y += 1

def selection_sorting(array):
    i = 0
    while i < len(array):
        ii = i + 1
        while ii < len(array):
            if array[ii] < array [i]:
                temp = array[i]
                array[i] = array[ii]
                array[ii] = temp
            ii += 1
        i += 1


def my_sorting_algorithm(array):
    i = 1
    while i < len(array):
        x = 0
        while x < i:
            if array[i] < array[x]:
                temp = array[x]
                array[x] = array[i]
                y = x + 1
                while y < i + 1: # Shifting algorithm
                    temp2 = array[y]
                    array[y] = temp
                    temp = temp2
                    y += 1
            x += 1
        i += 1


def merge_sort(array):
    if len(array) == 1:
        return array
    else:
        halfway = len(array) / 2

        # Arrays to append the left and right halves
        left_half = []
        right_half = []

        # In the case of the length of an array being odd, the left halve will always have an additional value
        for i, n in enumerate(array):
            if i < halfway:
                left_half.append(n)
            else:
                right_half.append(n)
        
        sorted_left_half = merge_sort(left_half)
        sorted_right_half = merge_sort(right_half)

        merged = []
        
        # Merging the two arrays in order
        while len(sorted_left_half) != 0 or len(sorted_right_half) != 0:
            # Exception if one array is empty
            if len(sorted_left_half) == 0:
                merged.append(sorted_right_half[0])
                sorted_right_half.pop(0)

            elif len(sorted_right_half) == 0:
                merged.append(sorted_left_half[0])
                sorted_left_half.pop(0)

            # Regular case where comparisons can be made
            else:
                if sorted_left_half[0] < sorted_right_half[0]:
                    merged.append(sorted_left_half[0])
                    sorted_left_half.pop(0)
                else:
                    merged.append(sorted_right_half[0])
                    sorted_right_half.pop(0)

        return merged
                    

# bubble_sorting(array)
# my_sorting_algorithm()
x = bubble_sort(array)

for i in x:
    print(i)