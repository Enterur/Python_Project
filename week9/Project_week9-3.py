from tkinter import *
from time import *

fnameList = ["moon.gif", "dog_photo1.gif", "heart.gif", "ball.gif", "sun1.gif",
             "light.gif", "cat.gif", "book.gif", "pen.gif"]
photoList = [None] * 9
num = 0

def clickNext():
    global num
    num += 1
    if num > 8:
        num = 0
    photo = PhotoImage(file = "C:\\Users\\kimmi\\OneDrive\\바탕 화면\\Python_Project\\week9\\" + fnameList[num])
    pLabel.configure(image= photo)
    pLabel.image = photo
    nameLabel.configure(text = fnameList[num])


def clickPrev():
    global num
    num -= 1
    if num < 0:
        num = 8
    photo = PhotoImage(file = "C:\\Users\\kimmi\\OneDrive\\바탕 화면\\Python_Project\\week9\\" + fnameList[num])
    pLabel.configure(image= photo)
    pLabel.image = photo
    nameLabel.configure(text = fnameList[num])


window = Tk()
window.geometry("700x500")
window.title("사진 앨범 보기")

btnPrev = Button(window, text = "<< 이전", command = clickPrev)
btnNext = Button(window, text = "다음 >>", command = clickNext)
nameLabel = Label(window, text = fnameList[0]) #num 사용 시 전역변수 num = 0이므로 초기값만 보임
nameLabel.place(x = 325, y = 12.5)

photo = PhotoImage(file = "C:\\Users\\kimmi\\OneDrive\\바탕 화면\\Python_Project\\week9\\" + fnameList[0])
pLabel = Label(window, image = photo)

btnPrev.place(x = 250, y = 10)
btnNext.place(x = 400, y = 10)
pLabel.place(x = 15, y = 50)

window.mainloop()