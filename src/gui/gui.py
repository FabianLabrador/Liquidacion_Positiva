"""
gui.py

Este módulo contiene la lógica para la interfaz gráfica de usuario (GUI).
Define la ventana principal y los elementos de la interfaz.

"""

import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import pandas as pd
from processing.data_processing import procesar_datos

def cargar_imagen():
    """
    Carga una imagen desde el sistema de archivos y la adapta para su visualización en la GUI.
    
    Returns:
        ImageTk.PhotoImage: Imagen lista para ser mostrada en la interfaz gráfica.
    """
    try:
        imagen = Image.open("C:/Users/fabian.labrador/Documents/logo.png")
        imagen = imagen.resize((100, 50))
        return ImageTk.PhotoImage(imagen)
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo cargar la imagen: {e}")
        return None

def cargar_archivo(entry_widget):
    """
    Abre un cuadro de diálogo para seleccionar un archivo y muestra la ruta seleccionada en un widget de entrada.
    
    Args:
        entry_widget (tk.Entry): Widget de entrada donde se mostrará la ruta del archivo seleccionado.
    """
    filepath = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
    entry_widget.delete(0, tk.END)
    entry_widget.insert(0, filepath)

def iniciar_gui():
    """
    Inicia la interfaz gráfica de usuario.
    """
    ventana = tk.Tk()
    ventana.title("Herramienta de Procesamiento de Servicios")
    ventana.geometry("550x250")
    ventana.resizable(False, False)

    logo = cargar_imagen()

    if logo:
        logo_label = tk.Label(ventana, image=logo)
        logo_label.place(x=225, y=186)

    tk.Label(ventana, text="Archivo de Servicios:").grid(row=1, column=0, padx=10, pady=5, sticky="E")
    entry_servicios = tk.Entry(ventana, width=50)
    entry_servicios.grid(row=1, column=1, padx=10, pady=5, sticky="W")
    tk.Button(ventana, text="Cargar", command=lambda: cargar_archivo(entry_servicios)).grid(row=1, column=2, padx=10, pady=5)

    tk.Label(ventana, text="Archivo de Tarifas:").grid(row=2, column=0, padx=10, pady=5, sticky="E")
    entry_tarifas = tk.Entry(ventana, width=50)
    entry_tarifas.grid(row=2, column=1, padx=10, pady=5, sticky="W")
    tk.Button(ventana, text="Cargar", command=lambda: cargar_archivo(entry_tarifas)).grid(row=2, column=2, padx=10, pady=5)

    tk.Label(ventana, text="Archivo de Operadores:").grid(row=3, column=0, padx=10, pady=5, sticky="E")
    entry_operadores = tk.Entry(ventana, width=50)
    entry_operadores.grid(row=3, column=1, padx=10, pady=5, sticky="W")
    tk.Button(ventana, text="Cargar", command=lambda: cargar_archivo(entry_operadores)).grid(row=3, column=2, padx=10, pady=5)

    label_status = tk.Label(ventana, text="", anchor="center")
    label_status.grid(row=5, column=0, columnspan=3, padx=10, pady=5, sticky="EW")

    tk.Button(ventana, text="Ejecutar", command=lambda: procesar_archivos(entry_servicios, entry_tarifas, entry_operadores, label_status, ventana)).grid(row=4, column=0, columnspan=3, padx=10, pady=10, sticky="EW")

    ventana.mainloop()