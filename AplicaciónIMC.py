
from ast import Delete
from cProfile import label
from cgitb import reset
from distutils.cmd import Command
from email.mime import text
from faulthandler import disable
from msilib.schema import Class
from sre_parse import State
from struct import pack
import time
import tkinter 
from tkinter import *
from tkinter.ttk import Labelframe
from turtle import position
from webbrowser import get

# VENTANA

ventana = tkinter.Tk()
ventana.geometry("600x300")
ventana.title("Calculador de Masa Corporal")

# VARIABLES Y ETIQUETAS

Peso = StringVar
Peso = tkinter.Entry(ventana)
Peso.pack()

etiqueta1 = tkinter.Label(ventana,text="\nIngresa tu peso en kilogramos (sólo el número): ")
etiqueta1.config()
etiqueta1.pack()

Altura = tkinter.StringVar()
Altura = tkinter.Entry(ventana)
Altura.pack()

etiqueta2 = tkinter.Label(ventana,text="Ingresa tu altura en metro (Separa decimales con punto): ")
etiqueta2.pack()

# FUNCIONES

def Calcular():
    IMC = (round(float(Peso.get()) / pow(float(Altura.get()),2),2))
    

    if IMC <= 18.5:
        res1 = tkinter.Label(ventana,text="Tu índice es: "+str(IMC)+ " .Estas por debajo de lo recomendado. Consulta con tu médico/a")
        res1.pack() 
        botonresultado["state"]= "disabled"                                  
    elif IMC >= 18.5 and IMC <= 24.9:
        res2= tkinter.Label(ventana,text="Tu índice es: "+str(IMC)+ " .Estás saludable")
        res2.pack()
        botonresultado["state"]= "disabled"        
    elif IMC >= 25 and IMC <= 29.9:
        res3= tkinter.Label(ventana,text="Tu índice es: "+str(IMC)+ " -Tienes sobrepeso. Consulta con tu médico/a")
        res3.pack()
        botonresultado["state"]= "disabled"        
    elif IMC >= 30 and IMC <= 34.9:
        res4= tkinter.Label(ventana,text="Tu índice es: "+str(IMC)+ " .Tienes obesidad grado I. Consulta con tu médico/a")
        res4.pack()
        botonresultado["state"]= "disabled"       
    elif IMC >= 35 and IMC <= 39.9:
        res5= tkinter.Label(ventana,text="Tu índice es: "+str(IMC)+ " .Tienes obesidad grado II. Consulta con tu médico/a")        
        res5.pack()
        botonresultado["state"]= "disabled"
    else:
        res6 = tkinter.Label(ventana,text="Tu índice es: "+ str(IMC)+ " .Tienes obesidad grado III. Consulta con tu médico/a")
        res6.pack()
        botonresultado["state"]= "disabled"
     
def borrar():
    botonresultado.config(state="normal")
    Peso.delete(0,1000)
    Altura.delete(0,1000)
    ventana.winfo_children()[6].destroy()
    
    
    
# BOTONES         

    
botonresultado = tkinter.Button(ventana,text="Calcular")
botonresultado.configure(command=Calcular)
botonresultado.pack()


boton_borrado = tkinter.Button(ventana,text="Borrar",command=borrar) 
boton_borrado.pack()  


 

ventana.mainloop()
