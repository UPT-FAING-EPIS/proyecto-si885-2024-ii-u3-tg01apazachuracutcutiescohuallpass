# SIMGR-UPT: Sistema de Monitoreo y Gestión de Red para Laboratorios UPT

## GITHUB PAGES subir archivos al bucket web: https://upt-faing-epis.github.io/proyecto-si885-2024-ii-u3-tg01apazachuracutcutiescohuallpass/ 

**Descripción:**  
El **Sistema de Monitoreo y Gestión de Red para Laboratorios UPT (SIMGR-UPT)** tiene como objetivo supervisar y gestionar en tiempo real el rendimiento de la red en los laboratorios de la Universidad Privada de Tacna. Esto incluye monitoreo de ancho de banda, estabilidad de la conexión y detección de problemas para optimizar los recursos y garantizar un entorno eficiente.



## Integrantes

| Nombre                             | Código             |
|------------------------------------|-------------------|
| Escobar Rejas, Carlos Andrés       | (2021070016)       |
| Apaza Ccalle, Albert Kenyi         | (2021071075)       |
| Ricardo Cutipa Gutierrez           | (2021069827)       |
| Erick Churacutipa Blass            | (2020067578)       |
| Jesus Huallpa Maron                | (2021071085)       |


## Reporte de Power BI
📊 **Puedes acceder al reporte de Power BI haciendo clic en el siguiente enlace:**

[Ver Reporte en Power BI](https://app.powerbi.com/view?r=eyJrIjoiNjljYmE5NzAtZjk2My00NDFlLWE5MDktNDAyNzE2OWI0YjZmIiwidCI6IjE2NzFiMjY2LTJhNDktNDYyYi05Zjk1LWU4MzFjOGRlMDRkOSIsImMiOjEwfQ%3D%3D)


## Diagramas

### 1. Construcción de la Infraestructura
![Construcción de la Infraestructura](media/diagramaBrainboard.png)

### 2. Interacción del Usuario sobre lo Creado
![Interacción del Usuario](media/Brainboard-athena.png).


## Inventario de Archivos y Carpetas

### Carpeta Raíz

1. **`data/`**  
   - Contiene los archivos de datos en formato CSV utilizados por el sistema.

2. **`G02_UPTRED.pbix`**  
   - Archivo de Power BI para análisis y visualización de datos.

3. **`lambda_function.zip`**  
   - Comprimido con los siguientes componentes:
     - `s3bucket.py`: Script para subir datos al bucket S3.
     - `datos_combinados.csv`: Archivo combinado generado desde `data`.

4. **`requirements.txt`**  
   - Dependencias necesarias para los scripts Python.

5. **`s3bucket.py`**  
   - Script que sube archivos CSV al bucket S3.

6. **`sqlcsv.py`**  
   - Combina los CSV en `data` para generar `datos_combinados.csv`.

### Carpeta PruebasExpo

1. **`APPs3uploaddata.exe`**  
   - Aplicación de escritorio en Python para subir archivos CSV al bucket S3.

2. **`final data prueba.csv`**  
   - Archivo de prueba para demostración.

3. **`s3uploaddata.py`**  
   - Código fuente de `APPs3uploaddata.exe`.

### Estructura General

```
/
├── data/
│   ├── [Archivos CSV...]
├── G02_UPTRED.pbix
├── lambda_function.zip
│   ├── s3bucket.py
│   ├── datos_combinados.csv
├── requirements.txt
├── s3bucket.py
├── sqlcsv.py
├── PruebasExpo/
│   ├── APPs3uploaddata.exe
│   ├── final data prueba.csv
│   ├── s3uploaddata.py
```

## Pasos de Automatización de Recursos

### 1. Configuración Inicial

- Asegúrate de tener los siguientes archivos en el entorno local:
  - `sqlcsv.py`
  - `s3bucket.py`
  - `requirements.txt`
  - `lambda_function.zip`
  - Carpeta `data/` con los archivos CSV.

### 2. Eliminar Recursos Existentes

Si necesitas limpiar tu entorno, sigue estos pasos:

1. Eliminar datos en el bucket S3:
   ```bash
   aws s3 rm s3://netuptinteligencianegocios --recursive
   ```

2. Eliminar crawler en AWS Glue:
   ```bash
   aws glue delete-crawler --name netuptinteligencianegocios-crawler
   ```

3. Destruir la infraestructura de AWS con Terraform:
   ```bash
   terraform destroy --auto-approve
   ```

### 3. Configuración y Generación de Recursos

1. Ubícate en la carpeta que contiene `main.tf` (Terraform).

2. Inicia Terraform:
   ```bash
   terraform init
   ```

3. Crea la infraestructura:
   ```bash
   terraform apply --auto-approve
   ```

### 4. Automatización con Scripts

1. Combina los archivos CSV de `data/` con `sqlcsv.py`:
   ```bash
   python3 sqlcsv.py
   ```

2. Sube el archivo combinado al bucket S3 con `s3bucket.py`:
   ```bash
   python3 s3bucket.py
   ```

## Configuración del Controlador ODBC para Power BI

### 1. Descargar e Instalar Controlador

- Descarga el controlador desde:  
  [Amazon Athena ODBC Driver v2.0.3.0](https://downloads.athena.us-east-1.amazonaws.com/drivers/ODBC/v2.0.3.0/Windows/AmazonAthenaODBC-2.0.3.0.msi).

### 2. Configuración del ODBC

- Abre el Administrador de ODBC (64 bits).
- Configura un nuevo DSN con los siguientes parámetros:
  - **Data Source Name**: `athena-in`
  - **Description**: `athena-in in Power BI`
  - **Region**: `us-east-1`
  - **Catalog**: `AwsDataCatalog`
  - **Database**: `default`
  - **Workgroup**: `primary`
  - **S3 Output**: `s3://netuptinteligencianegocios/athena-output/`
  - **Authentication Options**: `DEFAULT CREDENTIALS`

### 3. Probar la Conexión

- Presiona **Test** en el ODBC configurado.
- Resultado esperado:
  ```
  Successfully connected to: Athena engine version 3
  Region: us-east-1
  Catalog: AwsDataCatalog
  Workgroup: primary
  Auth Type: Default Credentials
  ```

## Carga de Datos en Power BI

1. Abre Power BI y selecciona **Obtener Datos → Amazon Athena**.
2. Configura el DSN:
   - Introduce el DSN configurado: `athena-in`.
3. Selecciona las tablas disponibles desde `AwsDataCatalog` y cárgalas en Power BI.
4. Realiza ajustes en las visualizaciones según sea necesario.

## Notas Finales

- Asegúrate de que las credenciales de AWS están configuradas antes de ejecutar los scripts.
- Antes de cargar datos en Power BI, verifica que el bucket S3 contiene los datos esperados.
- Durante la exposición, utiliza `final data prueba.csv` para las pruebas de carga en tiempo real.

# **🎥 Explicación y Video**

[**Haz clic aquí para ver el video**](https://youtu.be/sGZVTyP8z5c)

![prediccion1](prediccion1.png)

en esta prediccion la linea roja representa la prediccion y los puntos azules los datos del csv.
como se puede ver la prediccion es casi precisa , ya que hay como 4 puntos azules fuera de la linea pero no estan muy legos de la linea

![prediccion2](prediccion2.png)

codigo:
en este caso utilizamos R

```
El código siguiente, que crea un dataframe y quita las filas duplicadas, siempre se ejecuta y actúa como un preámbulo del script:
dataset <- data.frame(clase, consumo_energia_kwh, dia, docente, Año, Trimestre, Mes, Día, horario, id, ip, laboratorio, navegador, seccion, tema, tiempo_sesion, total_enviado_mb, total_GB, total_recibido_mb, turno, total_mbps)
dataset <- unique(dataset)
Pegue o escriba aquí el código de script:
Información del dataset provisto por Power BI
if (!require(caret)) install.packages("caret", repos = "http://cran.us.r-project.org"/)
if (!require(ggplot2)) install.packages("ggplot2", repos = "http://cran.us.r-project.org"/)

Cargar librerías
library(caret)
library(ggplot2)

datos <- dataset

head(datos)

str(datos)

summary(datos)
if (all(is.na(datos$horario))) {
    datos$horario <- "Sin horario"
} else {
    datos$horario[is.na(datos$horario)] <- "Sin horario"
}

datos$total_enviado_mb <- as.numeric(datos$total_enviado_mb)
datos$total_recibido_mb <- as.numeric(datos$total_recibido_mb)
datos$total_GB <- as.numeric(datos$total_GB)

set.seed(123)
modelo <- train(total_GB ~ total_enviado_mb + total_recibido_mb, data = datos, method = "lm")

modelo_resumen <- summary(modelo)

predicciones <- predict(modelo, datos[, c("total_enviado_mb", "total_recibido_mb")])

datos$prediccion_GB <- predicciones

library(ggplot2)
ggplot(datos, aes(x = total_GB, y = prediccion_GB)) +
  geom_point(color = "blue") +
  geom_abline(slope = 1, intercept = 0, color = "red") +
  labs(title = "Predicción vs Real", x = "Valor Real de total_GB", y = "Predicción de total_GB") +
  theme_minimal()

rmse <- sqrt(mean((predicciones - datos$total_GB)^2))
cat("RMSE:", rmse)
```
