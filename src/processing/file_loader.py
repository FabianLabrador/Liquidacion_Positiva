"""
file_loader.py

Este módulo contiene funciones para cargar archivos de datos necesarios para el procesamiento.
"""

import pandas as pd
from tkinter import messagebox

def cargar_archivo(filepath):
    """
    Carga un archivo Excel desde la ruta proporcionada.
    
    Args:
        filepath (str): Ruta del archivo Excel.
    
    Returns:
        pd.DataFrame: DataFrame de pandas con los datos cargados.
    """
    try:
        df = pd.read_excel(filepath)
        return df
    except Exception as e:
        messagebox.showerror("Error", f"Error al cargar el archivo {filepath}: {e}")
        return None
