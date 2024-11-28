Documentación:
1. Introducción
El departamento de analítica de datos de ABC Corporation juega un papel fundamental en la mejora de la retención de empleados. A través de herramientas avanzadas de análisis y modelos predictivos, identifica patrones y factores clave que influyen en la satisfacción y rotación del personal. Su enfoque basado en datos permite diseñar estrategias personalizadas para reducir la rotación y mejorar el ambiente laboral. Además, mediante experimentos A/B y el monitoreo en tiempo real, optimiza las decisiones de recursos humanos, brindando soluciones más efectivas y basadas en evidencia.

1.1 Descripción del proyecto.
El proyecto "Transformando el Talento" tiene como objetivo analizar los datos de los empleados de ABC Corporation para identificar los factores que afectan la retención y satisfacción laboral. A través de un análisis exploratorio de los datos, se identificarán patrones relevantes, seguidos de un proceso de transformación de los mismos para asegurar su calidad. Posteriormente, se diseñará un experimento A/B para probar la relación entre la satisfacción laboral y la rotación de empleados. Finalmente, se automatizará el proceso de extracción, transformación y carga (ETL) de los datos en una base de datos, y se presentarán los resultados mediante un informe con visualizaciones para apoyar la toma de decisiones estratégicas.
1.2 Objetivos
Los objetivos del proyecto son los siguientes:
Mejorar la retención de empleados de ABC Corporation mediante el análisis de datos para identificar los factores clave que afectan la satisfacción laboral y la rotación.
Desarrollar habilidades en Python y SQL para gestionar y analizar grandes volúmenes de datos, así como para automatizar procesos mediante la creación de una infraestructura ETL.
Aplicar experimentación A/B para validar hipótesis sobre la relación entre la satisfacción laboral y la rotación de empleados, proporcionando insights basados en datos para la toma de decisiones.
Optimizar la comunicación y trabajo en equipo mediante la implementación de metodologías ágiles (Scrum) y el uso de control de versiones en GitHub.
Generar informes visuales y detallados que presenten los hallazgos del análisis, facilitando la comprensión y apoyo en las decisiones estratégicas de recursos humanos.



1.3 Audiencia 
Este proyecto está diseñado específicamente para el departamento de Recursos Humanos de ABC Corporation, con el objetivo de proporcionarles herramientas basadas en datos para optimizar la retención de empleados y mejorar la satisfacción laboral. A través del análisis detallado de los datos de los empleados, incluyendo la creación de experimentos A/B y visualizaciones informativas, buscamos ofrecer insights claros y accionables que les permitan identificar patrones en la rotación y los factores que influyen en el compromiso de los empleados. Con esta información, el departamento de RRHH podrá tomar decisiones más informadas y estratégicas para fomentar un entorno de trabajo positivo y reducir la rotación de talento clave.

2. Requisitos
El proyecto requiere una combinación de habilidades técnicas, infraestructura adecuada y un proceso bien definido para garantizar su éxito. Desde el punto de vista técnico, se necesita experiencia en Python, SQL y herramientas de visualización de datos para analizar y presentar la información de manera efectiva. A nivel de infraestructura, se requiere una base de datos bien estructurada, un sistema de gestión ágil y un repositorio de código colaborativo como GitHub. Además, el proyecto debe incluir un análisis exploratorio de los datos y la implementación de un experimento A/B, con una comunicación clara y documentación detallada para facilitar la toma de decisiones en el departamento de RRHH.
2.1 Requisitos funcionales 
Los requisitos funcionales del proyecto son los siguientes:
Análisis Exploratorio de Datos (EDA): Realizar un análisis exhaustivo del conjunto de datos para comprender su estructura, identificar patrones y detectar posibles problemas, como datos faltantes o valores inconsistentes.


Transformación de Datos: Implementar funciones para limpiar y transformar los datos, asegurando que estén listos para el análisis, incluyendo la conversión de tipos de datos y la corrección de inconsistencias.


Creación y Gestión de Base de Datos: Diseñar y crear una base de datos relacional para almacenar los datos de los empleados, establecer relaciones entre las tablas y asegurar su integridad.


Experimento A/B: Dividir a los empleados en dos grupos según su nivel de satisfacción, calcular la tasa de rotación de cada grupo y realizar un análisis estadístico para determinar la relación entre la satisfacción y la rotación.


Automatización de ETL: Desarrollar un proceso de extracción, transformación y carga (ETL) que permita actualizar automáticamente la base de datos con nuevos datos y mantener su consistencia.


Visualización y Reportes: Generar visualizaciones en Python para resumir los resultados del análisis y crear informes detallados que faciliten la toma de decisiones en el departamento de RRHH.



2.2 Requisitos técnicos
Los requisitos técnicos del proyecto son los siguientes:
Lenguajes de Programación:


Python: Para realizar el análisis de datos, transformaciones, pruebas A/B y creación de visualizaciones.
SQL: Para la creación y gestión de la base de datos, así como para consultas y manipulaciones de los datos almacenados.
Herramientas y Bibliotecas:


Pandas: Para la manipulación y análisis de los datos.
NumPy: Para realizar cálculos numéricos y operaciones matemáticas.
Matplotlib y Seaborn: Para la visualización de datos.
SciPy o Statsmodels: Para realizar análisis estadísticos, como las pruebas de hipótesis del experimento A/B.
SQLAlchemy: Para la conexión y manipulación de bases de datos relacionales desde Python.
Gestión de Base de Datos:


MySQL, PostgreSQL o SQLite: Sistema de gestión de bases de datos relacionales para almacenar la información de los empleados y facilitar la realización de consultas y análisis.
Entorno de Desarrollo:


Jupyter Notebooks o IDEs como PyCharm o VS Code: Para el desarrollo del código Python y análisis interactivo.
Git y GitHub: Para el control de versiones y la colaboración en equipo, permitiendo un trabajo eficiente y seguro en el código.
Automatización ETL:


Pandas o herramientas como Airflow o Luigi: Para automatizar el proceso de extracción, transformación y carga de datos.
Infraestructura en la Nube (opcional):


Google Cloud o AWS: Si se necesita manejar grandes volúmenes de datos o se quiere utilizar un entorno de nube para almacenamiento y procesamiento de datos.
Este conjunto de tecnologías y herramientas garantizará que el proyecto sea escalable, eficiente y pueda ser fácilmente gestionado y automatizado.

2.3 Herramientas
Las herramientas y tecnologías necesarias para el proyecto son las siguientes, como lenguajes de programación hemos usado Python y SQL. Python para la generación del código necesario para crear el proyecto y SQL para las consultas a la BBDD una vez que tenemos los datos ahí. 
El entorno de desarrollo que se usa es Visual Studio Code. 
Respecto a la BBDD,  para la gestión de bases de datos, diseño de esquemas y ejecución de consultas SQL. MySQL Workbench
Hemos usado GitHub para alojar el repositorio del proyecto y facilitar la colaboración en equipo y Git para el control de versiones del código
En cuanto a frameworks y bibliotecas de Python hemos usado: Pandas para la manipulación y análisis de datos. Requests para realizar solicitudes HTTP a las apis. Glop para la optimización matemática  en la que se necesiten gestionar decisiones bajo restricciones específicas.
Herramientas y Bibliotecas:
Pandas: Para la manipulación y análisis de los datos.
NumPy: Para realizar cálculos numéricos y operaciones matemáticas.
Matplotlib y Seaborn: Para la visualización de datos.
SciPy o Statsmodels: Para realizar análisis estadísticos, como las pruebas de hipótesis del experimento A/B.
SQLAlchemy: Para la conexión y manipulación de bases de datos relacionales desde Python.








3. Arquitectura del sistema


Resumen de la Arquitectura:
Entrada de Datos: Recopilación desde diversas fuentes (bases de datos, encuestas, etc.).
Procesamiento de Datos: Extracción, limpieza y transformación de los datos para su análisis.
Análisis de Datos: Ejecución de análisis estadísticos y pruebas A/B.
Visualización y Reportes: Presentación de los resultados mediante gráficos y dashboards interactivos, junto con la generación de informes automáticos.
Seguridad e Integración: Protección de los datos y conexión con otros sistemas corporativos.
Esta arquitectura garantiza un flujo de trabajo eficiente y seguro para analizar datos y realizar pruebas A/B dentro del departamento de Recursos Humanos.
4. Resumen de los resultados y análisis
1. Rotación de Empleados:
Tasa de rotación: La tasa de rotación total es del 17.64%. Para los empleados satisfechos (SatisfactionLevel 3-4), la rotación es del 15.06%, mientras que para los insatisfechos (SatisfactionLevel 1-2) es del 21.92%. Esto sugiere que la insatisfacción laboral está vinculada con una mayor rotación de empleados.
La tasa de rotación también se desglosa por nivel jerárquico y departamento, lo que permite identificar áreas problemáticas.
2. Hipótesis Económicas:
Salario mensual: No se encontró una relación significativa entre el salario mensual y la satisfacción laboral.
Incremento salarial: Similar al salario, no se encontró una relación entre el incremento salarial y la satisfacción.
Opciones de compra de acciones: Esta variable tampoco mostró correlación significativa con la satisfacción laboral.
Conclusión: El salario y los beneficios económicos no parecen ser factores determinantes para la satisfacción de los empleados en este análisis.
3. Hipótesis sobre Movilidad:
Viajes de trabajo: No se encontró relación significativa entre la cantidad de viajes de trabajo y la satisfacción de los empleados.
Teletrabajo: Aunque no se encontró una relación significativa entre el teletrabajo y la satisfacción, se podría explorar más a fondo añadiendo variables como la preferencia por el trabajo remoto.
Distancia al trabajo: No se detectó que la distancia desde el hogar afecte la satisfacción laboral, posiblemente porque la mayoría de los empleados viven cerca de la oficina.
4. Análisis de Variables Categóricas:
Se realizaron pruebas de Chi-cuadrado para evaluar la relación entre la satisfacción laboral y diversas variables como el campo educativo y el viaje de negocios. Ninguna de estas variables mostró una relación significativa con la satisfacción laboral.
5. Coste de la Rotación:
Se estimó el costo económico asociado a la rotación de empleados, tomando en cuenta factores como reclutamiento, formación y pérdida de productividad. Este análisis resalta el impacto económico de la rotación laboral, lo cual podría ser crucial para la toma de decisiones.
Sugerencias y siguientes pasos:
Mejorar las estrategias de retención:
Como se observa, los empleados insatisfechos tienen una mayor tasa de rotación. Sería útil investigar más a fondo las causas de la insatisfacción laboral (por ejemplo, mediante encuestas o entrevistas) para desarrollar estrategias que mejoren la retención, como mejorar las condiciones de trabajo o fomentar un entorno de trabajo positivo.
Análisis de preferencia por teletrabajo:
Aunque no se encontró una relación significativa entre la satisfacción y el teletrabajo, podría ser valioso recoger más datos específicos sobre la preferencia de los empleados por el trabajo remoto. Esto podría ayudar a ajustar las políticas laborales según las necesidades de los empleados.
Estudios de impacto organizacional:
Investigar cómo los cambios organizacionales (como cambios en la estructura de la empresa, nuevos beneficios, etc.) impactan en la satisfacción laboral y en la retención.
Análisis de otras variables:
Aunque algunas de las variables económicas y de movilidad no mostraron relaciones significativas con la satisfacción, sería interesante explorar otros factores no abordados en el análisis actual, como el estilo de liderazgo, las oportunidades de desarrollo profesional, la cultura organizacional, etc.
Profundización en la educación y el trabajo en equipo:
Aunque no se encontró una relación directa entre el campo educativo y la satisfacción laboral, puede haber otros factores más complejos a considerar. Es posible que algunos roles específicos requieran habilidades o educación especializadas, lo cual podría influir en la satisfacción de los empleados en esos sectores.
Validación y predicción con modelos de Machine Learning:
Si los datos disponibles lo permiten, podrías usar técnicas de modelado predictivo (como regresión logística o árboles de decisión) para identificar factores que predicen con mayor precisión la insatisfacción laboral o la rotación, lo que puede ofrecer insights más detallados para la toma de decisiones.


























5. Guía para desarrolladores
	
5.1 Estructura de código
/Proyecto
│
├── data/                # Carpeta para los datos (csv, excel, etc.)
│   └── df_modificado.csv
│
├── src/                 # Carpeta para el código fuente
│   ├── data_processing/ # Para todo el código relacionado con la preparación de los datos
│   │   ├── clean_data.py
│   │   └── transformations.py
│   ├── visualizations/  # Para todos los gráficos y visualizaciones
│   │   ├── boxplots.py
│   │   └── barplots.py
│   ├── hypothesis_tests/ # Para pruebas estadísticas
│   │   ├── chi_square_tests.py
│   │   └── t_tests.py
│   └── main.py          # Script principal que orquesta el flujo del proyecto
│
├── requirements.txt     # Dependencias del proyecto
└── README.md            # Documentación del proyecto

Presentación: https://docs.google.com/presentation/d/1wAsgBhCEKlBA39O_m0dBYFJocZwah243Q_AfFPY1Ar8/edit#slide=id.p







