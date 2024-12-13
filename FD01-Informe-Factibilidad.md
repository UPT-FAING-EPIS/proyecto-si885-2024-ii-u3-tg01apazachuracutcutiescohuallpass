
<center>


![./media/logo-upt.png](./media/logo-upt.png)

**UNIVERSIDAD PRIVADA DE TACNA**

**FACULTAD DE INGENIERIA**

**Escuela Profesional de Ingeniería de Sistemas**

**Sistema *"Herramienta de Seguimiento y Evaluación del Desempeño de Red en Computadoras UPT"**

Curso: Inteligencia de Negocios

Docente: Mag. Patrick Cuadros Quiroga

Integrantes:

Escobar Rejas, Carlos Andrés (2021070016)  
Apaza Ccalle, Albert Kenyi   (2021071075)  
Cutipa Gutierrez, Ricardo    (2021069827)  
Churacutipa Blass, Erick     (2020067578)  
Huallpa Maron, Jesus Antonio (2021071085) 

**Tacna – Perú**

2024


**  
**
</center>
<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

**Sistema *"Herramienta de Seguimiento y Evaluación del Desempeño de Red en Computadoras UPT"***

Informe de Factibilidad

Versión *{1.0}*

|CONTROL DE VERSIONES||||||
| :-: | :- | :- | :- | :- | :- |
|Versión|Hecha por|Revisada por|Aprobada por|Fecha|Motivo|
|1\.0|MPV|ELV|ARV|24/08/2024|Versión Original|

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

# **INDICE GENERAL**

[1. Descripción del Proyecto](#_Toc52661346)

[2. Riesgos](#_Toc52661347)

[3. Análisis de la Situación actual](#_Toc52661348)

[4. Estudio de Factibilidad](#_Toc52661349)

[4.1 Factibilidad Técnica](#_Toc52661350)

[4.2 Factibilidad económica](#_Toc52661351)

[4.3 Factibilidad Operativa](#_Toc52661352)

[4.4 Factibilidad Legal](#_Toc52661353)

[4.5 Factibilidad Social](#_Toc52661354)

[4.6 Factibilidad Ambiental](#_Toc52661355)

[5. Análisis Financiero](#_Toc52661356)

[6. Conclusiones](#_Toc52661357)


<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

**<u>Informe de Factibilidad</u>**

1. <span id="_Toc52661346" class="anchor"></span>**Descripción del Proyecto**

1.1. Nombre del proyecto

"Herramienta de Seguimiento y Evaluación del Desempeño en Redes de Computadoras UPT"

1.2. Duración del proyecto

Empieza el 13 de agosto y termina el 13 diciembre

1.3. Descripción

El proyecto "Herramienta de Seguimiento y Evaluación del Desempeño de Red en Computadoras UPT" consiste en el desarrollo de una solución integral para monitorear y evaluar el rendimiento de la red de computadoras dentro de la Universidad Privada de Tacna (UPT). Esta herramienta está diseñada para proporcionar un análisis detallado del estado y desempeño de los recursos tecnológicos, permitiendo a los administradores de TI identificar y solucionar problemas de manera proactiva. A través de la recopilación de datos, la herramienta facilita la gestión eficiente del rendimiento, asegurando que la red funcione sin interrupciones. Además, incluye funciones de evaluación continua, que ayudan a realizar un seguimiento del rendimiento a lo largo del tiempo, identificar patrones de uso, y proponer mejoras basadas en datos concretos.

1.4. Objetivos 

1.4.1 Objetivo general


- Desarrollar e implementar un sistema robusto que permita la recopilación y supervisión de la red en las computadoras en los laboratorios de la UPT, con el fin de graficar datos relevantes para facilitar el análisis y la toma de decisiones en soporte técnico.

1.4.2 Objetivos Específicos

   - Diseñar un script para la recolección de datos que monitorice el rendimiento de la red de cada computadora en los laboratorios.
- Establecer un mecanismo eficiente para enviar los datos recopilados a una base de datos centralizada, asegurando un almacenamiento adecuado para su análisis posterior. 
- Facilitar la comprensión de la información recopilada mediante la organización de datos que permitan su visualización clara y efectiva.
- Analizar el tráfico de red en el laboratorio A para identificar las horas de mayor actividad, facilitando la optimización del uso de recursos en los laboratorios.
- Evaluar el consumo de internet diario para establecer patrones de uso y detectar posibles congestiones en la red.
- Identificar las direcciones IP con mayor tráfico de red, permitiendo a los administradores detectar equipos o usuarios que puedan estar consumiendo excesivos recursos.
- Determinar los cursos que generan mayor tráfico de red, lo cual puede ayudar en la planificación de recursos y en la mejora del servicio durante las clases.
- Establecer qué clases presentan mayor tráfico de red, proporcionando información valiosa para la gestión de recursos durante los períodos de mayor demanda.
- Apoyar al área de soporte proporcionando información detallada a través de reportes o un dashboard interactivo, lo que permitirá una gestión más proactiva y eficiente de los recursos tecnológicos, facilitando la identificación y resolución de problemas de la red.
- Realizar predicciones del consumo de GB por día de la semana utilizando modelos de análisis de datos, para anticipar la demanda de ancho de banda y optimizar la gestión de recursos en los laboratorios.


<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

2. <span id="_Toc52661347" class="anchor"></span>**Riesgos**

    -Retrasos en el Cronograma: Los retrasos en el desarrollo, pruebas o implementación podrían afectar la fecha de finalización del proyecto, especialmente si dependen de factores externos como la disponibilidad de recursos o la integración con sistemas existentes.

    -Definición Inadecuada de Requisitos: Cambios en los requisitos durante el desarrollo podrían llevar a la necesidad de rediseñar partes del sistema, afectando el alcance y el tiempo del proyecto.  

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

3. <span id="_Toc52661348" class="anchor"></span>**Análisis de la Situación actual**

    3.1. Planteamiento del problema

      La Universidad Privada de Tacna (UPT) enfrenta desafíos significativos en la gestión del rendimiento de su red. En el entorno actual, los administradores de TI lidian con la falta de herramientas adecuadas para monitorear y evaluar el estado y desempeño de los recursos tecnológicos. La ausencia de una solución integral limita la capacidad para identificar y solucionar problemas de manera proactiva, afectando la operación eficiente de la red.

   Actualmente, la supervisión del rendimiento se realiza de manera fragmentada y manual, lo que resulta en un seguimiento inadecuado de los recursos tecnológicos. Esto genera dificultades para mantener las computadoras en un nivel óptimo de operación y para asegurar un funcionamiento continuo de la red. Además, la falta de análisis detallado impide una gestión efectiva e identificación de patrones de uso, lo que podría llevar a problemas recurrentes no detectados a tiempo.

   Para abordar estas deficiencias, es esencial desarrollar una herramienta de seguimiento y evaluación que permita un análisis detallado del desempeño de la red. Esta solución permitirá a los administradores de TI tomar decisiones informadas, identificar problemas potenciales antes de que se conviertan en fallos graves, y proponer mejoras basadas en datos concretos, optimizando así el rendimiento general de la infraestructura tecnológica de la UPT.


    3.2. Consideraciones de software

   Para el proyecto "Herramienta de Seguimiento y Evaluación del Desempeño de Red en Computadoras UPT", se utilizará Python 3.12.5 por su estabilidad y compatibilidad, y Tableau 2021.4 para visualizaciones avanzadas. Estas tecnologías, ampliamente reconocidas y estandarizadas en la industria, ofrecerán un entorno de desarrollo robusto y confiable.

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

4. <span id="_Toc52661349" class="anchor"></span>**Estudio de
    Factibilidad**

    Describir los resultados que esperan alcanzar del estudio de factibilidad, las actividades que se realizaron para preparar la evaluación de factibilidad y por quien fue aprobado.

    4.1. <span id="_Toc52661350" class="anchor"></span>Factibilidad Técnica


      Infraestructura de Red:
         • Conectividad a Internet: La UPT cuenta con conectividad a internet mediante fibra óptica, ofreciendo alta velocidad y estabilidad para la transferencia de datos.
         • Red Física: La infraestructura de red incluye routers, switches y puntos de acceso inalámbricos distribuidos por el campus. Esta red está diseñada para soportar múltiples dispositivos conectados simultáneamente, facilitando la recolección de datos de diferentes puntos sin sobrecargar los recursos.

      Dominio y Gestión de Red:
         • Dominio Institucional: La UPT dispone de un dominio institucional que permite la administración centralizada de las aplicaciones y herramientas de monitoreo. Esto facilita la integración del sistema y su gestión a nivel de toda la red universitaria.


    4.2. <span id="_Toc52661351" class="anchor"></span>Factibilidad Económica

   El propósito del estudio de viabilidad económica, es determinar los beneficios económicos del proyecto o sistema propuesto para la organización, en contraposición con los costos.
        Como se mencionó anteriormente en el estudio de factibilidad técnica wvaluar si la institución (departamento de TI) cuenta con las herramientas necesarias para la implantación del sistema y evaluar si la propuesta requiere o no de una inversión inicial en infraestructura informática.
        Se plantearán los costos del proyecto.
        Costeo del Proyecto: Consiste en estimar los costos de los recursos Humanos, materiales o consumibles y/o máquinas) directos para completar las actividades del proyecto}.*

   Definir los siguientes costos:

      4.2.1. Costos Generales


   |Material|Cantidad|Costo Unitario (S/)|
   | :-: | :- | :- |
   |LAPTOP INTEL CORE I7 3.4 GHZ MONITOR 27'' RAM 16GB DISCO DURO 1TB + SSD 480GB|1|2900.00||
   |Disco de almacenamiento de seguridad (2 TB), color negro|1|262.00||
   |Cooler Laptop|1|60||
   |Total||3,222.00|


      4.2.2. Costos operativos durante el desarrollo 

      Evaluar costos necesarios para la operatividad de las actividades de la empresa durante el periodo en el que se realizara el proyecto. Los costos de operación pueden ser renta de oficina, agua, luz, teléfono, etc.

   
