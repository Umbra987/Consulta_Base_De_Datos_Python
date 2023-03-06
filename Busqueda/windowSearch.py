import tkinter as grafico
from tkinter import ttk

def open_Ventana_Impresion(resultados_busqueda):
    ventana2 = grafico.Toplevel();
    ventana2.title("RESULTADOS");
    ventana2.geometry("700x500");

    

    columnas = resultados_busqueda.columns;

    for x in range(len(columnas)):
        columna = grafico.Label(ventana2,text=f" {columnas[x]} ");
        columna.grid(row=0 , column=x);


    for j in range (len(resultados_busqueda)):
        for i in range (len(resultados_busqueda.columns)):
            fila = grafico.Label(ventana2,text=f"{resultados_busqueda.iloc[j][i]}");
            fila.grid(row=j+1,column=i);
            if i >= 18:
                i = 0
            else: 
                i+=1

        if i == 18:
            j+=1;


    #scroll = grafico.Scrollbar(ventana2)
    #scroll.pack(side="bottom" , fill=grafico.X)

    
    
    