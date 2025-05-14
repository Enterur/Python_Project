inFp = None
inStr = ""
i = 1

inFp = open("C:\\Users\\kimmi\\OneDrive\\바탕 화면\\Python_Project\\week10\\memo1.txt", "r", encoding = "UTF-8")

while True:
    inStr = inFp.readline()
    if inStr == "":
        break
    print("%d: %s"% (i, inStr))
    i += 1

inFp.close()