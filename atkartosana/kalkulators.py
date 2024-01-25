from tkinter import *

logs = Tk()
logs.geometry('600x400')
logs.configure(bg='#fcc4dc')

def rekinat ():
    sk1 = int(skaitlis1.get())
    sk2 = int(skaitlis2.get())
    summa = sk1 + sk2
    atbilde.configure(text = summa)

skaitlis1 = Entry(logs, width = 5, font = ('Arial',40))
skaitlis2 = Entry(logs, width = 5, font = ('Arial',40))
skaitlis1.configure(fg = '#741b47')
skaitlis2.configure(fg = '#741b47')
plus = Label(logs,text = '+', font = ('Arial',40))
plus.configure(bg='#fcc4dc')
plus.configure(fg= '#a7204c')
ir = Label(logs,text = '=', font = ('Arial',40))
ir.configure(bg='#fcc4dc')
ir.configure(fg= '#a7204c')
poga = Button(logs, text = 'Rēķināt', font = ('Arial',20), command = rekinat)
poga.configure(bg= '#a7204c')
poga.configure(fg='#fcc4dc')
atbilde = Label(logs,text = '', font = ('Arial',40))
atbilde.configure(bg='#fcc4dc')
atbilde.configure(fg = '#741b47')


skaitlis1.grid(row = 0, column=0)
skaitlis2.grid(row = 0, column=2)
plus.grid(row = 0, column=1)
ir.grid(row = 0, column=3)
poga.grid(row = 1, column=1)
atbilde.grid(row = 0, column=4)

logs.mainloop()