from tkinter import *

def simple_interest():
    p,t,r = float(p_input.get()),float(time_inpu.get()),float(rate_input.get())
    sinterest = (p*t*r)/100
    result.config(text=f'{sinterest}')

screen = Tk()
screen.title('Interest Calculator')
screen.minsize(width=300,height=300)
screen.config(padx=20, pady=20)

principle = Label(text='Principle:')
principle.grid(column=0, row=1)

p_input = Entry()
p_input.grid(column=1,row=1)

rate = Label(text='Rate:')
rate.grid(column=0,row=2)

rate_input = Entry()
rate_input.grid(column=1, row=2)

time = Label(text='Time:')
time.grid(column=0, row=3)

time_inpu = Entry()
time_inpu.grid(column=1, row=3)

si = Label(text='SI:')
si.grid(column=0, row=4)
result = Label(text='0')
result.grid(column=1, row=4)

mybutton = Button(text='Calculate',command = simple_interest)
mybutton.grid(column=1,row=5)

screen.mainloop()