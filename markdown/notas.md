Verificar los tipos de datos (**EDA**):

VERIFICACIÓN GENERALES:

-Hay 64 filas repetidas. Hemos averiguado estos datos, y concluimos que son exactamente los mismo datos y por esto podemos borrar. 
-PODEMOS BORRAR ESTAS 64 filas repetidas!!!!

VERIFICACÓN COLUMNAS:

**age** - tiene un tipo de dato object. Por esto hemos verificado, y hay string junto con inters.
Cambiar a esta columna INTER.

**attrition**  - CORRECTA. Es una string y solo tiene 'Yes' y 'No'.

**businesstravel** - La gente que no viaja también es un dato nulo, porque antes la empresa dejaba el campo vacio. 
Así que aqui podemos poner todos los NaN como 'non-travel'.

**dailyrate** - La hora del empleado que vende la empresa a un cliente.
            Esta correcta porque es un inter, y tiene solo numeros. 
           Podemos hacer un ROUND en los números. 

**department** - Substituir NaN por 'No data'
PREGUNTA: que significa el NaN en esta columna??  
NaN - NO hay este dato 

Gestionar los nulos: Poner como 'Unknow'

**distancefromhome** esta correcta, porque es un inter
                    HAY UN ERROR EN ESTOS DATOS: Pero hay que hacer comprobaciones
                    convertir estos números en absoluto.

**education** - Esta CORRECTA.

**educationfield**  - Substituir NaN por 'No data'.
CAMBIAR el tipo de dato a string.

Gestionar los nulos: Poner como 'Unknow'

**employeecount** - un contador para cada trabajador. Esta CORRECTA.

**employeenumber** - Esta CORRECTA.

**environmentsatisfaction** - Hay números que no están en rango definido en la documentación. 
                            El rango difinido es de 1 al 4.Con valores que estan comprendidos entre el 1 y el 4, siendo el 4 el nivel de máxima satisfacción. 
han querido poner en decimales y no ha podido.
Arreglar estos datos. Hay que poner una coma en lo medio de los numeros con 2 campos. 

**gender** - Esta CORRECTA porque solo hay numeros. Pero quizás sería mejor para la visibilidad, cambiar a 'male' y 'female'.
            Donde 0 corresponde con "hombre" y 1 con "mujer". 

**hourlyrate** - Dejarlo en 2 decimales.

**jobinvolvement** - CORRECTA. Es una escala del 1 al 4. 

**joblevel** - Es una escala del 1 al 5. Esta CORRECTA.


**jobsatisfaction** - Es una escala del 1 al 4. Esta CORRECTA.

**maritalstatus** - Hay errores en la sintaxis de palabras. 
HAY que poner igual las palabras. 
single
married
divorced
Los NaN podemos poder 'no data' ya que la columna es una string

**monthlyincome** - HAY que transformar esta columna en INTER. 
MIrar los vacios, que significa los NaNs???


**monthlyrate** Cambiar esta columna a INTER


**numcompaniesworked** - Escala del 0 al 7. Esta CORRECTA

**over18** - PREGUNTAR: Que significa este NaN? Porque hay muchos, hay más NaN que Y.
No es posible que sean todos NaN = N.
Podemos sacar esta info desde la columna edad o del año de nascimiento. 
Pero es relevante esta columna??? 

**overtime** - Hay alguna columna que podemos relacionar con esta? 
NaN es que no hay los datos

**percentsalaryhike** - Esta CORRECTA.

**performancerating** - Solo hay 3 o 4. No sabemos que es 3 y que es 4. La separación de decimales es una coma, creo que es importante que sea un punto.(CAMBIAR LA COMA POR EL PUNTO)
 Escala de esta columna es de 0 a 4. 

**relationshipsatisfaction** - Es una escala del 1 al 4. Esta CORRECTA. 

**standardhours** - Sustituir NaN por 'No data'. CAMBIAR el tipo de DATO a object.
NaN es igual que FULL TIME.
ARREGLAR ESTOS DATOS

**stockoptionlevel** - Escala de 0 a 3. CORECTA.
Relacionar esta columna con la de total de años trabajado. Y ver si hay alguna relación positiva.

**totalworkingyears** -(CAMBIAR LA COMA POR EL PUNTO) 
NaN = no hay el dato

**trainingtimeslastyear** - Escala de 0 a 6. Veces que ha hecho un surco
CORRECTA

**worklifebalance** - (CAMBIAR LA COMA POR EL PUNTO)
CAMBIAR el tipo de dato
NaN = no hay el dato

**yearsatcompany** - Esta CORRECTA
Relacionar con el número de empresas que la persona ha estado en su vida. Y también relacionar con el total de años trabajado en toda su vida, para así poder tener una idea del nivel de satisfacion. 

**yearsincurrentrole** - La separación de decimales es una coma,
CAMBIAR el tipo de dato a un INT 

**yearssincelastpromotion** - Esta CORRECTA

**yearswithcurrmanager** - Esta CORRECTA

**sameasmonthlyincome** - La separación de decimales es una coma, creo que es importante que sea un punto.(CAMBIAR LA COMA POR EL PUNTO)
COMPARAR con la columna MONTHLY INCOME y ver si son los mismo datos. SI SÍ podemos BORRAR esta columna.

**datebirth** - Esta CORRECTA
Podemos mirar si es una empresa 'vieja' o 'joven'.

**salary** - (Dejar nos NaN) La separación de decimales es una coma, creo que es importante que sea un punto.(CAMBIAR LA COMA POR EL PUNTO)
Y cambiar el tipo de dato a INTER. 
Explotar los nulos de estas columnas. 
Relacionar esta columna con el de monthly income.

**roledepartament** - Sustituir NaN por 'No data'. Hay cosas escritas mix de mayusculas y minusculas(ManaGER). ¿Hay que homogeneizar esto en min o may? El que esten diferentes escrito hace que coja como unicos cosas que son lo mismo. Pongo ejemplo aqui
' ManaGER  -  Research & Development ',
' MANAger  -  Research & Development ',
' mANaGer  -  Research & Development '

Habría que homogeneizar esto para que de verdad tengamos los diferentes. 
PONER TODOS EN MINUSCULO.

**numberchildren** - Todos son nan. No parece util. 
Hay alguna columna que podemos extraer este dato? 
Si no hay, podemos borrarla. 
Sugerencia a la empresa: al no tener este dato no podemos considerar esta info en el workbalance por ejemplo.

**remotework** - Hay 4 datos. 'Yes', '1', 'False', '0', 'True'. 
Hay que homogeneizar en yes/no o en 1/0. 
1 - > Yes
0 - > No 
False -> No
True -> Yes


## Fase 2:

##Transformación de los datos

-Buscar columnas categoricas: crear funcion para revisar cada una de las columns
-Comparacion de info redundante de cada column
-Revisión de notas. IMPORTANTE
