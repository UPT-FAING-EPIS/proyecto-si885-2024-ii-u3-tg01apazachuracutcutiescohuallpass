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

**Propuesta Proyecto**

Versión *{1.0}*

|CONTROL DE VERSIONES||||||  
| :-: | :- | :- | :- | :- | :- |  
|Versión|Hecha por|Revisada por|Aprobada por|Fecha|Motivo|  
|1\.0|MPV|ELV|ARV|24/08/2024|Versión Original|  

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

## ÍNDICE GENERAL

1. [Resumen Ejecutivo](#1-resumen-ejecutivo)  
2. [Planteamiento del Problema](#2-planteamiento-del-problema)  
   - 2.1. [Justificación del Proyecto](#21-justificación-del-proyecto)  
   - 2.2. [Objetivo General](#22-objetivo-general)  
   - 2.3. [Alcance](#23-alcance)  
   - 2.4. [Requerimientos del Sistema](#24-requerimientos-del-sistema)  
   - 2.5. [Restricciones](#25-restricciones)  
   - 2.6. [Supuestos](#26-supuestos)  
   - 2.7. [Resultados Esperados](#27-resultados-esperados)  
   - 2.8. [Metodología de Implementación](#28-metodología-de-implementación)
   - 2.9. [Actores Claves](#29-actores-claves)  
   - 2.10. [Papeles y Responsabilidades del Personal](#210-papeles-y-responsabilidades-del-personal)  
   - 2.11. [Plan de Monitoreo y Evaluación](#211-plan-de-monitoreo-y-evaluación)  
   - 2.12. [Cronograma del Proyecto](#212-cronograma-del-proyecto)  
   - 2.13. [Hitos de Entregables](#213-hitos-de-entregables)  
3. [Presupuesto](#3-presupuesto)  
   - 3.1. [Planteamiento del Presupuesto](#31-planteamiento-del-presupuesto)  
   - 3.2. [Presupuesto](#32-presupuesto)  
   - 3.3. [Análisis de Factibilidad](#33-análisis-de-factibilidad)  
   - 3.4. [Evaluación Financiera](#34-evaluación-financiera)  
4. [Anexos](#4-anexos)  
   - 4.1. [Requerimientos del Sistema](#41-requerimientos-del-sistema)




# **1. Resumen Ejecutivo**

El **Sistema de Monitoreo y Gestión de Red para Laboratorios UPT (SIMGR-UPT)** es una propuesta innovadora para optimizar la infraestructura tecnológica de la Universidad Privada de Tacna. Este sistema tiene como objetivo principal proporcionar una solución integral para el monitoreo continuo del rendimiento de la red en los laboratorios de informática. Se busca garantizar la conectividad estable y eficiente necesaria para apoyar las actividades académicas y administrativas.

## **Antecedentes y Contexto**
Actualmente, la gestión de la red en los laboratorios presenta desafíos significativos:
- **Falta de herramientas de monitoreo proactivo**, lo que dificulta la identificación y resolución de problemas antes de que afecten a los usuarios.
- **Uso ineficiente de los recursos de red**, debido a la falta de análisis histórico y patrones de uso.
- **Impacto en la calidad educativa**, ya que los tiempos de inactividad afectan la experiencia de estudiantes y docentes.

## **Solución Propuesta**
El proyecto SIMGR-UPT empleará tecnologías avanzadas como AWS (Lambda, S3, Glue) y Python para recopilar, procesar y analizar datos de red en tiempo real. Además, el sistema incluirá:
- **Dashboard interactivo** para la visualización de métricas clave.
- **Alertas automáticas** para identificar problemas de conectividad.
- **Reportes analíticos** para optimizar la planificación y mantenimiento.

## **Beneficios Esperados**
1. **Optimización de la conectividad**: Mejora de la estabilidad y desempeño de la red.
2. **Reducción de costos operativos**: A través de decisiones informadas y mantenimiento preventivo.
3. **Mejor experiencia de usuario**: Garantizando un entorno académico eficiente y funcional.
4. **Datos confiables para la toma de decisiones**: Basados en métricas y patrones históricos.

## **Impacto Estratégico**
Este proyecto posicionará a la Universidad Privada de Tacna como líder en la gestión tecnológica, alineándose con los estándares modernos de infraestructura de red. Además, permitirá:
- Mayor competitividad académica.
- Aumento de la satisfacción de estudiantes y docentes.
- Mejora en la reputación institucional.

## **Resumen Financiero**
El presupuesto estimado de S/ 10,172.00 incluye todos los costos asociados al desarrollo, implementación y operación inicial del sistema. Esta inversión está respaldada por un análisis de factibilidad técnica, operativa y económica.

# **2. Planteamiento del Problema**

## **2.1. Justificación del Proyecto**
El desarrollo de un sistema de monitoreo y gestión de red es crucial para resolver los problemas de conectividad que afectan la calidad de las actividades académicas en los laboratorios de informática de la Universidad Privada de Tacna. Actualmente, la falta de monitoreo proactivo ocasiona interrupciones frecuentes y un uso ineficiente de los recursos tecnológicos, lo que impacta negativamente en estudiantes, docentes y personal administrativo.

Implementar el SIMGR-UPT permitirá identificar patrones de uso, resolver problemas antes de que escalen y optimizar la distribución de recursos de red, garantizando un servicio confiable y continuo.

## **2.2. Objetivo General**
Desarrollar e implementar un sistema integral que permita el monitoreo continuo, la gestión eficiente y el análisis detallado del rendimiento de la red en los laboratorios de informática de la Universidad Privada de Tacna.

## **2.3. Alcance**
- **Incluye**:
  - Monitoreo de tráfico de red en los laboratorios.
  - Generación de reportes y alertas automáticas.
  - Análisis de patrones históricos de uso.
- **Excluye**:
  - Monitoreo de dispositivos personales.
  - Gestión de aspectos de ciberseguridad.

## **2.4. Requerimientos del Sistema**
- **Hardware**:
  - Computadoras con procesadores Intel Core i5 o superiores.
  - Almacenamiento SSD para manejo eficiente de datos.
- **Software**:
  - Python 3.12.
  - Servicios de AWS (Lambda, S3, Glue).
  - Herramientas de visualización como Power BI.

## **2.5. Restricciones**
- Presupuesto limitado a S/ 10,172.00.
- Implementación exclusiva con servicios en la nube de AWS.
- Operatividad enfocada exclusivamente en los laboratorios de informática.

## **2.6. Supuestos**
- La infraestructura de red existente soportará la carga de datos generada por el sistema.
- El personal técnico de la universidad estará disponible para las capacitaciones y pruebas del sistema.

## **2.7. Resultados Esperados**
- **Estabilidad en la conectividad**: Reducción significativa de interrupciones.
- **Optimización de recursos**: Uso eficiente del ancho de banda.
- **Soporte técnico mejorado**: Resolución proactiva de problemas.

## **2.8. Metodología de Implementación**
Se utilizará un enfoque incremental que incluye las siguientes etapas:
1. **Levantamiento de requisitos**: Identificar necesidades y especificaciones técnicas.
2. **Diseño del sistema**: Crear diagramas UML y especificar componentes clave.
3. **Desarrollo**: Implementar scripts en Python y configurar servicios AWS.
4. **Pruebas**: Validar la funcionalidad y el rendimiento del sistema.
5. **Implementación**: Desplegar el sistema en un laboratorio piloto y capacitar al personal.

## **2.9. Actores Claves**
- **Área de TI**: Responsable de la gestión y supervisión del sistema.
- **Soporte Técnico**: Operación y mantenimiento diario del sistema.
- **Estudiantes y Docentes**: Usuarios indirectos beneficiados por la mejora en la conectividad.

## **2.10. Papeles y Responsabilidades del Personal**
- **Gerente de Proyecto**:
  - Supervisar las actividades del equipo de desarrollo.
  - Garantizar el cumplimiento de plazos y objetivos.
- **Desarrolladores**:
  - Implementar y probar el sistema.
  - Documentar las soluciones técnicas.
- **Técnicos de Soporte**:
  - Monitorear y operar el sistema diariamente.
  - Generar reportes de uso y alertas.

## **2.11. Plan de Monitoreo y Evaluación**
El desempeño del sistema será evaluado trimestralmente mediante:
- **Métricas clave**:
  - Tiempo promedio de respuesta ante alertas.
  - Reducción en interrupciones de red.
- **Informes de uso**:
  - Generación de reportes automáticos para evaluar patrones de uso y efectividad del sistema.

## ANEXO 01  
### Requerimientos del Sistema de Monitoreo y Gestión de Red para Laboratorios UPT (SIMGR-UPT)
