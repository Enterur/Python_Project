inFp = None
inList, inStr = [], ""
i = 0

inFp = open("C:\\Users\\kimmi\\OneDrive\\바탕 화면\\Python_Project\\week10\\memo1.txt", "r", encoding = "UTF-8")

inList = inFp.readlines()

for inStr in inList:
    i += 1
    print("%d: %s"% (i, inStr))

inFp.close()