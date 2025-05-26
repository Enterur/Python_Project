import threading

class AddNumber:
    def __init__(self, number):
        self.number = number

    def addNumber(self):
        total_sum = 0
        for i in range(1, self.number + 1):
            total_sum += i
        print(f"1 + 2 + 3 +....+  {self.number} = {total_sum}")

sum1 = AddNumber(1000)
sum2 = AddNumber(100000)
sum3 = AddNumber(10000000)

th1 = threading.Thread(target = sum1.addNumber)
th2 = threading.Thread(target = sum2.addNumber)
th3 = threading.Thread(target = sum3.addNumber)

th1.start()
th2.start()
th3.start()