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
Desarrollar e implementar un sistema robusto que permita la recopilación y supervisión de la red en las computadoras en los laboratorios de la UPT, con el fin de graficar datos relevantes para facilitar el análisis y la toma de decisiones en soporte técnico.

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

##### Costos Operativos durante el Desarrollo  

| Concepto | Costo |  
|----------|-------|  
| Viáticos | 300.00 |  
| Movilidad del equipo de trabajo | 200.00 |  
| **Total** | **500.00** |  

##### Costos del Ambiente  

| Concepto | Costo |  
|----------|-------|  
| Servicio VPS (Nube) | 350.00 |  
| Software de Diagramas y Arquitectura del Proyecto | 100.00 |  
| **Total** | **450.00** |  

##### Costos de Personal  

| Rol | Personas | Salario Mensual | Horas Mensuales |  
|-----|----------|-----------------|-----------------|  
| Desarrollador | 4 | 1000 | 60 |  
| Gerente de Proyecto | 1 | 1200 | 60 |  

##### Costos Totales del Desarrollo del Sistema  

| Concepto | Costo Total (S/) |  
|----------|------------------|  
| Costos Generales | 3,222.00 |  
| Costos Operativos durante el Desarrollo | 500.00 |  
| Costos del Ambiente | 450.00 |  
| Costos del Personal | 6,000.00 |  
| **Total** | **10,172.00** |

#### 5.1.3. Factibilidad Operativa  
- **Optimización de Recursos:** La herramienta ayudará a optimizar la utilización de los recursos tecnológicos al proporcionar datos detallados sobre el uso de la red.  
- **Mejora en la Toma de Decisiones:** Al disponer de información precisa y actualizada sobre el desempeño de la infraestructura tecnológica, los administradores podrán tomar decisiones basadas en datos.  
- **Facilidad de Uso e Integración:** La herramienta está diseñada para ser fácil de usar e integrarse con los sistemas existentes.  

#### 5.1.4. Factibilidad Social  
- **Aceptación del Proyecto:** La herramienta de monitoreo proporcionará beneficios claros para la comunidad universitaria al mejorar el rendimiento de las computadoras en los laboratorios.  
- **Impacto en los Usuarios:** Los estudiantes y docentes se beneficiarán de un entorno de aprendizaje más eficiente.  
- **Capacitación y Adaptación:** Se deben realizar capacitaciones para el personal de TI y otros usuarios relevantes sobre el uso de la herramienta.  

#### 5.1.5. Factibilidad Legal  
- **Protección de Datos Personales:** La recopilación y análisis de datos debe cumplir con las leyes de protección de datos personales en Perú.  
- **Licenciamiento de Software:** El uso de bibliotecas y herramientas debe estar conforme a sus respectivas licencias de uso.  

#### 5.1.6. Factibilidad Ambiental  
- **Uso de Recursos:** La herramienta hace uso de software basado en Python, lo que no requiere recursos físicos adicionales significativos.  
- **Eficiencia Energética:** La herramienta está diseñada para identificar patrones de uso y consumo de recursos como energía y datos.  


## 5.2. Tecnología de Desarrollo  
Para el desarrollo del sistema SIMGR-UPT, se emplearán tecnologías modernas y escalables que garanticen un rendimiento eficiente y una integración fluida con la infraestructura existente de la UPT. Las tecnologías seleccionadas incluyen:

- **Python**: Este lenguaje de programación será utilizado para desarrollar los scripts que procesarán los datos de red. Python es altamente versátil, fácil de integrar con otros sistemas y cuenta con numerosas bibliotecas que facilitan el manejo de datos y la automatización de tareas.
- **AWS (Amazon Web Services)**: Se utilizarán varios servicios de AWS para el almacenamiento, procesamiento y análisis de los datos de red:
  - **AWS Lambda**: Para la ejecución de scripts automatizados de Python que procesan los datos en la nube.
  - **AWS S3**: Como almacenamiento de datos en la nube, asegurando accesibilidad y alta disponibilidad.
  - **AWS Glue**: Para la integración y transformación de datos, permitiendo la preparación de los datos para análisis.
  - **AWS Athena**: Para realizar consultas SQL sobre los datos almacenados en AWS S3, permitiendo la generación de métricas clave.
- **Power BI**: Se utilizará para la visualización de los datos de forma interactiva, lo que permitirá a los administradores y personal de TI interpretar fácilmente el desempeño de la red y tomar decisiones basadas en los datos recopilados.

Estas tecnologías se eligieron por su capacidad para manejar grandes volúmenes de datos, su integración sencilla y su escalabilidad, asegurando que el sistema sea robusto y eficiente en su ejecución.

## 5.3. Metodología de Implementación  

La implementación del SIMGR-UPT se llevará a cabo utilizando un enfoque ágil, que permitirá al equipo adaptarse rápidamente a los cambios y asegurar la entrega continua de valor a las partes interesadas.
El proceso de implementación se dividirá en las siguientes fases:

- **Fase 1: Análisis y Planificación**
  - **Documento de Visión**: En esta fase, se definieron claramente los objetivos y funcionalidades del sistema, asegurando que el proyecto tenga un enfoque claro desde el inicio. Este documento está completo y aprobado por todas las partes interesadas.
  - **Especificación de Requisitos de Software (SRS)**: En este documento, se detallaron los requisitos funcionales y no funcionales, identificando las necesidades específicas de la UPT en términos de monitoreo de red y rendimiento de los equipos. Todos los requisitos fueron validados y están listos para su implementación.
  
- **Fase 2: Diseño y Desarrollo**
  - **Análisis y Diseño de Sistemas (SAD)**: En esta fase, se elaboraron los diagramas de arquitectura y diseño del sistema, detallando cómo se integrarán los componentes y cómo se gestionarán los flujos de datos. Estos diagramas y la estructura del sistema están completamente definidos y se encuentran listos para la implementación.
  - **Desarrollo**: Se comenzará el desarrollo iterativo, implementando las funcionalidades básicas primero, seguidas de las más avanzadas.

- **Fase 3: Implementación y Pruebas**
  - Durante esta fase, el sistema será probado en un entorno controlado para validar su correcto funcionamiento y asegurar que cumpla con los requisitos especificados. Las pruebas se realizarán de manera continua a medida que se agregan nuevas funcionalidades.

- **Fase 4: Implementación en Producción y Monitoreo**
  - El sistema será desplegado en los laboratorios de la UPT, donde se monitoreará su rendimiento y se recopilarán datos de uso. Durante esta fase, se realizarán ajustes finos y mejoras basadas en el feedback de los usuarios.

Esta metodología garantiza que el sistema será entregado de manera eficiente, con un enfoque claro en la calidad y la mejora continua.

## 6. Cronograma  
![Cronograma](https://github.com/UPT-FAING-EPIS/proyecto-si885-2024-ii-u3-tg01apazachuracutcutiescohuallpass/raw/main/media/cronograma.PNG)


## 7. Presupuesto  

| Concepto | Costo Total (S/) |  
|----------|------------------|  
| Costos Generales | 3,222.00 |  
| Costos Operativos durante el Desarrollo | 500.00 |  
| Costos del Ambiente | 450.00 |  
| Costos del Personal | 6,000.00 |  
| **Total** | **10,172.00** |  

## 8. Conclusiones  
El proyecto es completamente viable, dado que la infraestructura de la UPT permite su implementación sin requerir grandes inversiones adicionales, y los costos previstos son justificados por los beneficios que ofrecerá. Entre estos beneficios destacan una gestión más eficiente de los recursos tecnológicos, optimización del rendimiento de los equipos, reducción de costos operativos a largo plazo y un mantenimiento preventivo más eficaz. Además, el sistema cumple con las normativas legales, asegurando un impacto positivo en la comunidad universitaria, mejorando la calidad del servicio tecnológico, y manteniendo un impacto ambiental mínimo.  


## 9. Recomendaciones

- **Monitoreo Continuo**: Se recomienda realizar un seguimiento constante del rendimiento del sistema y de la red, aprovechando las herramientas de visualización como Power BI para asegurar que los administradores puedan identificar problemas de manera proactiva.
  
- **Entrenamiento y Capacitación**: Para maximizar los beneficios del sistema, se sugiere capacitar al personal de TI y a los administradores de la red en el uso del sistema, asegurando que puedan interpretar correctamente los datos y tomar decisiones informadas.

- **Optimización Regular**: A medida que el sistema y la infraestructura de red evolucionen, se recomienda realizar ajustes regulares en los scripts y en la configuración de AWS para manejar de manera eficiente los crecientes volúmenes de datos.

- **Evaluación de Resultados**: Se recomienda realizar evaluaciones periódicas del desempeño del sistema, con el fin de verificar si las metas iniciales del proyecto se están cumpliendo, y ajustar el sistema en función de nuevos requerimientos o problemas detectados.


## 10. Bibliografía

ISO/IEC 27001:2013. Information technology — Security techniques — Information security management systems — Requirements. International Organization for Standardization.


## 11. Anexos  
### Anexo 01: Informe de Factibilidad  
### Anexo 02: Documento de Visión  
### Anexo 03: Documento SRS  
### Anexo 04: Documento SAD  
### Anexo 05: Manuales y otros documentos
