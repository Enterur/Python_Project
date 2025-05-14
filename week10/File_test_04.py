inFp, outFp = None, None
inStr = ""
inSTR = input("소스 파일명을 입력하세요: ")
outSTR = input("타깃 파일명을 입력하세요: ")

inFp = open("C:\Windows\win.ini", "r")
outFp = open("C:\Windows\Temp\memo.txt", "w")

inList = inFp.readlines()

for inStr in inList:
    outFp.writelines(inStr)

inFp.close()
outFp.close()
print("--- %s파일이 %s파일로 복사되었음 ---"% (inSTR, outSTR))