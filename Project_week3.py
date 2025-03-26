digit = int(input("입력 진수 결정(16/10/8/2):"))
num = input("값 입력:")

if digit == 16:
  n = int(num, 16) #진수를 정수로 변환
elif digit == 10:
  n = int(num)
elif digit == 8:
  n = int(num, 8)
elif digit == 2:
  n = int(num, 2)
else:
  print("잘못된 진수입니다.")

print("16진수 ==>", hex(n))
print("10진수 ==>", n)
print("8진수  ==>", oct(n))
print("2진수  ==>", bin(n))