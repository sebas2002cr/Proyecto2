
import tkinter as tk
from tkinter import*


ventana = tk.Tk()

ventana.geometry('1400x800')
ventana.resizable(0, 0)
ventana.config( bg = "lightgreen")







carta = tk,Button(ventana,
                    text = "CARTA 1", width = 15 , height = 15 ,
                    bg='red',
                    fg='red').pack(side=TOP  )

button1 = tk.Button(ventana, 
                    text='Comer', 
                    bg='blue',
                    fg='red').pack(side=TOP , padx = 10 , pady = 10)
button2 = tk.Button(ventana, 
                    text='Botar', 
                    bg='red', 
                    fg='red').pack(side = TOP , padx = 10 , pady = 10)
button3 = tk.Label(ventana, 
                   text='Cambiar de carta', 
                   bg='white',
                   fg='red').pack(side = TOP , padx = 10 , pady = 10)




carta2 = tk,Button(ventana,
                    text = "CARTA 2", width = 15 , height = 15 ,
                    bg='red', 
                    fg='red').pack(side=BOTTOM  )

button4 = tk.Button(ventana, 
                    text='Comer', 
                    bg='red', 
                    fg='red').pack(side=BOTTOM  , padx = 10 , pady = 10)
button5 = tk.Button(ventana, 
                    text='Botar', 
                    bg='red', 
                    fg='red').pack(side=BOTTOM , padx = 10 , pady = 10)
button6 = tk.Label(ventana, 
                   text='Cambiar de carta', 
                   bg='white',
                   fg='red').pack(side=BOTTOM , padx = 10 , pady = 10)


mazo = tk,Button(ventana,
                    text = "mazo", width = 15 , height = 25 ,
                    bg='red',
                    fg='red').pack(side=LEFT  )

botadas = tk,Button(ventana,
                    text = "botadas", width = 15 , height = 25 ,
                    bg='red',
                    fg='red').pack(side=RIGHT  )


ventana.mainloop()

