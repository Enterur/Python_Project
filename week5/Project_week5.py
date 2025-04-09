i, k, multi_line= 0, 0, ""

for i in range (2, 10):
    multi_line = multi_line + ("# %d단 #" % i)

print(multi_line) # '# %d단 #' 출력 

for i in range (1, 10):
    multi_line = ""
    for k in range(2, 10):
        multi_line = multi_line + str("%2d X%2d=%2d" % (k, i, k * i))
    print(multi_line) #가로로 구구단 출력