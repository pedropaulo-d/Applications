from tkinter import *
from tkinter import ttk

janela = Tk()
janela.title('Calculadora')
janela.geometry('300x410')
janela.config(bg='#9c7373') #COR PRETA

frame_tela = Frame(janela, width=300, height=60, bg='#2b2b2b') #COR CINZA
frame_tela.grid(row=0, column=0)

frame_interface = Frame(janela, width=300, height=350, bg='#000000') #COR PRETA
frame_interface.grid(row=1, column=0)

valores = ''
valordo_texto = StringVar()

def entrada_valores(comando):
    global valores
    valores = valores + str(comando)
    valordo_texto.set(valores)

def calculando_valores():
    global valores
    resultado = eval(valores)
    valordo_texto.set(str(resultado))

def limpando_tela():
    global valores
    valores = ''
    valordo_texto.set('')


app_input = Label(frame_tela, textvariable=valordo_texto, width=16, height=2, padx=7, relief=FLAT, anchor='e', justify=RIGHT,
font=('Ivy 20'), bg='#2b2b2b', fg='#ffffff')
app_input.place(x=0, y=0)


b_1 = Button(frame_interface, command=limpando_tela, text='C', width=11, height=3, bg='#0f0f0f', fg='#ffffff', font=('Ivy 13 bold'), relief=RAISED,
overrelief=RIDGE)
b_1.place(x=0, y=0)
b_2 = Button(frame_interface, command = lambda: entrada_valores('%'), text='%', width=9, height=3, bg='#0f0f0f', fg='#ffffff', font=('Ivy 13 bold'), relief=RAISED,
overrelief=RIDGE)
b_2.place(x=120, y=0)
b_4 = Button(frame_interface, command = lambda: entrada_valores('/'), text='/', width=7, height=3, bg='#780000', fg='#ffffff', font=('Ivy 13 bold'),
relief=RAISED, overrelief=RIDGE)
b_4.place(x=220, y=0)

b_5 = Button(frame_interface, command = lambda: entrada_valores('7'), text='7', width=6, height=3, bg='#0f0f0f', fg='#ffffff', font=('Ivy 13 bold'), relief=RAISED,
overrelief=RIDGE)
b_5.place(x=0, y=70)
b_6 = Button(frame_interface, command = lambda: entrada_valores('8'), text='8', width=7, height=3, bg='#0f0f0f', fg='#ffffff', font=('Ivy 13 bold'), relief=RAISED,
overrelief=RIDGE)
b_6.place(x=70, y=70)
b_7 = Button(frame_interface, command = lambda: entrada_valores('9'), text='9', width=6, height=3, bg='#0f0f0f', fg='#ffffff', font=('Ivy 13 bold'), relief=RAISED,
overrelief=RIDGE)
b_7.place(x=150, y=70)
b_8 = Button(frame_interface, command = lambda: entrada_valores('*'), text='X', width=7, height=3, bg='#780000', fg='#ffffff', font=('Ivy 13 bold'),
relief=RAISED, overrelief=RIDGE)
b_8.place(x=220, y=70)
b_9 = Button(frame_interface, command = lambda: entrada_valores('4'), text='4', width=6, height=3, bg='#0f0f0f', fg='#ffffff', font=('Ivy 13 bold'), relief=RAISED,
overrelief=RIDGE)
b_9.place(x=0, y=140)
b_10 = Button(frame_interface, command = lambda: entrada_valores('5'), text='5', width=7, height=3, bg='#0f0f0f', fg='#ffffff', font=('Ivy 13 bold'), relief=RAISED,
overrelief=RIDGE)
b_10.place(x=70, y=140)
b_11 = Button(frame_interface, command = lambda: entrada_valores('6'), text='6', width=6, height=3, bg='#0f0f0f', fg='#ffffff', font=('Ivy 13 bold'), relief=RAISED,
overrelief=RIDGE)
b_11.place(x=150, y=140)
b_12 = Button(frame_interface, command = lambda: entrada_valores('-'), text='-', width=7, height=3, bg='#780000', fg='#ffffff', font=('Ivy 13 bold'),
relief=RAISED, overrelief=RIDGE)
b_12.place(x=220, y=140)
b_13 = Button(frame_interface, command = lambda: entrada_valores('1'), text='1', width=6, height=3, bg='#0f0f0f', fg='#ffffff', font=('Ivy 13 bold'), relief=RAISED,
overrelief=RIDGE)
b_13.place(x=0, y=210)
b_14 = Button(frame_interface, command = lambda: entrada_valores('2'), text='2', width=7, height=3, bg='#0f0f0f', fg='#ffffff', font=('Ivy 13 bold'), relief=RAISED,
overrelief=RIDGE)
b_14.place(x=70, y=210)
b_15 = Button(frame_interface, command = lambda: entrada_valores('3'), text='3', width=6, height=3, bg='#0f0f0f', fg='#ffffff', font=('Ivy 13 bold'), relief=RAISED,
overrelief=RIDGE)
b_15.place(x=150, y=210)
b_12 = Button(frame_interface, command = lambda: entrada_valores('+'), text='+', width=7, height=3, bg='#780000', fg='#ffffff', font=('Ivy 13 bold'),
relief=RAISED, overrelief=RIDGE)
b_12.place(x=220, y=210)
b_13 = Button(frame_interface, command = lambda: entrada_valores('0'), text='0', width=11, height=3, bg='#0f0f0f', fg='#ffffff', font=('Ivy 13 bold'), relief=RAISED,
overrelief=RIDGE)
b_13.place(x=0, y=280)
b_14 = Button(frame_interface, text='%', width=9, height=3, bg='#0f0f0f', fg='#ffffff', font=('Ivy 13 bold'), relief=RAISED,
overrelief=RIDGE)
b_14.place(x=120, y=280)
b_15 = Button(frame_interface, command=calculando_valores, text='=', width=7, height=3, bg='#780000', fg='#ffffff', font=('Ivy 13 bold'),
relief=RAISED, overrelief=RIDGE)
b_15.place(x=220, y=280)



janela.mainloop()
