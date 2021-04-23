from tkinter import * 
import tkinter as tk
from tkinter import ttk
from unitconvert import lengthunits, temperatureunits, volumeunits, massunits

root = tk.Tk()
root.geometry("400x400")


userin = IntVar()
resultin = IntVar()
uf = StringVar()
us = StringVar()

def clearFunc():
    userin.set("")
    resultin.set("")
    uf.set("")
    us.set("")

def conv1():
    a = lengthunits.LengthUnit(userin.get(), f'{uf.get()}', f'{us.get()}').doconvert()
    resultin.set(a)


def conv2():
    a = temperatureunits.TemperatureUnit(userin.get(), f'{uf.get()}', f'{us.get()}').doconvert()
    resultin.set(a)


def conv3():
    a = massunits.MassUnit(userin.get(), f'{uf.get()}', f'{us.get()}').doconvert()
    resultin.set(a)


def conv4():
    a = volumeunits.VolumeUnit(userin.get(), f'{uf.get()}', f'{us.get()}').doconvert()
    resultin.set(a)



def mk():

    clearFunc()
    new_window = Toplevel(root)
    new_window.title("Distance")
    
    

    head = Label(new_window,text="Miles/Kilometer", font= ('comic sans', 20))
    head.grid(row=0,column=0,columnspan=2)


    userinput = Entry(new_window, textvariable=userin, font=('comic sans', 20),width=10)
    userinput.grid(row=1,column=0,padx=10,pady=10)


    unitfirst = ttk.Combobox(new_window, textvariable=uf, font=('comic sans', 20),width=10)
    unitfirst['value'] = ('mi', 'km')
    unitfirst.grid(row=1,column=1, padx=10,pady=10)

    result = Label(new_window, textvariable=resultin, font=('comic sans', 20))
    result.grid(row=2, column=0, padx=10,pady=10)


    unitsecond = ttk.Combobox(new_window, textvariable=us,font=('comic sans', 20),width=10)
    unitsecond['value'] = ('mi', 'km')
    unitsecond.grid(row=2,column=1, padx=10,pady=10)


    submit = Button(new_window, text="SUBMIT", font=('comic sans', 10),command=conv1)
    submit.grid(row=3,columnspan=2, padx=10,pady=10)

    close = Button(new_window, text="CLOSE",  command=lambda: new_window.destroy())
    close.grid(row=4,columnspan=2, padx=10,pady=10)

    reset = Button(new_window, text="RESET",  command=clearFunc)
    reset.grid(row=5,columnspan=2, padx=10,pady=10)

    

def cf():
    clearFunc()
    new_window = Toplevel(root)
    new_window.title("Temperature")
    
    

    head = Label(new_window,text="Celcius/Fahrenheit", font= ('comic sans', 20))
    head.grid(row=0,column=0,columnspan=2)


    userinput = Entry(new_window, textvariable=userin, font=('comic sans', 20),width=10)
    userinput.grid(row=1,column=0,padx=10,pady=10)


    unitfirst = ttk.Combobox(new_window, textvariable=uf, font=('comic sans', 20),width=10)
    unitfirst['value'] = ('C', 'F')
    unitfirst.grid(row=1,column=1, padx=10,pady=10)

    result = Label(new_window, textvariable=resultin, font=('comic sans', 20))
    result.grid(row=2, column=0, padx=10,pady=10)


    unitsecond = ttk.Combobox(new_window, textvariable=us,font=('comic sans', 20),width=10)
    unitsecond['value'] = ('C', 'F')
    unitsecond.grid(row=2,column=1, padx=10,pady=10)


    submit = Button(new_window, text="SUBMIT", font=('comic sans', 10),command=conv2)
    submit.grid(row=3,columnspan=2, padx=10,pady=10)

    close = Button(new_window, text="CLOSE", command=lambda: new_window.destroy())
    close.grid(row=4,columnspan=2, padx=10,pady=10)

    reset = Button(new_window, text="RESET",  command=clearFunc)
    reset.grid(row=5,columnspan=2, padx=10,pady=10)

    

def pl():
    clearFunc()
    new_window = Toplevel(root)
    new_window.title("Volume")
    
    

    head = Label(new_window,text="Pints/Litres", font= ('comic sans', 20))
    head.grid(row=0,column=0,columnspan=2)


    userinput = Entry(new_window, textvariable=userin, font=('comic sans', 20),width=10)
    userinput.grid(row=1,column=0,padx=10,pady=10)


    unitfirst = ttk.Combobox(new_window, textvariable=uf, font=('comic sans', 20),width=10)
    unitfirst['value'] = ('pt', 'l')
    unitfirst.grid(row=1,column=1, padx=10,pady=10)

    result = Label(new_window, textvariable=resultin, font=('comic sans', 20))
    result.grid(row=2, column=0, padx=10,pady=10)


    unitsecond = ttk.Combobox(new_window, textvariable=us,font=('comic sans', 20),width=10)
    unitsecond['value'] = ('pt', 'l')
    unitsecond.grid(row=2,column=1, padx=10,pady=10)


    submit = Button(new_window, text="SUBMIT", font=('comic sans', 10),command=conv4)
    submit.grid(row=3,columnspan=2, padx=10,pady=10)

    close = Button(new_window, text="CLOSE", command=lambda: new_window.destroy())
    close.grid(row=4,columnspan=2, padx=10,pady=10)

    reset = Button(new_window, text="RESET",  command=clearFunc)
    reset.grid(row=5,columnspan=2, padx=10,pady=10)

    

def ks():
    clearFunc()
    new_window = Toplevel(root)
    new_window.title("Mass")
    
    

    head = Label(new_window,text="Pints/Litres", font= ('comic sans', 20))
    head.grid(row=0,column=0,columnspan=2)


    userinput = Entry(new_window, textvariable=userin, font=('comic sans', 20),width=10)
    userinput.grid(row=1,column=0,padx=10,pady=10)


    unitfirst = ttk.Combobox(new_window, textvariable=uf, font=('comic sans', 20),width=10)
    unitfirst['value'] = ('mg', 'kg')
    unitfirst.grid(row=1,column=1, padx=10,pady=10)

    result = Label(new_window, textvariable=resultin, font=('comic sans', 20))
    result.grid(row=2, column=0, padx=10,pady=10)


    unitsecond = ttk.Combobox(new_window, textvariable=us,font=('comic sans', 20),width=10)
    unitsecond['value'] = ('mg', 'kg')
    unitsecond.grid(row=2,column=1, padx=10,pady=10)


    submit = Button(new_window, text="SUBMIT", font=('comic sans', 10),command=conv3)
    submit.grid(row=3,columnspan=2, padx=10,pady=10)

    close = Button(new_window, text="CLOSE", command=lambda: new_window.destroy())
    close.grid(row=4,columnspan=2, padx=10,pady=10)

    reset = Button(new_window, text="RESET",  command=clearFunc)
    reset.grid(row=5,columnspan=2, padx=10,pady=10)

    





distance = Button(root, text="Distance", font=('comic sans', 10), command=mk)
distance.grid(row=1,columnspan=2, padx=100,pady=10)

temperature = Button(root, text="Temperature", font=('comic sans', 10),  command=cf)
temperature.grid(row=2,columnspan=2, padx=100,pady=10)

volume = Button(root, text="Volume", font=('comic sans', 10), command=pl)
volume.grid(row=3,columnspan=2, padx=100,pady=10)

mass = Button(root, text="Mass", font=('comic sans', 10), command=ks)
mass.grid(row=4,columnspan=2, padx=100,pady=10)

close = Button(root, text="CLOSE", command=lambda: root.destroy())
close.grid(row=5,columnspan=2, padx=10,pady=10)


root.title("Converter")
root.mainloop()