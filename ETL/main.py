# Importaciones necesarias:

import pandas as pd
from datetime import datetime
import numpy as np
from src import soporte as sp

#-------------------------------------------------------------------------------------------------------------------------

# Lectura del .csv

df = pd.read_csv("data/hr_raw_data_final.csv", index_col = 0)

#-------------------------------------------------------------------------------------------------------------------------

# Reemplazar los NaN en una columna específica

sp.transformar_nan_sql(df, columna="educationfield")
sp.transformar_nan_sql(df, columna="department")
sp.transformar_nan_sql(df, columna="maritalstatus")
sp.transformar_nan_sql(df, columna="overtime")
sp.transformar_nan_sql(df, columna="roledepartament")

#---------------------------------------------------------------------------

# Conversión de números a numeros absolutos

df["distancefromhome"] = df["distancefromhome"].apply(sp.convertir_a_absoluto)

#---------------------------------------------------------------------------

#Cambia las comas por puntos y elimina símbolos como '$'

columnas = ["totalworkingyears", "worklifebalance", "yearsincurrentrole", "monthlyincome", "monthlyrate", "sameasmonthlyincome", "salary","performancerating"]


for col in columnas:
    if col in df.columns:
        df[col] = df[col].apply(sp.cambiar_coma_punto)

#---------------------------------------------------------------------------

# Quedarse con el Primer Dígito de un Número de Dos Dígitos:

sp.primer_digito(df, 'environmentsatisfaction')

#---------------------------------------------------------------------------

# Convierte los valores: 0 a 'yes', 1 a 'no'

df["gender"] = df["gender"].apply(sp.convertir_valores)

#---------------------------------------------------------------------------

# Funcion para corregir minusculas.

x = ["jobrole", "roledepartament", "educationfield","department","maritalstatus","standardhours",]

for columna in x:
    sp.corregir_y_minusculas(df, columna)

#---------------------------------------------------------------------------

# Etamos calculando la tarifa por hora del empleado.

df["hourlyrate"] = df["dailyrate"] / 8

#---------------------------------------------------------------------------

# Función que redondea los valores de una columna.

columnas_a_redondear = ["dailyrate", "hourlyrate"]

for col in columnas_a_redondear:
    df = sp.cambio_round(df, col, decimales=1)

#---------------------------------------------------------------------------

# Convierte los valores: 0 a 'yes', 1 a 'no', y deja el resto sin cambios

df["remotework"] = df["remotework"].apply(sp.convertir_valores)

#---------------------------------------------------------------------------

# Autocompletamos la columna "Age" calculando ç.

current_year = datetime.now().year
df['age'] = current_year - df['datebirth']

#---------------------------------------------------------------------------

# Iguala NAN a Non-travel en la columna "businesstravel"

df['businesstravel'] = df['businesstravel'].replace(np.nan, 'non-travel') 

#---------------------------------------------------------------------------

# Iguala NAN  a full-time

df["standardhours"] = df["standardhours"].fillna("full time")

#---------------------------------------------------------------------------

# Eliminación de columnas 

df = df.drop(columns="over18")
df = df.drop(columns="numberchildren")
df = df.drop(columns="yearsincurrentrole") 

#---------------------------------------------------------------------------

print("Todo a salido segun lo previsto - Linea 112")
df.to_csv("data/df_modificado.csv")
print("CSV creado correctamente")

#---------------------------------------------------------------------------

# Lectura del csv modificado

df1 = pd.read_csv("data/df_modificado.csv", index_col = 0)

#---------------------------------------------------------------------------

# 

df['SatisfactionLevel'] = np.where(df['jobsatisfaction'] <= 2, 'No satisfecho', 'Satisfecho')