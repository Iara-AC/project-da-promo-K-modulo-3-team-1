# Importaciones necesarias:

import pandas as pd
from datetime import datetime
import numpy as np
from src import soporte as sp
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
from scipy.stats import chi2_contingency, ttest_ind
import warnings
warnings.filterwarnings("ignore")

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


df.to_csv("data/df_modificado.csv")
print("CSV creado correctamente")
print("---------------------------------------------------------------------------")
print("PROYECTO DE VISUALIZACIÓN:")

#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#------------------------------ GRAFICOS------------------------------------
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------

# Lectura del csv modificado

df1 = pd.read_csv("data/df_modificado.csv", index_col = 0)

#---------------------------------------------------------------------------
print("DataFrame df_modificado.csv")
print(df1.head())

#---------------------------------------------------------------------------

# Estamos categorizando los satisfechos y no satisfechos en una nueva columna SatisfactionLevel. 
# Satisfechos serán los job satisfaction (3-4) y los Insatisfechos (1-2)

df1['SatisfactionLevel'] = np.where(df1['jobsatisfaction'] <= 2, 'No satisfecho', 'Satisfecho')

#---------------------------------------------------------------------------

# Porcentaje de nulos en cada columna.

porc_nulos = (df1.isnull().sum() / df1.shape[0]) * 100

# lo convertimos a DataFrame
df_nulos = pd.DataFrame(porc_nulos, columns = ["%_nulos"])
# filtramos el DataFrame para quedarnos solo con aquellas columnas que tengan nulos
df_nulos[df_nulos["%_nulos"] > 0]

#---------------------------------------------------------------------------

# Creamos una grafica con las columnas que tienen nulos.

columnas2 = ["salary", "percentsalaryhike", "worklifebalance", "distancefromhome", "dailyrate", "totalworkingyears", "yearssincelastpromotion", "monthlyincome"]

fig, axes = plt.subplots(nrows = 3, ncols = 3, figsize = (20,10)) 
axes = axes.flat
for indice, col in enumerate(columnas2):
    sns.boxplot(x = col, data = df1, ax = axes[indice])
    
plt.tight_layout();

#---------------------------------------------------------------------------

# La mediana de la columna salary.

mediana_salary = df1["salary"].median()

df1["salary"] = df1["salary"].fillna(mediana_salary)

print("---------------------------------------------------------------------------")
print("La mediana de la columna salary.")
print("---------------------------------------------------------------------------")
print(df1["salary"].describe()[["mean", "50%"]])
print("---------------------------------------------------------------------------")

#---------------------------------------------------------------------------

# La mediana de la columna monthlyincome.

mediana_monthlyincome = df1["monthlyincome"].median()

df1["monthlyincome"] = df1["monthlyincome"].fillna(mediana_monthlyincome)

print("La mediana de la columna monthlyincome")
print("---------------------------------------------------------------------------")
print(df1["monthlyincome"].describe()[["mean", "50%"]])
print("---------------------------------------------------------------------------")

#---------------------------------------------------------------------------

# La media de la columna worklifebalance.

media_worklifebalance = df1["worklifebalance"].mean()

df1["worklifebalance"] = df1["worklifebalance"].fillna(media_worklifebalance)

print("La media de la columna worklifebalance.")
print("---------------------------------------------------------------------------")
print(df1["worklifebalance"].describe()[["mean", "50%"]])
print("---------------------------------------------------------------------------")

#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#---------------------df-Satisfecho / df-No Satisfecho----------------------
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------

# Separacion del DataFrame en: job_satisfecha y job_no_satisfecha.

job_satisfecha = df1[df1['jobsatisfaction'].isin([3,4])]
job_no_satisfecha = df1[df1['jobsatisfaction'].isin([1,2])]

#---------------------------------------------------------------------------

# Visualización del df job_satisfecha = (3-4).
print("Visualización del DataFrame: job_satisfecha.")
print("---------------------------------------------------------------------------")
print(job_satisfecha.head())

#---------------------------------------------------------------------------

# Visualización del df job_no_satisfecha = (1-2).

print("Visualización del DataFrame: job_no_satisfecha.")
print("---------------------------------------------------------------------------")
print(job_no_satisfecha.head())

#---------------------------------------------------------------------------

#TASA ROTACION TOTAL
df1["attrition"].value_counts()

# Valores definidos
empleados_inicio = 1678  # Número de empleados al inicio del período
empleados_fin = 1406      # Número de empleados al final del período
empleados_salieron = 272 # Número de empleados que salieron durante el período

# Calcular y mostrar la tasa de rotación
tasa_rotacion = sp.calcular_tasa_rotacion(empleados_inicio, empleados_fin, empleados_salieron)
print(f"La tasa de rotación total es: {tasa_rotacion}%")
print("---------------------------------------------------------------------------")

#---------------------------------------------------------------------------

#TASA ROTACION SATISFECHOS 
job_satisfecha["attrition"].value_counts()

# Valores definidos
empleados_inicio = 1035  # Número de empleados al inicio del período
empleados_fin = 890      # Número de empleados al final del período
empleados_salieron = 145 # Número de empleados que salieron durante el período

# Calcular y mostrar la tasa de rotación
tasa_rotacion = sp.calcular_tasa_rotacion(empleados_inicio, empleados_fin, empleados_salieron)
print(f"La tasa de rotación de las personas satisfechas es: {tasa_rotacion}%")
print("---------------------------------------------------------------------------")

#---------------------------------------------------------------------------

#TASA ROTACION INSATISFECHOS
job_no_satisfecha["attrition"].value_counts()

# Valores definidos
empleados_inicio = 643  # Número de empleados al inicio del período
empleados_fin = 516      # Número de empleados al final del período
empleados_salieron = 127 # Número de empleados que salieron durante el período

# Calcular y mostrar la tasa de rotación
tasa_rotacion = sp.calcular_tasa_rotacion(empleados_inicio, empleados_fin, empleados_salieron)
print(f"La tasa de rotaciónde las personas insatisfechas es: {tasa_rotacion}%")
print("---------------------------------------------------------------------------")

#---------------------------------------------------------------------------

# COUNT TOTAL DE PERSONAS POR JOBROLE
df1["jobrole"].value_counts()

#---------------------------------------------------------------------------

# % POR JOB ROLE DE SATISFACCIÓN

# Calcular el conteo de cada valor en la columna 'jobrole'
x = job_satisfecha["jobrole"].value_counts()

# Calcular el porcentaje con respecto al total de empleados (1035 en este caso)
porcentajes = (x / 1035) * 100

# Mostrar los porcentajes
print("PORCENTAJES DE SATISFACCIÓN DE LA COLUMNA: Jobrole")
print("---------------------------------------------------------------------------")
print(porcentajes)# Calcular el conteo de cada valor en la columna 'jobrole'

#---------------------------------------------------------------------------

# % POR JOB ROLE DE INSATISFACCIÓN

# Calcular el conteo de cada valor en la columna 'jobrole'
x = job_no_satisfecha["jobrole"].value_counts()

# Calcular el porcentaje con respecto al total de empleados (1035 en este caso)
porcentajes = (x / 643) * 100

# Mostrar los porcentajes
print("---------------------------------------------------------------------------")
print("PORCENTAJES DE INSATISFACCIÓN DE LA COLUMNA: Jobrole")
print("---------------------------------------------------------------------------")
print(porcentajes)

#---------------------------------------------------------------------------

# Calcular el conteo de cada valor en la columna 'jobrole'
x = job_satisfecha["jobrole"].value_counts()

# Calcular el porcentaje con respecto al total de empleados (643 en este caso)
porcentajes = (x / 643) * 100

# Crear el gráfico de barras
plt.figure(figsize=(10,6))
porcentajes.plot(kind='bar', color='skyblue')

# Añadir etiquetas y título
plt.title('Porcentaje de empleados satisfechos en Job Role', fontsize=14)
plt.xlabel('Job Role', fontsize=12)
plt.ylabel('Porcentaje de empleados', fontsize=12)

# Mostrar los valores en las barras
for i in range(len(porcentajes)):
    plt.text(i, porcentajes[i] + 1, f'{porcentajes[i]:.2f}%', ha='center', fontsize=10)

# Mostrar el gráfico
plt.tight_layout()
plt.show()

#---------------------------------------------------------------------------

# Calcular el conteo de cada valor en la columna 'jobrole'
y = job_no_satisfecha["jobrole"].value_counts()

# Calcular el porcentaje con respecto al total de empleados (643 en este caso)
porcentajes = (y / 643) * 100

# Crear el gráfico de barras
plt.figure(figsize=(10,6))
porcentajes.plot(kind='bar', color='skyblue')

# Añadir etiquetas y título
plt.title('Porcentaje de empleados satisfechos en Job Role', fontsize=14)
plt.xlabel('Job Role', fontsize=12)
plt.ylabel('Porcentaje de empleados', fontsize=12)

# Mostrar los valores en las barras
for i in range(len(porcentajes)):
    plt.text(i, porcentajes[i] + 1, f'{porcentajes[i]:.2f}%', ha='center', fontsize=10)

# Mostrar el gráfico
plt.tight_layout()
plt.show()

#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#---A/B TESTING - PARA RELACION ENTRE SATISFACCIÓN Y ABANDONAR LA EMPRESA---
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------

print("---------------------------------------------------------------------------")
print("Gente satisfecha e insatisfecha que se ha ido de la empresa:")
cross_tab_satisf =  pd.crosstab(df1['SatisfactionLevel'], df1["attrition"])
print(cross_tab_satisf)
print("---------------------------------------------------------------------------")

#---------------------------------------------------------------------------

# Test de Chi-cuadrado 

print("Test de Chi-cuadrado:")
chi2, p, dof, expected = chi2_contingency(cross_tab_satisf)
print(f"Chi2: {chi2}, p-valor: {p}, Grados de libertad: {dof}")
print("---------------------------------------------------------------------------")

#---------------------------------------------------------------------------

# Interpretar resultado

print("Interpretación de resultados:")
if p < 0.05:
     print("Rechazamos la hipótesis nula: Hay una relación significativa entre satisfacción laboral y attrition.") 
else:
     print("No podemos rechazar la hipótesis nula: No hay relación significativa.")
print("---------------------------------------------------------------------------")

#---------------------------------------------------------------------------

empleados_rotacion = df1[df1['attrition'] == "Yes"]

empleados_rotacion['Costo_Rotacion'] = empleados_rotacion.apply(sp.calcular_costo_empleado, axis=1)

# Sumar el costo total de rotación
costo_total_rotacion = empleados_rotacion['Costo_Rotacion'].sum()

# Resultados
print(f"Costo total de rotación: ${costo_total_rotacion:,.2f}")
print("---------------------------------------------------------------------------")

# Opcional: Ver costos por departamento
costo_por_departamento = empleados_rotacion.groupby('department')['Costo_Rotacion'].sum()
print("\nCosto total por departamento:")
print(costo_por_departamento)
print("---------------------------------------------------------------------------")

#---------------------------------------------------------------------------

print("""Calculo de lo que costaria el reemplazo de cada empleado.
Por lo que vemos para la empresa que significa en terminos economicos que haya una alta rotación y posteriormente tengamos que sustituir a los empleados 
que significa en terminos economicos.""")
print("---------------------------------------------------------------------------")


# Aplicar la función a los empleados con rotación

empleados_rotacion = df1[df1['attrition'] == "Yes"]

empleados_rotacion['Costo_Rotacion'] = empleados_rotacion.apply(sp.calcular_costo_empleado, axis=1)

# Sumar el costo total de rotación
costo_total_rotacion = empleados_rotacion['Costo_Rotacion'].sum()

# Resultados
print(f"Costo total de rotación: ${costo_total_rotacion:,.2f}")
print("---------------------------------------------------------------------------")

# Opcional: Ver costos por departamento
costo_por_departamento = empleados_rotacion.groupby('department')['Costo_Rotacion'].sum()
print("\nCosto total por departamento:")
print(costo_por_departamento)
print("---------------------------------------------------------------------------")

#---------------------------------------------------------------------------


rotacion_nivel = sp.calcular_rotacion_nivel(bajas_nivel=3, empleados_inicio=20, empleados_fin=18)
print(f"Tasa de rotación por nivel jerárquico: {rotacion_nivel:.2f}%")
print("---------------------------------------------------------------------------")

#---------------------------------------------------------------------------
print("Hipotesis Economicas:")
print("---------------------------------------------------------------------------")
print("""Hipotesis 1, la gente que  esta  satisfecha cobra mas que la gente insatisfecha.
Para contrastar esta hipotesis hemos hecho la media a ambas poblaciones y hemos descubierto 
que la gente no-satisfecha cobra más por lo que nuestra hipotesis es nula.
De esto podemos deducir que el monthly income a prioory no es tan determinante enla satisfacción.""")
print("---------------------------------------------------------------------------")

print("La media de job_satisfecha sobre monthlyincome:")
print(job_satisfecha["monthlyincome"].mean())
print("---------------------------------------------------------------------------")

print("La media de job_no_satisfecha sobre monthlyincome:")
print(job_no_satisfecha["monthlyincome"].mean())
print("---------------------------------------------------------------------------")

#---------------------------------------------------------------------------

print("""Hipótesis 2. La gente satisfecha tiene mas incremento salarial percentual anual que
la insatisfecha. Para ello hemos hecho la media de ambas. La hipótesis es nula. Esto vuelve 
a confirmar que la satisfacción no tiene una fuerte relación con el salario.""")
print("---------------------------------------------------------------------------")

print("La media de job_satisfecha sobre percentsalaryhike:")
print(job_satisfecha["percentsalaryhike"].mean())
print("---------------------------------------------------------------------------")

print("La media de job_no_satisfecha sobre percentsalaryhike:")
print(job_no_satisfecha["percentsalaryhike"].mean())
print("---------------------------------------------------------------------------")

#---------------------------------------------------------------------------

print("""Hipotesis 3: La opción de compra de acciones es relevante para la satisfacción del empleado.
Hemos descubierto haciendo las medias que no es así.""")
print("---------------------------------------------------------------------------")

print("La media de job_satisfecha sobre stockoptionlevel:")
print(job_satisfecha["stockoptionlevel"].mean())
print("---------------------------------------------------------------------------")

print("La media de job_no_satisfecha sobre stockoptionlevel:")
print(job_no_satisfecha["stockoptionlevel"].mean())
print("---------------------------------------------------------------------------")

#---------------------------------------------------------------------------

print("""*Reflexión motivos económicos.*
Hemos contrastado tres hipótesis respecto a datos económicos de los empleados respecto a la satisfacción.
Las tres variables contrastadas han sido ingresos mensuales, incremento salarial anual y opción de compra de acciones. 
En las tres ha sucedido que hemos contrastado que no tiene relación con la satisfacción laboral, por lo que descartamos 
avanzar en esta linea de investigación.""")

#---------------------------------------------------------------------------
print("---------------------------------------------------------------------------")
print("---------------------------------------------------------------------------")
print("Hipotesis de Movilidad:")
print("---------------------------------------------------------------------------")

print("Hipotesis1: La gente que vive mas lejos del trabajo esta mas insatisfecha")
print("---------------------------------------------------------------------------")

print("La media de job_satisfecha sobre distancefromhome:")
print(job_satisfecha["distancefromhome"].mean())
print("---------------------------------------------------------------------------")

print("La media de job_no_satisfecha sobre distancefromhome:")
print(job_no_satisfecha["distancefromhome"].mean())
print("---------------------------------------------------------------------------")

#---------------------------------------------------------------------------
print("""Test hipotesis(prueba hipotesis)
H0 --> No hay diferencia en satisfaccion del empleado por los viajes que hace.
H1 --> La gente satisfecha viaja mas.""")
print("---------------------------------------------------------------------------")

print("Hipotesis2: Le gente que viaja más esta mas satisfife de la gente que viaja menos. No es significativo.")
print("---------------------------------------------------------------------------")

print("La caidad de gente de job_satisfecha que viaja de la columna businesstravel:")
print(job_satisfecha["businesstravel"].value_counts())
print("---------------------------------------------------------------------------")

print("La caidad de gente de job_no_satisfecha que viaja de la columna businesstravel:")
print(job_no_satisfecha["businesstravel"].value_counts())
print("---------------------------------------------------------------------------")

#---------------------------------------------------------------------------

# Estamos haciendo una separacion, dejando solo la columna businesstravel.

job_satisfecha = df1[df1['jobsatisfaction'].isin([3,4])]["businesstravel"]
job_no_satisfecha = df1[df1['jobsatisfaction'].isin([1,2])]["businesstravel"]

print("Creacion del Cross_Table:")
cross_table_satisfaccion =  pd.crosstab(df1["SatisfactionLevel"], df1["businesstravel"])
print(cross_table_satisfaccion)
print("---------------------------------------------------------------------------")

#---------------------------------------------------------------------------

# Test de Chi-cuadrado 

print("Test de Chi-cuadrado:")
chi2, p, dof, expected = chi2_contingency(cross_table_satisfaccion)
print(f"Chi2: {chi2}, p-valor: {p}, Grados de libertad: {dof}")
print("---------------------------------------------------------------------------")

print("Interpretación de los resultados:")
if p < 0.05:
     print("Rechazamos la hipótesis nula: Hay una relación significativa entre Satisfacción laboral  y tener que hacer viajes.") 
else:
     print("No podemos rechazar la hipótesis nula: No hay relación significativa.")

print("---------------------------------------------------------------------------")

print("""*Reflexión motivos de movilidad.*
En este test de hipótesis no podemos rechazar el H0. por esto la satisfacción laboral es independiente de los viajes que hace el empleado.
Conclusión : Añadir una columna para hacer cuestionario a empleados para preguntar si les gusta o no viajar.(en una escala del 1-4""")

print("---------------------------------------------------------------------------")

# Estamos haciendo una separacion, dejando solo la columna businesstravel.

print("Creacion del Cross_Table:")
cross_table_satisfaccion1 =  pd.crosstab(df1['SatisfactionLevel'], df1["remotework"])
print(cross_table_satisfaccion1)
print("---------------------------------------------------------------------------")

#---------------------------------------------------------------------------

print("""H₀: "La satisfacción laboral  es independiente del teletrabajo."
H₁: "La satisfacción laboral depende del teletrabajo." """)
print("---------------------------------------------------------------------------")

# Test de Chi-cuadrado
print("Test de Chi-cuadrado:") 
chi2, p, dof, expected = chi2_contingency(cross_table_satisfaccion1)
print(f"Chi2: {chi2}, p-valor: {p}, Grados de libertad: {dof}")
print("---------------------------------------------------------------------------")
# Interpretar resultado
print("Interpretación de los resultados:")
if p < 0.05:
     print("Rechazamos la hipótesis nula: Hay una relación significativa.") 
else:
     print("No podemos rechazar la hipótesis nula: No hay relación significativa entre satisfacción labora y teletrabajo.")
print("---------------------------------------------------------------------------")
      
#---------------------------------------------------------------------------

print("Hipotesis de Movilidad:")
print("---------------------------------------------------------------------------")

print("""H₀: "La satisfacción laboral es independiente de la distancia al trabajo."
H₁: "La satisfacción laboral depende de la distancia al trabajo." """)

medianadistancefromhome = df1["distancefromhome"].median()
print("La mediana de distancefromhome:")
print("medianadistancefromhome")
#---------------------------------------------------------------------------



