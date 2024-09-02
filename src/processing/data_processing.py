"""
data_processing.py

Este módulo contiene funciones para procesar los datos cargados.
"""

import pandas as pd

def procesar_datos(servicios_df, tarifas_df, operadores_df):
    """
    Procesa los datos de servicios, tarifas y operadores para identificar traslados vacíos.
    
    Args:
        servicios_df (pd.DataFrame): DataFrame con los datos de servicios.
        tarifas_df (pd.DataFrame): DataFrame con los datos de tarifas.
        operadores_df (pd.DataFrame): DataFrame con los datos de operadores.
    
    Returns:
        pd.DataFrame: DataFrame procesado con la información combinada y los traslados vacíos identificados.
    """
    # Lógica para procesar los datos e identificar traslados vacíos
    # Ejemplo de procesamiento:
    # 1. Comparar ubicaciones iniciales y finales para detectar traslados vacíos.
    # 2. Usar las tarifas y operadores para calcular costos y otras métricas.

    # Aquí puedes incluir tu lógica personalizada.
    # Ejemplo simplificado:

    # Fusionar operadores_df con servicios_df para añadir ubicaciones iniciales
    servicios_df = servicios_df.merge(operadores_df, on="Nombre_Contratista", how="left")

    # Realizar el procesamiento para identificar traslados vacíos
    # Ejemplo:
    servicios_df['Traslado_Vacío'] = servicios_df.apply(lambda row: 'Sí' if row['Ubicacion_Inicial'] != row['Ubicacion_Final'] else 'No', axis=1)

    # Manejar los casos donde la tarifa no se encuentra
    servicios_df['Tarifa'] = servicios_df.apply(lambda row: 'Buscar tarifa' if row['Tarifa'] is None else row['Tarifa'], axis=1)

    return servicios_df

def guardar_resultados(df, output_path):
    """
    Guarda los resultados procesados en un archivo Excel.
    
    Args:
        df (pd.DataFrame): DataFrame con los resultados procesados.
        output_path (str): Ruta del archivo Excel donde se guardarán los resultados.
    """
    try:
        df.to_excel(output_path, index=False)
    except Exception as e:
        print(f"Error al guardar los resultados: {e}")