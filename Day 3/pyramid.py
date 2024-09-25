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
    recursive_pyramid(rows - 1)

    i = 0
    while i < rows:
        print("#", end = "")
        i += 1
    print("")

# recursive_pyramid(5)
normal_pyramid(6)