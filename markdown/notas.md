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

**employeecount** - un contador para cada trabajador. Esta CORRECTA.

**employeenumber** - Esta CORRECTA.

**environmentsatisfaction** - Hay números que no están en rango definido en la documentación. 
                            El rango difinido es de 1 al 4.Con valores que estan comprendidos entre el 1 y el 4, siendo el 4 el nivel de máxima satisfacción. 

**gender** - Esta CORRECTA porque solo hay numeros. Pero quizás sería mejor para la visibilidad, cambiar a 'male' y 'female'.
            Donde 0 corresponde con "hombre" y 1 con "mujer". 

**hourlyrate** - Sustituir NaN por 'No data'. Dejarlo en 2 decimales.

**jobinvolvement** - Es una escala del 1 al 4. Esta CORRECTA.DUDA: No sabemos qué es 1 y qué es 4. Imagino que lo podremos saber al relacionarlo con otras columnas. 

**joblevel** - Es una escala del 1 al 5. Esta CORRECTA.DUDA: No sabemos qué es 1 y qué es 4. Imagino que lo podremos saber al relacionarlo con otras columnas. 

**jobsatisfaction** - Es una escala del 1 al 4. Esta CORRECTA.DUDA: No sabemos qué es 1 y qué es 4. Imagino que lo podremos saber al relacionarlo con otras columnas. 

**numcompaniesworked** - Escala del 0 al 7. Esta CORRECTA: o sabemos qué es 0 y qué es 7. Imagino que lo podremos saber al relacionarlo con otras columnas. 

**over18** - Sustituir NaN por 'No data'

**overtime** - Sustituir NaN por 'No data'

**percentsalaryhike** - Esta CORRECTA.

**performancerating** - Sustituir NaN por 'No data'. Solo hay 3 o 4. No sabemos que es 3 y que es 4. La separación de decimales es una coma, creo que es importante que sea un punto.Preguntar a Cesar

**relationshipsatisfaction** - Es una escala del 1 al 4. Esta CORRECTA.DUDA: No sabemos qué es 1 y qué es 4. Imagino que lo podremos saber al relacionarlo con otras columnas. 

**standardhours** - Sustituir NaN por 'No data'

**stockoptionlevel** - Escala de 0 a 3.

**totalworkingyears** - Sustituir NaN por 'No data'. DUDA: La separación de decimales es una coma, creo que es importante que sea un punto. Preguntar a Cesar

**trainingtimeslastyear** - Escala de 0 a 6. 

**worklifebalance** - Sustituir NaN por 'No data'. La separación de decimales es una coma, creo que es importante que sea un punto.Preguntar a Cesar.

**yearsatcompany** - Esta CORRECTA

**yearsincurrentrole** - Escala de 0 a 13. Sustituir NaN por 'No data'.La separación de decimales es una coma, Creo que deberia ser un INT este dato porque son años¿?¿?. Preguntar a Cesar.

**yearssincelastpromotion** - Esta CORRECTA

**yearswithcurrmanager** - Esta CORRECTA

**sameasmonthlyincome** - Sustituir NaN por 'No data'. La separación de decimales es una coma, creo que es importante que sea un punto.Preguntar a Cesar.

**datebirth** - Esta CORRECTA

**salary** - Sustituir NaN por 'No data'. La separación de decimales es una coma, creo que es importante que sea un punto.Preguntar a Cesar.

**roledepartament** - Sustituir NaN por 'No data'. Hay cosas escritas mix de mayusculas y minusculas(ManaGER). ¿Hay que homogeneizar esto en min o may? El que esten diferentes escrito hace que coja como unicos cosas que son lo mismo. Pongo ejemplo aqui
' ManaGER  -  Research & Development ',
' MANAger  -  Research & Development ',
' mANaGer  -  Research & Development '

Habría que homogeneizar esto para que de verdad tengamos los diferentes. 

**numberchildren** - Todos son nan. No parece util. 

**remotework** - Hay 4 datos. 'Yes', '1', 'False', '0', 'True'. Hay que homogeneizar en yes/no o en 1/0. 