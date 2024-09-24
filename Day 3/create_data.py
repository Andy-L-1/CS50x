import numpy as np

i = 100000
f = open("test.txt", "w")

while i > 0:
    a = str(np.random.randint(1, 10000000))
    f.write(a)
    f.write("\n")

    
    i -= 1

f.close()