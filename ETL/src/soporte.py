# Importaciones necesarias:

import numpy as np
import pandas as pd

#-------------------------------------------------------------------------------------------------------------------------

# Transformación de los NAN

def transformar_nan_sql(df, columna=None, valor_reemplazo='Desconocido'):
    """
    Reemplaza los valores NaN en una columna específica o en todas las columnas 
    de un DataFrame con un valor compatible con SQL.

    Parámetros:
    - df (pd.DataFrame): El DataFrame en el que se reemplazarán los NaN.
    - columna (str, opcional): El nombre de la columna donde se reemplazarán los NaN. 
                               Si es None, reemplazará en todas las columnas.
    - valor_reemplazo: El valor con el que se reemplazarán los NaN. Ejemplo: 'NULL', '', 0.

    Retorna:
    - pd.DataFrame: El DataFrame con los NaN reemplazados.
    """
    if columna:
        # Si se especifica una columna, verifica que exista
        if columna not in df.columns:
            raise ValueError(f"La columna '{columna}' no existe en el DataFrame.")
        # Reemplaza los NaN en la columna específica
        df[columna] = df[columna].replace({np.nan: valor_reemplazo})
    else:
        print("Te falta añadir la columna")
    
    return df

#-----------------------------------------------------------------------------------------------------------------------------

# Conversión de números a numeros absolutos

def convertir_a_absoluto(numero):
    """
    Convierte un número a su valor absoluto.

    Parámetros:
    numero (int | float): Número a convertir.

    Retorno:
    int | float: Valor absoluto del número.
    """
    return abs(numero)

#-----------------------------------------------------------------------------------------------------------------------------

# Funcion que cambia las comas por puntos y elimina símbolos como '$'

def cambiar_coma_punto(columna):
    """
    Cambia las comas por puntos y elimina símbolos como '$' en los valores de una columna.
    Parámetros:
        columna (str): Cadena de texto a modificar.
    Retorna:
        float: Número transformado, o np.nan si ocurre un error.
    """
    #if isinstance(columna, (int, float)):
            #return columna
    try:
        # Reemplazar comas por puntos y eliminar el símbolo '$'
        return float(columna.replace(',', '.').replace('$', ''))
    except:
        # Si hay un error (como valores no numéricos), devolver NaN
        return np.nan

#-----------------------------------------------------------------------------------------------------------------------------

# Quedarse con el Primer Dígito de un Número de Dos Dígitos:

def primer_digito(df, column):
    df[column] = df[column].astype(str).str[0].astype(int)
    return df

#-----------------------------------------------------------------------------------------------------------------------------

def convertir_valores(valor):
    """
    Convierte los valores: 0 a 'yes', 1 a 'no', y deja el resto sin cambios
    Parámetros:
        valor: Valor a transformar (puede ser numérico o texto).
    Retorna:
        string: Valor transformado, o np.nan si ocurre un error.
    """
    try:
        valor_str = str(valor).strip()  # Convertir a cadena y eliminar espacios en blanco
        if valor_str == "0":  # Comparar como cadena
            return 'm'.title()
        elif valor_str == "1":  # Comparar como cadena
            return 'f'.title()
        else:
        
            return valor  # Si no es '0' ni '1', dejar el valor sin cambios
    except Exception as e:
        print(f"Error al procesar el valor {valor}: {e}")
        return np.nan  # Manejar errores con np.nan
    
#-------------------------------------------------------------------------------------------------------------------------

# Funcion para corregir minusculas.

def corregir_y_minusculas(df, columna):
    # Verifica si la columna existe en el DataFrame
    if columna in df.columns:
        # Itera sobre las filas y corrige los valores
        corrected_values = []
        for value in df[columna]:
            if pd.notnull(value):  # Si el valor no es nulo
                corrected_values.append(str(value).strip().lower())  # Corrige y convierte a minúsculas
            else:
                corrected_values.append(value)  # Deja los valores nulos como están
        # Asigna los valores corregidos a la columna
        df[columna] = corrected_values
    else:
        raise ValueError(f"La columna {columna} no existe en el DataFrame.")
    return df

#-------------------------------------------------------------------------------------------------------------------------

# Funcion que redondea los valores de una columna

def cambio_round(df, columna, decimales=0):
    """
    Redondea los valores de una columna específica de un DataFrame.

    Parámetros:
    df : DataFrame
        El DataFrame que contiene los datos.
    columna : str
        El nombre de la columna a redondear.
    decimales : int, opcional
        El número de decimales a redondear (por defecto es 0).
    
    Retorna:
    df : DataFrame
        El DataFrame con la columna redondeada.
    """
    if columna in df.columns:
        # Intentamos convertir todos los valores a numéricos, forzando errores a NaN
        df[columna] = pd.to_numeric(df[columna], errors='coerce')

        # Redondeamos solo los valores numéricos
        df[columna] = df[columna].round(decimales)
    else:
        raise ValueError(f"La columna '{columna}' no existe en el DataFrame.")
    
    return df

#-------------------------------------------------------------------------------------------------------------------------

# Función que convierte los valores: 0 a 'yes', 1 a 'no', y deja el resto sin cambios.

def convertir_valores(valor):
    """
    Convierte los valores: 0 a 'yes', 1 a 'no', y deja el resto sin cambios
    Parámetros:
        valor: Valor a transformar (puede ser numérico o texto).
    Retorna:
        string: Valor transformado, o np.nan si ocurre un error.
    """
    try:
        valor_str = str(valor).strip()  # Convertir a cadena y eliminar espacios en blanco
        if valor_str == "0":  # Comparar como cadena
            return 'true'.title()
        elif valor_str == "1":  # Comparar como cadena
            return 'false'.title()
        elif valor_str == "Yes":
            return 'true'.title()
        else:
            return valor  # Si no es '0' ni '1', dejar el valor sin cambios
    except Exception as e:
        print(f"Error al procesar el valor {valor}: {e}")
        return np.nan  # Manejar errores con np.nan
    
    #-------------------------------------------------------------------------------------------------------------------------

    
