import tkinter
import pickle
import joblib
from tkinter import ttk
from tkinter import messagebox
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
ventana = tkinter.Tk()

ventana.title("Entrada de datos")
#Nitroso
def Nitroso_message():
    messagebox.showinfo("Mensaje", "En esta casilla se ingresa el Nitroso en tierra")

#Phosphoru
def Phosphoru_message():
    messagebox.showinfo("Mensaje", "En esta casilla se ingresa el Fosforo en Tierra")
#Mensaje colesterol
def Potasio_message():
    messagebox.showinfo("Mensaje", "En esta casilla se ingresa el Potasio en Tierra")

def temperature_message():
    messagebox.showinfo("Mensaje", "En esta casilla se ingresa la Temperatura promedio de la zona")

def humidity_message():
    messagebox.showinfo("Mensaje", "En esta casilla se ingresa la humedad Promedio de la zona ")

def ph_message():
    messagebox.showinfo("Mensaje", "En esta casilla se ingresa el ph de la tierra ")

def rainfall_message():
    messagebox.showinfo("Mensaje", "En esta casilla se la precipitación ")




frame = tkinter.Frame(ventana)
frame.pack()
#Frame del paciente
info_usuario_frame = tkinter.LabelFrame(frame, text="Datos de entrada")
info_usuario_frame.grid(row=0, column=0, padx=20, pady=20)
#Entrada de la edad del paciente

Nitroso_label= tkinter.Label(info_usuario_frame, text="Nitroso")
Nitroso_label.grid(row=0, column=0)
Nitroso_entry = ttk.Entry(info_usuario_frame)
Nitroso_entry.grid(row=1, column=0)
Nitroso_entry.bind("<Button-1>", lambda e: Nitroso_message())


#Fosforo
Phosphoru_label= tkinter.Label(info_usuario_frame, text="Fosforo")
Phosphoru_label.grid(row=0, column=1)
Phosphoru_entry = tkinter.Entry(info_usuario_frame)
Phosphoru_entry.grid(row=1, column=1)
Phosphoru_entry.bind("<Button-1>", lambda e: Phosphoru_message())

#Potasio
Potasio_label= tkinter.Label(info_usuario_frame, text="Potasio")
Potasio_label.grid(row=0, column=2)
Potasio_entry = tkinter.Entry(info_usuario_frame)
Potasio_entry.grid(row=1, column=2)
Potasio_entry.bind("<Button-1>", lambda e: Potasio_message())

temperature_label= tkinter.Label(info_usuario_frame, text="temperatura")
temperature_label.grid(row=0, column=3)
temperature_entry = tkinter.Entry(info_usuario_frame)
temperature_entry.grid(row=1, column=3)
temperature_entry.bind("<Button-1>", lambda e: temperature_message())


humidity_label= tkinter.Label(info_usuario_frame, text="humidity")
humidity_label.grid(row=2, column=0)
humidity_entry = tkinter.Entry(info_usuario_frame)
humidity_entry.grid(row=3, column=0)
humidity_entry.bind("<Button-1>", lambda e: humidity_message())

ph_label= tkinter.Label(info_usuario_frame, text="PH")
ph_label.grid(row=2, column=1)
ph_entry = tkinter.Entry(info_usuario_frame)
ph_entry.grid(row=3, column=1)
ph_entry.bind("<Button-1>", lambda e: ph_message())

precipitación_label= tkinter.Label(info_usuario_frame, text="precipitación")
precipitación_label.grid(row=2, column=2)
precipitación_entry = tkinter.Entry(info_usuario_frame)
precipitación_entry.grid(row=3, column=2)
precipitación_entry.bind("<Button-1>", lambda e: rainfall_message())


#Repuesta
Respuesta_usuario_label= tkinter.Label(info_usuario_frame, text="respuesta:")
Respuesta_usuario_label.grid(row=4, column=0)


modelo_cargado= joblib.load('modelo_entrenado.pkl')



def usar_modelo():
    Target=np.ones((1, 7))
    if not Nitroso_entry.get():
        messagebox.showwarning("Advertencia", "Por favor, ingresa el Nitroso.")
    else:
        Target[0,0]=int(Nitroso_entry.get()) #Nitroso
 
    if not Phosphoru_entry.get():
        messagebox.showwarning("Advertencia", "Por favor, ingresa el fosforo")
    else:
        Target[0,1]=int(Phosphoru_entry.get()) #Fosforo

    if not Potasio_entry.get():
        messagebox.showwarning("Advertencia", "Por favor, ingresa el Potasio")
    else:       
        Target[0,2]=int(Potasio_entry.get()) #Potasio

    if not temperature_entry.get():
        messagebox.showwarning("Advertencia", "Por favor, ingrese la Temperatura")
    else:
        Target[0,3]=int(temperature_entry.get()) #temperature

    if not humidity_entry.get():
        messagebox.showwarning("Advertencia", "Por favor, ingrese la humedad")
    else:
        Target[0,4]=int(humidity_entry.get()) # humidity
    
    if not ph_entry.get():
        messagebox.showwarning("Advertencia", "Por favor, ingrese el PH")
    else:
        Target[0,5]=int(ph_entry.get()) # PH
        
    if not precipitación_entry.get():
        messagebox.showwarning("Advertencia", "Por favor, ingrese la precipitación")
    else:
        Target[0,6]=int(precipitación_entry.get()) #precipitación



    if modelo_cargado.predict (Target)==1:
        Respuesta_usuario_label= tkinter.Label(info_usuario_frame, text="respuesta:Segun los datos digitados el mejor cultivo es Arroz")
        Respuesta_usuario_label.grid(row=4, column=0)       
    elif modelo_cargado.predict (Target)==2:
        Respuesta_usuario_label= tkinter.Label(info_usuario_frame, text="respuesta:Segun los datos digitados el mejor cultivo es Maiz")
        Respuesta_usuario_label.grid(row=4, column=0)
    elif modelo_cargado.predict (Target)==3:
        Respuesta_usuario_label= tkinter.Label(info_usuario_frame, text="respuesta:Segun los datos digitados el mejor cultivo es garbanzo")
        Respuesta_usuario_label.grid(row=4, column=0)    
    elif modelo_cargado.predict (Target)==4:
        Respuesta_usuario_label= tkinter.Label(info_usuario_frame, text="respuesta:Segun los datos digitados el mejor cultivo es frijoles")
        Respuesta_usuario_label.grid(row=4, column=0) 
    elif modelo_cargado.predict (Target)==5:
        Respuesta_usuario_label= tkinter.Label(info_usuario_frame, text="respuesta:Segun los datos digitados el mejor cultivo es chícharo")
        Respuesta_usuario_label.grid(row=4, column=0)
    elif modelo_cargado.predict (Target)==6:
        Respuesta_usuario_label= tkinter.Label(info_usuario_frame, text="respuesta:Segun los datos digitados el mejor cultivo es mothbeans")
        Respuesta_usuario_label.grid(row=4, column=0)
    elif modelo_cargado.predict (Target)==8:
        Respuesta_usuario_label= tkinter.Label(info_usuario_frame, text="respuesta:Segun los datos digitados el mejor cultivo es frijol negro")
        Respuesta_usuario_label.grid(row=4, column=0)
    elif modelo_cargado.predict (Target)==11:
        Respuesta_usuario_label= tkinter.Label(info_usuario_frame, text="respuesta:Segun los datos digitados el mejor cultivo es Banano")
        Respuesta_usuario_label.grid(row=4, column=0)
    elif modelo_cargado.predict (Target)==12:
        Respuesta_usuario_label= tkinter.Label(info_usuario_frame, text="respuesta:Segun los datos digitados el mejor cultivo es mango")
        Respuesta_usuario_label.grid(row=4, column=0)
    elif modelo_cargado.predict (Target)==13:
        Respuesta_usuario_label= tkinter.Label(info_usuario_frame, text="respuesta:Segun los datos digitados el mejor cultivo es uvas")
        Respuesta_usuario_label.grid(row=4, column=0)
    elif modelo_cargado.predict (Target)==14:
        Respuesta_usuario_label= tkinter.Label(info_usuario_frame, text="respuesta:Segun los datos digitados el mejor cultivo es sandia")
        Respuesta_usuario_label.grid(row=4, column=0)
    elif modelo_cargado.predict (Target)==16:
        Respuesta_usuario_label= tkinter.Label(info_usuario_frame, text="respuesta:Segun los datos digitados el mejor cultivo es Manzana")
        Respuesta_usuario_label.grid(row=4, column=0)
    elif modelo_cargado.predict (Target)==17:
        Respuesta_usuario_label= tkinter.Label(info_usuario_frame, text="respuesta:Segun los datos digitados el mejor cultivo es Naranja")
        Respuesta_usuario_label.grid(row=4, column=0)
    elif modelo_cargado.predict (Target)==18:
        Respuesta_usuario_label= tkinter.Label(info_usuario_frame, text="respuesta:Segun los datos digitados el mejor cultivo es papaya")
        Respuesta_usuario_label.grid(row=4, column=0)
    elif modelo_cargado.predict (Target)==19:
        Respuesta_usuario_label= tkinter.Label(info_usuario_frame, text="respuesta:Segun los datos digitados el mejor cultivo es Coco")
        Respuesta_usuario_label.grid(row=4, column=0)
    elif modelo_cargado.predict (Target)==20:
        Respuesta_usuario_label= tkinter.Label(info_usuario_frame, text="respuesta:Segun los datos digitados el mejor cultivo es Algodon")
        Respuesta_usuario_label.grid(row=4, column=0)
    elif modelo_cargado.predict (Target)==22:
        Respuesta_usuario_label= tkinter.Label(info_usuario_frame, text="respuesta:Segun los datos digitados el mejor cultivo es Cafe")
        Respuesta_usuario_label.grid(row=4, column=0)
    else:
        Respuesta_usuario_label= tkinter.Label(info_usuario_frame, text="respuesta:Segun los datos digitados el mejor cultivo es Cafe")
        Respuesta_usuario_label.grid(row=4, column=0)
    

buttonModel=tkinter.Button(ventana,text='predecir', command=usar_modelo, fg="green" )
buttonModel.pack()
ventana.mainloop() 