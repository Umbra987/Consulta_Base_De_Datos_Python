import tkinter as grafico
from tkinter import messagebox
from Busqueda.windowSearch import open_Ventana_Impresion
from df.consulta import consulta_base_de_datos

#Consulta a la base de datos con los valores entregados por el usuario
def consulta():
    dep = departamento_name.get().upper();#Obtencion del valor en el entry y a su vez luego con el metodo upper() poner todo en mayuscula
    limit = int(value_limite.get());#Obtencion del valor del entry que es de class int

    results = consulta_base_de_datos(dep,limit);#llamado a la funcion que esta en el modulo df

    if results.empty == True:#Si no se encuentran datos se envia un messagebox
       messagebox.showinfo(message="No hay resultados de la busqueda", title="ERROR");
    else:
        open_Ventana_Impresion(results);#Imprimimos los resultados llamando a la funcion en el modulo busqueda.



#Impresion de los datos
# def impresion_DataFrame

#Ventana de consulta
ventana = grafico.Tk();
ventana.geometry("700x500");
ventana.title("Contaminación COVID-19");


etiqueta = grafico.Label(ventana,text="Contaminación COVID-19",font='Helvetica 20 bold');
etiqueta.pack(fill = grafico.X,pady = 20);

#Creacion del texto y el entry para ingresar el departamento
letrerodep = grafico.Label(ventana,text="Ingrese el nombre del departamento:");
letrerodep.pack();
departamento_name = grafico.Entry(ventana);
departamento_name.pack(pady= 10);

#Creacion del texto y el entry para ingresar el limite de resultados que se desean obtener
letrerolimit = grafico.Label(ventana,text="Ingrese el limite de consultas:");
letrerolimit.pack();
value_limite = grafico.Entry(ventana);
value_limite.pack(pady = 10);


#Boton para enviar los datos a la funcion consulta
enviar = grafico.Button(ventana, text="Consultar", bg= "#090979", padx= 50, pady= 10 , command= consulta); 
enviar.pack();



ventana.mainloop();
#Fin ventana de consulta

