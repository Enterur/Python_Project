from tkinter import *

window = Tk()

photo1 = PhotoImage(file = "C:\\Users\\kimmi\\OneDrive\\바탕 화면\\Python_Project\\week9\\dog_photo1.gif")
photo2 = PhotoImage(file = "C:\\Users\\kimmi\\OneDrive\\바탕 화면\\Python_Project\\week9\\cat.gif")
label1 = Label(window, image = photo1)
label2 = Label(window, image = photo2)

label1.pack(side = LEFT) #side = LEFT, RIGHT로 이미지 2개 출력
label2.pack(side = RIGHT)

window.mainloop()