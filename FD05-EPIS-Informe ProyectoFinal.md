<center>

![Logo UPT](https://github.com/UPT-FAING-EPIS/proyecto-si885-2024-ii-u1-tg01apazachuracutcutiescohuallpa/raw/main/media/logo-upt.png)

**UNIVERSIDAD PRIVADA DE TACNA**  
**FACULTAD DE INGENIERIA**  
**Escuela Profesional de Ingeniería de Sistemas**

**Informe Final**  
**Sistema de Monitoreo y Gestión de Red para Laboratorios UPT (SIMGR-UPT)**

Curso: Inteligencia de Negocios  
Docente: Mag. Patrick Cuadros Quiroga

Integrantes:  
Escobar Rejas, Carlos Andrés (2021070016)  
Apaza Ccalle, Albert Kenyi (2021071075)  
Cutipa Gutierrez, Ricardo (2021069827)  
Churacutipa Blass, Erick (2020067578)  
Huallpa Maron, Jesus Antonio (2021071085)

**Tacna – Perú**  
2024
</center>


<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

**Sistema de Monitoreo y Gestión de Red para Laboratorios UPT (SIMGR-UPT)**

**Informe Final**

Versión *{1.0}*

|CONTROL DE VERSIONES||||||
| :-: | :- | :- | :- | :- | :- |
|Versión|Hecha por|Revisada por|Aprobada por|Fecha|Motivo|
|1\.0|MPV|ELV|ARV|24/08/2024|Versión Original|

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

## ÍNDICE GENERAL

1. [Antecedentes](#1-antecedentes)  
2. [Planteamiento del Problema](#2-planteamiento-del-problema)  
   - 2.1. [Problema](#21-problema)  
   - 2.2. [Justificación](#22-justificación)  
   - 2.3. [Alcance](#23-alcance)  
3. [Objetivos](#3-objetivos)  
   - 3.1. [Objetivo General](#31-objetivo-general)  
   - 3.2. [Objetivos Específicos](#32-objetivos-específicos)  
4. [Marco Teórico](#4-marco-teórico)  
5. [Desarrollo de la Solución](#5-desarrollo-de-la-solución)  
   - 5.1. [Análisis de Factibilidad](#51-análisis-de-factibilidad)  
     * 5.1.1. [Factibilidad Técnica](#511-factibilidad-técnica)  
     * 5.1.2. [Factibilidad Económica](#512-factibilidad-económica)  
     * 5.1.3. [Factibilidad Operativa](#513-factibilidad-operativa)  
     * 5.1.4. [Factibilidad Social](#514-factibilidad-social)  
     * 5.1.5. [Factibilidad Legal](#515-factibilidad-legal)  
     * 5.1.6. [Factibilidad Ambiental](#516-factibilidad-ambiental)  
   - 5.2. [Tecnología de Desarrollo](#52-tecnología-de-desarrollo)  
   - 5.3. [Metodología de Implementación](#53-metodología-de-implementación)  
6. [Cronograma](#6-cronograma)  
7. [Presupuesto](#7-presupuesto)  
8. [Conclusiones](#8-conclusiones)  
9. [Recomendaciones](#9-recomendaciones)  
10. [Bibliografía](#10-bibliografía)  
11. [Anexos](#11-anexos)  

## 1. Antecedentes  

El monitoreo de redes ha evolucionado de ser una tarea manual y reactiva a un proceso automatizado y proactivo. En instituciones educativas, como la Universidad Privada de Tacna (UPT), la gestión eficiente de la infraestructura tecnológica es crucial para garantizar el buen funcionamiento de los recursos, especialmente en los laboratorios de computadoras. La falta de herramientas de monitoreo automatizadas ha generado la necesidad de implementar soluciones que permitan evaluar el rendimiento de la red de manera continua y precisa. Este contexto ha llevado al desarrollo de herramientas como el "Sistema de Monitoreo y Gestión de Red para Laboratorios UPT (SIMGR-UPT)", con el objetivo de optimizar el uso de los recursos de red en la UPT.

## 2. Planteamiento del Problema  
### 2.1. Problema  

La Universidad Privada de Tacna (UPT) enfrenta dificultades en la gestión eficiente de su red de computadoras debido a la falta de un sistema automatizado que permita monitorear el rendimiento de la red de manera continua. La ausencia de visibilidad sobre el uso de los recursos de red dificulta la identificación de problemas de conectividad y la optimización de la infraestructura tecnológica, lo que puede afectar el desempeño de los estudiantes y docentes en los laboratorios de computadoras.

### 2.2. Justificación  
La implementación de una herramienta de monitoreo automatizado es esencial para mejorar la eficiencia operativa de la red en los laboratorios de computadoras de la UPT. Un sistema como el SIMGR-UPT permite la recopilación y análisis de datos sobre el desempeño de la red, lo que facilita la identificación de patrones de uso y posibles problemas de conectividad. Esto permite a los administradores de TI tomar decisiones basadas en datos concretos, mejorar el soporte de red y realizar mantenimientos preventivos, asegurando un funcionamiento óptimo de los recursos tecnológicos y beneficiando tanto a estudiantes como a docentes.

### 2.3. Alcance  
El alcance del proyecto se centra en el análisis del desempeño de la red en los laboratorios de computadoras de la UPT. El sistema SIMGR-UPT incluirá los siguientes componentes clave:

- **Repositorio inicial**: Recepción de datos en formato CSV desde distintas fuentes.
- **AWS Lambda**: Ejecución automatizada de scripts en Python para procesar los datos de red.
- **AWS S3 y Glue**: Almacenamiento y configuración automática de los datos, generando tablas para consulta y análisis.
- **AWS Athena**: Plataforma de consulta para procesar los datos mediante SQL y generar métricas clave.
- **Power BI**: Visualización avanzada e interactiva de los datos.

El sistema también incorporará la automatización del flujo de datos en la nube y tendrá la capacidad de manejar volúmenes crecientes de datos. Sin embargo, no se contempla el desarrollo de integraciones directas con hardware físico ni aplicaciones móviles dentro de este alcance.

## 3. Objetivos  

### 3.1. Objetivo General  
Desarrollar e implementar un sistema robusto que permita la recopilación y supervisión de la red en las computadoras en los laboratorios de la UPT.

### 3.2. Objetivos Específicos  
- Diseñar un script para la recolección de datos que monitorice el rendimiento de la red de cada computadora en los laboratorios.  
- Establecer un mecanismo eficiente para enviar los datos recopilados a una base de datos centralizada, asegurando un almacenamiento adecuado para su análisis posterior.  
- Facilitar la comprensión de la información recopilada mediante la organización de datos que permitan su visualización clara y efectiva.  
- Analizar el tráfico de red en el laboratorio A para identificar las horas de mayor actividad, facilitando la optimización del uso de recursos en los laboratorios.  
- Evaluar el consumo de internet diario para establecer patrones de uso y detectar posibles congestiones en la red.  
- Identificar las direcciones IP con mayor tráfico de red, permitiendo a los administradores detectar equipos o usuarios que puedan estar consumiendo excesivos recursos.  
- Determinar los docentes que generan mayor tráfico de red, lo cual puede ayudar en la planificación de recursos y en la mejora del servicio durante las clases.  
- Establecer qué clases presentan mayor tráfico de red, proporcionando información valiosa para la gestión de recursos durante los períodos de mayor demanda.  
- Apoyar al área de soporte proporcionando información detallada a través de reportes o un dashboard interactivo, lo que permitirá una gestión más proactiva y eficiente de los recursos tecnológicos, facilitando la identificación y resolución de problemas de la red.


### 4. Marco Teórico
El marco teórico de este proyecto se basa en conceptos fundamentales para la implementación del *Sistema de Monitoreo y Gestión de Red para Laboratorios UPT (SIMGR-UPT)*:

#### 1. **Monitoreo de Redes**
El monitoreo de redes permite supervisar el rendimiento de los recursos tecnológicos en tiempo real. A través de herramientas especializadas, se pueden identificar problemas como cuellos de botella y fallas de conectividad, lo que facilita una gestión proactiva de la red.

#### 2. **Gestión del Desempeño de Red**
La gestión del desempeño de red implica evaluar factores como la disponibilidad, la velocidad y la calidad del servicio. Esta gestión es crucial en entornos educativos, donde el acceso confiable a los recursos en línea es esencial para las actividades académicas.

#### 3. **Análisis de Datos y Automatización**
El análisis automatizado de datos recolectados de la red permite identificar patrones y detectar problemas de manera anticipada. Tecnologías como Python y AWS facilitan la recopilación, almacenamiento y procesamiento de grandes volúmenes de datos para generar informes útiles.

#### 4. **Seguridad de la Información**
La seguridad de la información es vital para proteger los datos sensibles relacionados con el desempeño de la red. Se implementarán medidas de encriptación y autenticación para garantizar la privacidad e integridad de los datos.

#### 5. **Tecnologías en la Nube**
El uso de servicios en la nube, como AWS Lambda y S3, facilita el almacenamiento y procesamiento eficiente de datos. Estas plataformas permiten una escalabilidad flexible, adaptándose a las crecientes necesidades de monitoreo.


## 5. Desarrollo de la Solución  

### 5.1. Análisis de Factibilidad  

#### 5.1.1. Factibilidad Técnica  
**Infraestructura de Red:**  
- **Conectividad a Internet:** La UPT cuenta con conectividad a internet mediante fibra óptica, ofreciendo alta velocidad y estabilidad para la transferencia de datos.  
- **Red Física:** La infraestructura de red incluye routers, switches y puntos de acceso inalámbricos distribuidos por el campus. Esta red está diseñada para soportar múltiples dispositivos conectados simultáneamente, facilitando la recolección de datos de diferentes puntos sin sobrecargar los recursos.  

**Dominio y Gestión de Red:**  
- **Dominio Institucional:** La UPT dispone de un dominio institucional que permite la administración centralizada de las aplicaciones y herramientas de monitoreo. Esto facilita la integración del sistema y su gestión a nivel de toda la red universitaria.  

#### 5.1.2. Factibilidad Económica  
El propósito del estudio de viabilidad económica es determinar los beneficios económicos del proyecto o sistema propuesto para la organización, en contraposición con los costos.

##### Costos Generales  

| Material | Cantidad | Costo Unitario (S/) |  
|----------|----------|---------------------|  
| LAPTOP INTEL CORE I7 3.4 GHZ MONITOR 27'' RAM 16GB DISCO DURO 1TB + SSD 480GB | 1 | 2900.00 |  
| Disco de almacenamiento de seguridad (2 TB), color negro | 1 | 262.00 |  
| Cooler Laptop | 1 | 60.00 |  
| **Total** | | **3,222.00** |  
