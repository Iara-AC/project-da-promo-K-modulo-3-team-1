Verificar los tipos de datos (**EDA**):

VERIFICACIÓN GENERALES:

-Hay 64 filas repetidas.


VERIFICACÓN COLUMNAS:

**age** - tiene un tipo de dato object. Por esto hemos verificado, y hay string junto con inters.

**attrition**  - CORRECTA. Es una string y solo tiene 'Yes' y 'No'

**businesstravel** - Substituir NaN por 'No data'

**dailyrate** - La hora del empleado que vende la empresa a un cliente
            Esta correcta porque es un inter, y tiene solo numeros. Pero podemos hacer un ROUND en los números. 

**department** - Substituir NaN por 'No data'   

**distancefromhome** - PREGUNTAR: como esta hecha la columna de distancia de casa hasta el trabajo? 
                    esta correcta, porque es un inter
                    HAY UN ERROR EN ESTOS DATOS. Pero hay que hacer comprobaciones
                    convertir estos números en absoluto

**education** - Esta CORRECTA.

**educationfield**  - Substituir NaN por 'No data'. PREGUNTAR: hay un dato 'others', podemos tratarlo como NAN?  

**employeecount** - un contador para cada tranajador. Esta CORRECTA.

**employeenumber** - Esta CORRECTA.

**environmentsatisfaction** - Hay números que no están en rango definido en la documentación. 
                            El rango difinido es de 1 al 4.Con valores que estan comprendidos entre el 1 y el 4, siendo el 4 el nivel de máxima satisfacción. 

**gender** - Esta correcta porque solo hay numeros. Pero quizás sería mejor para la visibilidad, cambiar a 'male' y 'female'.
            Donde 0 corresponde con "hombre" y 1 con "mujer". 
