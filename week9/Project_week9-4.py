from tkinter import *
from tkinter import messagebox

def arrowUp(event):
    messagebox.showinfo("방향키", "↑ 상측 방향키")

def arrowDown(event):
    messagebox.showinfo("방향키", "↓ 하측 방향키")

def arrowRight(event):
    messagebox.showinfo("방향키", "→ 우측 방향키")

def arrowLeft(event):
    messagebox.showinfo("방향키", "← 좌측 방향키")


window = Tk()

window.bind("<Shift-Up>", arrowUp)
window.bind("<Shift-Down>", arrowDown)
window.bind("<Shift-Right>", arrowRight)
window.bind("<Shift-Left>", arrowLeft)

window.mainloop()