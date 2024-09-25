def normal_pyramid(rows):
    c = 0
    while rows > c:
        counter = c
        while rows > counter:
            print("#", end = "")
            counter += 1
        print("")
        c += 1

def recursive_pyramid(rows):
    if rows == 0:
        return 0
    
    i = 0
    while i < rows:
        print("#", end = "")
        i += 1
    print("")

    # Recursive property. If you want to reverse the pyramid, just put this at the start
    recursive_pyramid(rows - 1)


# My own experimentation with implementing the recursive pyramid
def recursive_pyramid_2(rows):
    if rows == 1:
        print("#", end = "")
    else:
        i = 0
        while i < rows:
            recursive_pyramid_2(rows - 1)
            # recursive_pyramid(1)
            rows -= 1
        print("")

recursive_pyramid(4)
recursive_pyramid_2(3)