import tkinter as grafico
from tkinter import *

def open_Ventana_Impresion(resultados_busqueda):
    ventana = Toplevel();#creacion de una ventana secundaria
    ventana.title("RESULTADOS");#titulo de la ventana
    ventana.iconbitmap("virus.ico");

    # Crear un widget Canvas con una barra de desplazamiento vertical
    canvas = Canvas(ventana);
    scrollbar = Scrollbar(ventana, orient="vertical", command=canvas.yview);#creacion del la barra de desplazamiento vertical para cuando el usuario pide muchos registros.
    scrollbar.pack(side="right", fill="y");
    canvas.configure(yscrollcommand=scrollbar.set);

    # Agregar el widget Canvas a la ventana principal
    canvas.pack(side="left", fill="both", expand=True);

    # Crear un frame dentro del widget Canvas para contener el contenido
    frame = Frame(canvas);
    canvas.create_window((0, 0), window=frame, anchor="nw");

    # Agregar el contenido al frame
    columna = resultados_busqueda.columns
    y = 0;
    for x in range(len(columna)):#Bucle para la impresion del nombre de las columnas solicitadas.
        if columna[x] == "ubicacion" or columna[x] == "departamento_nom" or columna[x] == "ciudad_municipio_nom" or columna[x] == "edad" or columna[x] == "fuente_tipo_contagio" or columna[x] == "estado" or columna[x] == "tipo_recuperacion":
            columnas =Label(frame,text=f" {columna[x]} ");
            columnas.grid(row=0, column=y);
            y = y + 1;
    columnas =Label(frame,text=f" Nacionalidad ");#Se agrega la columna nacionalidad para cumplir los requisitos del contrato
    columnas.grid(row=0, column=y);

    z = 0
    for j in range (len(resultados_busqueda)):#Bucle de impresion de los datos por un doble bucle donde se verifica que el dato que se imprima pertenezca a una de las columnas solicitadas
        for i in range (len(resultados_busqueda.columns)):
            if columna[i] == "ubicacion" or columna[i] == "departamento_nom" or columna[i] == "ciudad_municipio_nom" or columna[i] == "edad" or columna[i] == "fuente_tipo_contagio" or columna[i] == "estado" or columna[i] == "tipo_recuperacion":
                fila = Label(frame,text=f"{resultados_busqueda.iloc[j][i]}");
                fila.grid(row=j+1, column=z);
                z = z + 1;
            if i >= 18:
                fila =Label(frame,text=f" nan ");#ya que la columna nacionalidad no existe en el dataFrame se imprime "nan".
                fila.grid(row=j+1, column=7);
                i = 0;
                z = 0;
            else:                                               
                i+=1;

    # Configurar el tamaño del widget Canvas y el frame interno
    frame.update_idletasks();
    canvas.config(scrollregion=canvas.bbox("all"));
    canvas.config(width=700, height=500);
    ventana.mainloop();
    
    