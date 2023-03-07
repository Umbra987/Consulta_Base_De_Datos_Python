import tkinter as grafico
from tkinter import ttk

def open_Ventana_Impresion(resultados_busqueda):
    ventana2 = grafico.Toplevel();
    ventana2.title("RESULTADOS");
    ventana2.geometry("700x500");

    

    columnas = resultados_busqueda.columns;


    y = 0;

    for x in range(len(columnas)):
        if columnas[x] == "ubicacion" or columnas[x] == "departamento_nom" or columnas[x] == "edad" or columnas[x] == "fuente_tipo_contagio" or columnas[x] == "estado" or columnas[x] == "tipo_recuperacion":
            columna = grafico.Label(ventana2,text=f" {columnas[x]} ");
            columna.grid(row=0 , column=y);
            y = y + 1;

    z = 0;

    for j in range (len(resultados_busqueda)):
        for i in range (len(resultados_busqueda.columns)):
            if columnas[i] == "ubicacion" or columnas[i] == "departamento_nom" or columnas[i] == "edad" or columnas[i] == "fuente_tipo_contagio" or columnas[i] == "estado" or columnas[i] == "tipo_recuperacion":
                fila = grafico.Label(ventana2,text=f"{resultados_busqueda.iloc[j][i]}");
                fila.grid(row=j+1,column=z);
                z = z + 1;
            
            if i >= 18:
                i = 0;
                z = 0;
            else: 
                i+=1


    #scroll = grafico.Scrollbar(ventana2)
    #scroll.pack(side="bottom" , fill=grafico.X)

    
    
    