x, result, calc, num1, num2 = 0, 0, "", 0, 0
x = int(input("1. 입력한 수식 계산 2. 두 수 사이의 합계:"))

if x == 1:
    calc = input("수식을 입력하세요:")
    result = eval(calc)
    print("%s 결과는 %5.1f입니다" %(calc, result))
elif x == 2:
    num1 = int(input("첫 번째 숫자를 입력하세요: "))
    num2 = int(input("두 번째 숫자를 입력하세요: "))
    for i in range(num1, num2 + 1):
        result = result + i
    print("%d + ... + %d는 %d입니다." %(num1, num2, result))
else:
    print("잘못된 입력입니다.")