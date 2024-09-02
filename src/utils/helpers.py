"""
helpers.py

Este módulo contiene funciones de ayuda o utilidades que pueden ser reutilizadas en la aplicación.
"""

import os
from tkinter import messagebox

def verificar_ruta(filepath):
    """
    Verifica si una ruta de archivo existe.

    Args:
        filepath (str): Ruta del archivo.

    Returns:
        bool: True si la ruta existe, False en caso contrario.
    """
    return os.path.exists(filepath)

def mostrar_mensaje(tipo, titulo, mensaje):
    """
    Muestra un mensaje emergente de tipo `info`, `warning`, o `error`.

    Args:
        tipo (str): Tipo de mensaje ('info', 'warning', 'error').
        titulo (str): Título del mensaje.
        mensaje (str): Contenido del mensaje.
    """
    if tipo == 'info':
        messagebox.showinfo(titulo, mensaje)
    elif tipo == 'warning':
        messagebox.showwarning(titulo, mensaje)
    elif tipo == 'error':
        messagebox.showerror(titulo, mensaje)
    else:
        raise ValueError(f"Tipo de mensaje no soportado: {tipo}")
