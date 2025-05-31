import threading

class AddNumber: # 자연수 합 class
    def __init__(self, number):
        self.number = number

    def addNumber(self): # 자연수 합 메서드
        total_sum = 0
        for i in range(1, self.number + 1):
            total_sum += i
        print(f"1 + 2 + 3 +....+  {self.number} = {total_sum}")

# 서로 다른 범위의 인스턴스 생성
sum1 = AddNumber(1000)
sum2 = AddNumber(100000)
sum3 = AddNumber(10000000)

# .Thread를 통해 여러 개 thread 병렬 실행
th1 = threading.Thread(target = sum1.addNumber)
th2 = threading.Thread(target = sum2.addNumber)
th3 = threading.Thread(target = sum3.addNumber)

th1.start()
th2.start()
th3.start()