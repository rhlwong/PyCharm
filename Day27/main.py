import tkinter

window = tkinter.Tk()




def add(*args):
    for n in args:
        print(n)

def cal(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key)
cal(a=1, b=2)
window.mainloop()