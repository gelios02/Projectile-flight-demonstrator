import math
import time
from tkinter import *

root = Tk()
mx = 1000
my = 600
root.geometry("1000x600")
root.resizable(height=False, width=False)
root.title("Demonstrator")


def stop():
    time_duration = 4.5
    time.sleep(time_duration)


class EntryWithPlaceholder(Entry):

    def __init__(self, master=None, placeholder="PLACEHOLDER", color='grey'):
        super().__init__(master)

        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']

        self.bind("<FocusIn>", self.foc_in)
        self.bind("<FocusOut>", self.foc_out)

        self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color

    def foc_in(self, *args):
        if self['fg'] == self.placeholder_color:
            self.delete('0', 'end')
            self['fg'] = self.default_fg_color

    def foc_out(self, *args):
        if not self.get():
            self.put_placeholder()


c = Canvas(root, width=mx, height=400, bg='#cfcfcf')
c.pack()


# label_1.pack(side= LEFT)


def ball(x, y, km):
    c.create_oval(x * km - 5, y - 10, x * km + 5, y, width=2, fill="red")


def ball2(x, y, km, sy):
    c.create_oval(x * km - 10, sy - y * km - 10, x * km, sy - y * km, width=2, fill="orange")


def correct(v, inp):
    if inp.isdigit():
        # print(v)
        return True
    elif inp is "":
        # print(inp)
        return True
    else:
        # print(inp)
        return False


reg = root.register(correct)

# v0 = int(input('v0='))
# alf = int(input('alf=')) * math.pi / 180


c.create_line(0, my - 200, mx, my - 200, width=5, fill="green")


def do_c():
    mes.config(text="m/s", font=('Arial', 9, 'bold'))
    mes1.config(text="0", font=('Arial', 9, 'bold'))

    mes2.config(text="m.", font=('Arial', 9, 'bold'))
    mes3.config(text="m.", font=('Arial', 9, 'bold'))

    mes4.config(text="sec.", font=('Arial', 9, 'bold'))

    v0 = float(v.get())
    alf = float(f.get()) * math.pi / 180
    g = 9.8
    x = v0 ** 2 * math.sin(2 * alf) / g
    m = 20
    t = 0
    while t < 2 * v0 * math.sin(alf) / g:

        time.sleep(0.0005)
        c.update()
        x_all = (v0 * math.cos(alf) * t)
        y_all = (v0 * math.sin(alf) * t - (g * t ** 2) / 2) / 160
        fly: float = 2 * v0 * math.sin(alf) / g

        def frange(start, stop, step):
            i = start
            while i < stop:
                yield i
                i += step

        for x in frange(0.1, fly, 0.1):
            # time.sleep(0.1)
            label.config(text=str(x))
            label.update()

        # print(x_all, y_all)

        label_x.config(text=str(x_all))
        label_x.update()

        label_y.config(text=str(y_all))
        label_y.update()

        if 0 < v0 <= 21:
            t += 0.02
            x2 = (v0 * math.cos(alf) * t)
            y2 = (v0 * math.sin(alf) * t - (g * t ** 2) / 2)
            ball2(x2, y2, m, my - 200)
        if 22 <= v0 <= 31:
            t += 0.02
            x2 = (v0 * math.cos(alf) * t) / 2
            y2 = (v0 * math.sin(alf) * t - (g * t ** 2) / 2) / 2
            ball2(x2, y2, m, my - 200)
        if 32 <= v0 <= 48:
            t += 0.04
            x2 = (v0 * math.cos(alf) * t) / 6
            y2 = (v0 * math.sin(alf) * t - (g * t ** 2) / 2) / 6
            ball2(x2, y2, m, my - 200)
        if 49 <= v0 <= 70:
            t += 0.04
            x2 = (v0 * math.cos(alf) * t) / 10
            y2 = (v0 * math.sin(alf) * t - (g * t ** 2) / 2) / 10
            ball2(x2, y2, m, my - 200)
        if 71 <= v0 <= 110:
            t += 0.06
            x2 = (v0 * math.cos(alf) * t) / 26
            y2 = (v0 * math.sin(alf) * t - (g * t ** 2) / 2) / 26
            ball2(x2, y2, m, my - 200)
        if 111 <= v0 <= 160:
            t += 0.08
            x2 = (v0 * math.cos(alf) * t) / 54
            y2 = (v0 * math.sin(alf) * t - (g * t ** 2) / 2) / 54
            ball2(x2, y2, m, my - 200)
        if 161 <= v0 <= 210:
            t += 0.1
            x2 = (v0 * math.cos(alf) * t) / 80
            y2 = (v0 * math.sin(alf) * t - (g * t ** 2) / 2) / 80
            ball2(x2, y2, m, my - 200)
        if 211 <= v0 <= 300:
            t += 0.15
            x2 = (v0 * math.cos(alf) * t) / 200
            y2 = (v0 * math.sin(alf) * t - (g * t ** 2) / 2) / 200
            ball2(x2, y2, m, my - 200)
        if 301 <= v0 <= 400:
            t += 0.22
            x2 = (v0 * math.cos(alf) * t) / 430
            y2 = (v0 * math.sin(alf) * t - (g * t ** 2) / 2) / 430
            ball2(x2, y2, m, my - 200)
        if 401 <= v0 <= 490:
            t += 0.23
            x2 = (v0 * math.cos(alf) * t) / 520
            y2 = (v0 * math.sin(alf) * t - (g * t ** 2) / 2) / 520
            ball2(x2, y2, m, my - 200)
        if 491 <= v0 <= 590:
            t += 0.4
            x2 = (v0 * math.cos(alf) * t) / 800
            y2 = (v0 * math.sin(alf) * t - (g * t ** 2) / 2) / 800
            ball2(x2, y2, m, my - 200)
        if 591 <= v0 <= 700:
            t += 0.6
            x2 = (v0 * math.cos(alf) * t) / 1400
            y2 = (v0 * math.sin(alf) * t - (g * t ** 2) / 2) / 1400
            ball2(x2, y2, m, my - 200)
        if 701 <= v0 <= 800:
            t += 1
            x2 = (v0 * math.cos(alf) * t) / 1800
            y2 = (v0 * math.sin(alf) * t - (g * t ** 2) / 2) / 1800
            ball2(x2, y2, m, my - 200)

    # print('Общее время полета до поверхности земли = ', 2 * v0 * math.sin(alf) / g)


def do_cl():
    mes.update()
    mes.config(text=" ")

    mes1.update()
    mes1.config(text=" ")

    mes2.update()
    mes2.config(text=" ")

    mes3.update()
    mes3.config(text=" ")

    mes4.update()
    mes4.config(text=" ")

    c.delete('all')
    c.create_line(0, my - 200, mx, my - 200, width=5, fill="green")

    v.delete(0, END)
    f.delete(0, END)

    label_x.config(text="")
    label_x.config(text="X coordinates", font=('Arial', 12, 'bold'))
    label_x.pack()
    label_x.place(x=345, y=448)

    label_y.config(text="")
    label_y.config(text="Y coordinates", font=('Arial', 12, 'bold'))
    label_y.pack()
    label_y.place(x=345, y=513)

    label.config(text="")
    label.config(text="result", font=('Arial', 12, 'bold'))
    label.pack()
    label.place(x=802, y=483)


# Design
def on_enter_1(e):
    e.widget['background'] = '#5adb5e'


def on_enter_2(e):
    e.widget['background'] = '#777bf2'


def on_enter_3(e):
    e.widget['background'] = '#f54242'


def on_leave_com(e):
    e.widget['background'] = 'SystemButtonFace'


mes = Label(root, text=' ', font=('Arial', 9, 'bold'))
mes.pack()
mes.place(x=255, y=450)

mes1 = Label(root, text=' ', font=('Arial', 9, 'bold'))
mes1.pack()
mes1.place(x=255, y=498)

mes2 = Label(root, text=' ', font=('Arial', 9, 'bold'))
mes2.pack()
mes2.place(x=515, y=450)

mes3 = Label(root, text=' ', font=('Arial', 9, 'bold'))
mes3.pack()
mes3.place(x=515, y=515)

mes4 = Label(root, text=' ', font=('Arial', 9, 'bold'))
mes4.pack()
mes4.place(x=960, y=485)

btn = Button(root, text='Start',
             command=do_c,
             font=('Arial', 15, 'bold'),
             height=1,
             width=18
             )
btn.pack()
btn.place(x=29, y=550)
btn.bind('<Return>', do_c)
btn.bind("<Enter>", on_enter_1)
btn.bind("<Leave>", on_leave_com)
root.bind('<Return>', lambda event=None: btn.invoke())
root.bind('<space>', lambda event=None: stopButton.invoke())
stopButton = Button(root, height=1,
                    width=18,
                    text="Stop",
                    command=stop,
                    font=('Arial', 15, 'bold')
                    )
stopButton.pack()
stopButton.place(x=550, y=550)
stopButton.bind("<Enter>", on_enter_3)
stopButton.bind("<Leave>", on_leave_com)

btn_1 = Button(root, text='Clear',
               command=do_cl,
               font=('Arial', 15, 'bold'),
               height=1,
               width=18
               )
btn_1.pack()
btn_1.place(x=290, y=550)
btn_1.bind("<Enter>", on_enter_2)
btn_1.bind("<Leave>", on_leave_com)

label = Label(root, text='result', font=('Arial', 12, 'bold'))
label.pack()
label.place(x=790, y=483)

label_x = Label(root, text='X coordinates', font=('Arial', 12, 'bold'))
label_x.pack()
label_x.place(x=343, y=448)

label_y = Label(root, text='Y coordinates', font=('Arial', 12, 'bold'))
label_y.pack()
label_y.place(x=343, y=513)

label_1 = Label(root, text='''v0 = 

alf = ''',
                font=('Arial', 20, 'bold')
                )
label_1.place(x=29, y=441)

label_2 = Label(root, text='''X = 

Y = ''',
                font=('Arial', 20, 'bold')
                )
label_2.place(x=290, y=441)

Label_3 = Label(root, text='''Общее время полета\nдо поверхности земли = ''', justify=LEFT,
                font=('Arial', 14, 'bold')
                )
Label_3.pack()
Label_3.place(x=550, y=460)

v = EntryWithPlaceholder(root, "Enter from 0 to 800")
v.pack()
v.place(x=95, y=445, width=160, height=30)
v.config(validate="key", validatecommand=(reg, '%v', '%P'), font=('Helvetica', '12', 'bold'))

f = EntryWithPlaceholder(root, "Enter a corner")
f.pack()
f.place(x=95, y=509, width=160, height=30)
f.config(validate="key", validatecommand=(reg, '%v', '%P'), font=('Helvetica', '12', 'bold'))

# Z = EntryWithPlaceholder(root, "result")
# Z.pack()
# Z.place(x=845, y=513)

root.mainloop()
