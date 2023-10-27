from tkinter import*
ventana=Tk()


widget_uno=Frame()
widget_uno.grid(row=6,column=0)
widget_uno.config(height='30',width='30')


et=Label(ventana,text='Ingresa un numero 1:').grid(row=0,column=0)
num1=Entry()
num1.grid(row=1,column=0)

et=Label(ventana,text='Ingresa un numero 2:').grid(row=2,column=0)
num2=Entry()
num2.grid(row=3,column=0)

et=Label(ventana,text='RESULTADO').grid(row=4,column=0)
result=Entry()
result.grid(row=5,column=0)




datos=IntVar()

class Operadores:
    
    def operar():
        n1=int(num1.get())
        n2=int(num2.get())
        if datos.get()==1:
            resultado_suma=n1+n2
            result.insert(0,resultado_suma)
        else:
            resultado_resta=n1-n2
            result.insert(0,resultado_resta)


radios=Radiobutton(ventana,text='SUMAR',value=1,variable=datos)
radios.grid(row=2,column=1)

radior=Radiobutton(ventana,text='RESTAR',value=0,variable=datos)
radior.grid(row=3,column=1)

boton_suma=Button(ventana,text='CALCULAR',command=operar).grid(row=7,column=0)

def limpiar():
    num1.delete(0,END)
    num2.delete(0,END)
    result.delete(0,END)
    num1.focus()
boton_limpiar=Button(ventana,text='Limpiar',command=limpiar).grid(row=7,column=1)


ventana.mainloop()
