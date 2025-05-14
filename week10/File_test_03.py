outFp = None
inStr, outStr = "", ""

outFp = open("C:\\Users\\kimmi\\OneDrive\\바탕 화면\\Python_Git\\10-week_Practice\\FileTest\\data2.txt", "w")

while True:
    outStr = input("내용 입력: ")
    inStr = input("파일명을 입력하세요: ")
    if outStr != "":
        outFp.writelines(outStr + "\n")
    else:
        break

outFp.close()
print("---정상적으로 파일에 씀---")