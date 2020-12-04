from tkinter import *
root = Tk()
root.title('Сумма чисел')



EntryA = Entry(root, width=10, font='Arial 16')
EntryB = Entry(root, width=10, font='Arial 16')
EntryC = Entry(root, width=20, font='Arial 16')

# размещаем первые два поля справа от меток, второй столбец (отсчет от нуля)
EntryA.grid(row=0, column=1, sticky=E)
EntryB.grid(row=1, column=1, sticky=E)



# третье текстовое поле ввода занимает всю ширину строки 2
# columnspan — объединение ячеек по столбцам; rowspan — по строкам
EntryC.grid(row=3, columnspan=2)



def summa():
    a = EntryA.get() # берем текст из первого поля
    a = int(a) # преобразуем в число целого типа

    b = EntryB.get() 
    b = int(b)

    result = str(a + b) # результат переведем в строку для дальнейшего вывода
    EntryC.delete(0, END) # очищаем текстовое поле полностью
    EntryC.insert(0, result) # вставляем результат в начало 

# размещаем кнопку в строке 3 во втором столбце  
but = Button(root, text='Сложить!', command=summa)
but.grid(row=2, column=1, sticky=E)

def dvoich():
	a = EntryA.get()
	a = int(a)

	result = (bin(a)[2:])
	EntryA.delete(0, END)
	EntryA.insert(0, result)

	b = EntryB.get()
	b = int(b)

	result = (bin(b)[2:])
	EntryB.delete(0, END)
	EntryB.insert(0, result)

def vosmi():
	a = EntryA.get()
	a = int(a)

	result = (oct(a)[2:])
	EntryA.delete(0, END)
	EntryA.insert(0, result)

	b = EntryB.get()
	b = int(b)

	result = (oct(b)[2:])
	EntryB.delete(0, END)
	EntryB.insert(0, result)

def shesn():
	a = EntryA.get()
	a = int(a)

	result = (hex(a)[2:])
	EntryA.delete(0, END)
	EntryA.insert(0, result)

	b = EntryB.get()
	b = int(b)

	result = (hex(b)[2:])
	EntryB.delete(0, END)
	EntryB.insert(0, result)

var = IntVar()
var.set(0)
Radiobutton(root, text="2-я система", command=dvoich, variable=var, value=1).grid(row=0, sticky=W)
Radiobutton(root, text="8-я система", command=vosmi, variable=var, value=2).grid(row=1, sticky=W)
Radiobutton(root, text="16-я система", command=shesn, variable=var, value=3).grid(row=2, sticky=W)


root.mainloop()