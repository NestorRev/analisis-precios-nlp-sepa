# Comparación de precios y promociones: Carrefour vs. DIA

## 📌 Descripción del proyecto

Este proyecto analiza y compara los precios de productos comercializados por **Carrefour** y **DIA** utilizando los datasets de productos y sucursales correspondientes a **julio de 2026** publicados por el **Sistema SEPA**.

Los datasets de productos combinados superan los **7,6 millones de registros**, lo que permite trabajar con un volumen significativo de datos reales y abordar el problema desde una perspectiva de análisis exploratorio, integración de fuentes y modelado posterior.

El proyecto se desarrolla de forma incremental, en etapas. Hasta el momento se completó la preparación e integración de los datos de productos y el análisis exploratorio de precios y promociones (**Etapa 1**), y se encuentra en curso la incorporación de información de sucursales para un análisis geográfico (**Etapa 2**). Las siguientes etapas incorporarán la construcción de una canasta comparable, la categorización mediante NLP y modelos de Machine Learning.

---

## 🎯 Objetivos

Los objetivos generales del proyecto son:

- Integrar y preparar los datasets de Carrefour y DIA.
- Identificar productos presentes en ambas cadenas.
- Analizar la variabilidad de precios entre sucursales.
- Comparar precios de lista y precios efectivos.
- Analizar la presencia y profundidad de las promociones.
- Estudiar el alcance de `promo1` entre sucursales.
- Incorporar información de sucursales para analizar patrones geográficos.
- Construir posteriormente una comparación del costo de una canasta utilizando productos comunes y precios representativos entre sucursales.
- Incorporar una etapa de **NLP** para categorizar productos en rubros comerciales.
- Evaluar modelos de clasificación de texto sobre un subconjunto etiquetado manualmente.
- Utilizar el modelo seleccionado para categorizar el universo completo de productos.
- Enriquecer el análisis mediante técnicas de **Machine Learning**.

El objetivo final es construir un proyecto **claro, reproducible y basado en datos reales**, que permita demostrar competencias en:

- Exploratory Data Analysis (EDA)
- Limpieza y transformación de datos
- Integración de fuentes
- Análisis estadístico descriptivo
- Análisis de precios y promociones
- Análisis geográfico
- Procesamiento de lenguaje natural (NLP)
- Clasificación de texto
- Machine Learning
- Comunicación de resultados mediante visualizaciones y conclusiones

---

## 📊 Fuente de datos

Los datos utilizados provienen del **Sistema SEPA** y corresponden a la información publicada durante **julio de 2026** para:

- Carrefour
- DIA

Se utilizan dos tipos de dataset por cadena:

- **Productos**: información de productos y precios, asociada a cada sucursal mediante `id_comercio` + `id_sucursal`.
- **Sucursales**: información de cada sucursal (ubicación, provincia, localidad, tipo de sucursal, horarios), utilizada para incorporar la dimensión geográfica al análisis de precios.

### Unidad de análisis

Para el análisis de precios, una observación corresponde a:

> **un producto determinado en una sucursal determinada.**

La combinación:

```text
id_producto + id_sucursal
```

se utiliza como referencia para identificar una observación única.

---

## 🗺️ Etapas del proyecto

| Etapa | Contenido | Estado |
|---|---|---|
| 1 | Preparación, precios y promociones | ✅ Completada |
| 2 | Sucursales y análisis geográfico | 🟡 En curso |
| 3 | Construcción de una canasta comparable | ⬜ Pendiente |
| 4 | Categorización de productos mediante NLP | ⬜ Pendiente |
| 5 | Machine Learning | ⬜ Pendiente |

---

# 🔎 Etapa 1 — Preparación, precios y promociones

La primera etapa del proyecto estuvo orientada a transformar los archivos originales de productos en un conjunto de datos adecuado para el análisis, y a realizar un análisis exploratorio de precios y promociones sobre ese conjunto.

## 1.1 Preparación e integración de datos

### Actividades realizadas

- Carga de los datasets.
- Tratamiento de los campos como texto durante la importación para evitar conversiones no deseadas.
- Identificación y eliminación de registros que no corresponden a productos.
- Revisión de valores nulos.
- Control de duplicados.
- Identificación de productos comunes entre ambas cadenas.
- Integración de la información necesaria para realizar comparaciones.
- Selección de variables relevantes para el análisis.

Los productos comunes se identifican mediante `id_producto`, permitiendo realizar comparaciones sobre un universo compartido entre ambas cadenas.

> **Importante:** los resultados de precios de esta etapa se interpretan sobre el universo de productos comunes identificado en los datasets analizados.

## 1.2 Análisis exploratorio de precios

Una vez integrado el universo común de productos, se analizó la variabilidad de precios entre sucursales.

### Rango porcentual

Se utiliza `rango_pct` para medir la diferencia relativa entre el precio máximo y mínimo observado para un producto:

```text
(max - min) / max × 100
```

Esta métrica representa la **brecha entre el precio mínimo y máximo como porcentaje del precio máximo**. Permite identificar productos cuyo precio presenta diferencias importantes entre las sucursales observadas.

**Interpretación:** un rango elevado indica que existe una diferencia significativa entre el menor y el mayor precio registrado para un mismo producto. Sin embargo, el rango por sí solo no permite determinar el origen de esa diferencia. Por ese motivo se complementa con otras métricas y análisis.

### Coeficiente de variación

También se utiliza el **coeficiente de variación (CV)** para evaluar la dispersión relativa de los precios:

```text
CV = desviación estándar / media
```

El CV permite complementar el análisis del rango, especialmente porque tiene en cuenta la relación entre la dispersión y el nivel promedio de precios. Ambas métricas son complementarias y no deben interpretarse como medidas equivalentes.

## 1.3 Precio de lista y precio efectivo

El análisis diferencia entre **precio de lista** y **precio efectivo**.

Para este proyecto, el `precio_efectivo` se construye tomando el menor valor entre el precio de lista y el precio correspondiente a `promo1`. `promo2` se mantiene separada porque representa un tipo de promoción con condiciones particulares y no se incorpora automáticamente al precio efectivo general.

Esta distinción permite estudiar por separado:

1. La dispersión existente en los precios de lista.
2. La dispersión observada cuando se incorpora `promo1`.
3. La profundidad de los descuentos.

**Comparación de dispersión:** se compara la dispersión de precios de lista con la dispersión de precios efectivos. Esta comparación es descriptiva y permite observar cómo cambia la distribución de precios al incorporar `promo1`, sin atribuir causalidad a las promociones.

## 1.4 Análisis de promociones

Las promociones se analizan mediante dos variables principales:

**`promo1`** se utiliza para estudiar las promociones incorporadas al análisis del `precio_efectivo`. Se analiza:

- Frecuencia de aparición.
- Profundidad del descuento.
- Diferencias entre Carrefour y DIA.
- Extensión de la promoción entre sucursales.

**`promo2`** se mantiene como una variable independiente debido a sus características particulares. En el universo de productos comunes analizado, se observa una presencia de `promo2` en DIA y ausencia de registros de `promo2` en Carrefour.

> Esta observación se interpreta exclusivamente dentro del dataset utilizado y no como una afirmación sobre la estrategia comercial general de las cadenas fuera del universo analizado.

### Profundidad del descuento

La profundidad del descuento se calcula comparando el precio de lista con el precio efectivo correspondiente a `promo1`. El análisis se restringe a observaciones que presentan `promo1`.

Esto permite diferenciar entre:

- **Frecuencia:** qué proporción de observaciones presenta una promoción.
- **Profundidad:** cuánto se reduce el precio.
- **Alcance:** en qué proporción de sucursales aparece la promoción.

Estas dimensiones se analizan por separado porque una promoción puede tener un descuento elevado y, al mismo tiempo, estar limitada a pocas sucursales.

También se analiza específicamente la proporción de descuentos superiores al **65%**, informando tanto el número absoluto de observaciones como el total sobre el cual se calcula el porcentaje.

## 1.5 Alcance de `promo1` entre sucursales

Una parte específica del análisis estudia los productos con mayores descuentos registrados mediante `promo1`. Para cada producto se toma el **mayor descuento `promo1` observado entre sus sucursales** y se seleccionan los 15 productos con los valores más altos para cada cadena.

> Este TOP 15 identifica los mayores descuentos puntuales observados por producto. No representa necesariamente los productos con mayor descuento promedio entre sucursales.

Para cada producto también se calcula `frac_sucursales_con_promo`, la proporción de observaciones del producto que registra `promo1`. Dado que previamente se controla la unicidad de `id_producto + id_sucursal`, esta proporción puede interpretarse como la proporción de sucursales observadas en las que aparece `promo1`.

**Interpretación:**

- Un valor cercano a **1** indica una promoción extendida entre las sucursales observadas.
- Un valor bajo indica una promoción concentrada en una parte de las sucursales.

De esta manera se separan dos dimensiones — **profundidad del descuento** y **alcance entre sucursales** —, evitando la interpretación simplificada de que un descuento elevado necesariamente implica una promoción generalizada.

## Principales hallazgos de la Etapa 1

### 1. Carrefour presenta una mayor heterogeneidad de precios

Dentro del universo de productos comunes analizado, Carrefour presenta una dispersión de precios entre sucursales superior a la observada en DIA en las métricas estudiadas. Esto indica que el precio de un mismo producto puede variar de manera considerable dependiendo de la sucursal.

### 2. El rango de precios no explica por sí solo el origen de las diferencias

Una brecha elevada entre precios mínimos y máximos puede estar concentrada en una única sucursal o distribuirse entre varias. Por este motivo, el rango se complementa con el coeficiente de variación y con la comparación entre precio de lista y precio efectivo.

### 3. Precio de lista y precio efectivo representan fenómenos diferentes

La comparación de ambas variables permite observar cuánto cambia la dispersión al incorporar `promo1`. Esto resulta relevante porque una diferencia de precios entre sucursales puede existir incluso antes de considerar las promociones.

### 4. DIA presenta una mayor actividad promocional registrada

Considerando conjuntamente `promo1` y `promo2`, DIA presenta una proporción de observaciones promocionadas considerablemente superior a Carrefour dentro del universo analizado. Cuando se utiliza exclusivamente `promo1`, la comparación se vuelve más homogénea para estudiar el impacto promocional sobre el precio efectivo.

### 5. La profundidad y el alcance de una promoción son dimensiones diferentes

El análisis de los mayores descuentos `promo1` muestra que un descuento elevado no implica necesariamente que esté presente en todas las sucursales. Por eso, el proyecto incorpora explícitamente la variable de alcance entre sucursales.

## Visualizaciones de la Etapa 1

- Distribución de precios.
- Variabilidad de precios entre sucursales.
- Comparación de `rango_pct`.
- Comparación del coeficiente de variación.
- Diferencias entre precio de lista y precio efectivo.
- Distribución de descuentos.
- Relación entre profundidad de descuento y alcance entre sucursales.

Las visualizaciones se utilizan como complemento del análisis estadístico y no como sustituto de las métricas cuantitativas.

---

# 🗺️ Etapa 2 — Sucursales y análisis geográfico (en curso)

Esta etapa incorpora la información de sucursales de ambas cadenas para habilitar comparaciones de precios por provincia. Parte de los datasets de productos ya procesados en la Etapa 1 (guardados en formato Parquet) y de los datasets de sucursales publicados por SEPA.

## 2.1 Carga e integración de datasets de sucursales

- Carga de `sucursales_dia.csv` y `sucursales_carrefour.csv` como texto, para preservar el formato original de identificadores y coordenadas.
- Identificación de la misma fila de metadatos observada en los datasets de productos ("Última actualización: ..."), y su eliminación.

## 2.2 Control de calidad

La revisión de valores nulos muestra dos situaciones distintas entre cadenas:

- En **DIA**, los nulos se concentran en campos no críticos para el análisis geográfico (número de puerta, observaciones, barrio).
- En **Carrefour**, se detectaron **36 registros incompletos**, con `sucursales_provincia` nulo y ausencia simultánea de información en columnas asociadas a horarios de atención — un patrón consistente con filas de datos incompletas, no con valores faltantes aislados.

## 2.3 Imputación de la provincia en Carrefour

Dado que la provincia es una variable central para el análisis regional, se resolvieron los 36 registros incompletos mediante una estrategia en cascada, aplicando cada método solo a los casos no resueltos por el anterior:

1. **Coincidencia exacta con el nombre de la provincia**: en 25 de los 36 casos, el campo `sucursales_localidad` contenía directamente el nombre de la provincia (normalizado a mayúsculas). Se imputó ese valor de forma directa.
2. **Diccionario de ciudades conocidas**: para localidades que corresponden a una ciudad identificable (por ejemplo, "Ciudad Autónoma de Buenos Aires" o "Mar del Plata"), se completó la provincia mediante un mapeo ciudad → provincia.
3. **Inferencia geográfica**: para los registros restantes, sin localidad informada, se utilizaron los rangos de latitud y longitud característicos de la zona para asignar la provincia correspondiente.

Al finalizar este proceso, no quedan valores nulos en `sucursales_provincia` para Carrefour.

## Estado actual de la Etapa 2

**Completado hasta el momento:**

- Carga e integración de los datasets de sucursales.
- Control de calidad y detección de registros incompletos.
- Imputación completa de `sucursales_provincia` en Carrefour.

**Pendiente para continuar esta etapa:**

- Corrección del registro de DIA con `sucursales_provincia` en formato de texto libre ("Buenos Aires") en lugar del código ISO 3166-2 correspondiente.
- Normalización de `sucursales_provincia` a un formato único: actualmente coexisten códigos ISO 3166-2 (registros originales) y nombres completos en mayúsculas (registros imputados en el paso 2.3).
- Cruce de los datasets de productos con los de sucursales, utilizando `id_comercio` + `id_sucursal` como clave.
- Filtrado a las provincias donde ambas cadenas tienen presencia, para asegurar una comparación válida.
- Cálculo y comparación del precio promedio por provincia entre cadenas.

> **Nota metodológica:** la inferencia geográfica del punto 3 es una aproximación basada en rangos de coordenadas observados en los datos, no una georreferenciación exhaustiva. Es adecuada para resolver un número acotado de casos, pero no reemplaza una fuente oficial de límites provinciales si el análisis lo requiriera más adelante.

---

# 🧪 Metodología y criterios de interpretación

El proyecto mantiene una separación entre diferentes dimensiones del análisis:

| Dimensión | Métrica / variable |
|---|---|
| Diferencia entre precios extremos | `rango_pct` |
| Dispersión relativa | `CV` |
| Precio sin considerar `promo1` | Precio de lista |
| Precio incorporando `promo1` | `precio_efectivo` |
| Profundidad promocional | `descuento_pct` |
| Presencia total de promociones | `contador_promos` |
| Presencia de `promo1` | `promo1` |
| Alcance entre sucursales | `frac_sucursales_con_promo` |
| Ubicación de la sucursal | `sucursales_provincia` |

Esta separación permite evitar mezclar conceptos que responden preguntas diferentes.

---

# ⚠️ Limitaciones de las etapas actuales

Los resultados deben interpretarse teniendo en cuenta las siguientes limitaciones:

- El análisis corresponde exclusivamente a **julio de 2026**.
- Se trabaja sobre el universo de productos comunes identificado entre ambas cadenas.
- La comparación depende de la información publicada en los datasets de SEPA.
- Las diferencias de precios pueden estar relacionadas con características de las sucursales que todavía están siendo incorporadas al análisis (Etapa 2, en curso).
- El precio de lista puede presentar diferencias entre cadenas o sucursales.
- El rango porcentual es sensible a los valores extremos.
- El coeficiente de variación también puede verse afectado por valores extremos.
- `promo2` se mantiene separada de `precio_efectivo`.
- La ausencia de un tipo de promoción en el dataset no implica necesariamente su ausencia en la estrategia comercial general de una cadena.
- La imputación geográfica de algunos registros de Carrefour se basa en rangos de coordenadas aproximados, no en una fuente oficial de límites provinciales.
- `sucursales_provincia` todavía combina dos formatos (código ISO y nombre completo) pendientes de unificar.
- La categorización comercial de productos todavía no está incorporada porque SEPA no proporciona directamente rubros comerciales.

---

# 🚧 Próximas etapas

El proyecto continuará de manera incremental.

## Etapa 2 (continuación) — Análisis geográfico de precios

Una vez normalizada la provincia y cruzados los datasets, se comparará el precio promedio (y su dispersión) entre DIA y Carrefour en las provincias donde ambas cadenas tienen presencia.

## Etapa 3 — Construcción de una canasta comparable

Se seleccionarán productos comunes para construir una canasta de referencia. El costo se calculará utilizando el precio promedio observado entre sucursales, permitiendo comparar el costo de una misma selección de productos entre Carrefour y DIA. La metodología de selección de productos y la representatividad de la canasta serán definidas antes de realizar la comparación final.

## Etapa 4 — NLP: identificación y clasificación de categorías

Como SEPA no proporciona rubros comerciales directamente, se construirá una clasificación propia, con categorías como Alimentos, Bebidas, Higiene, Limpieza, Perfumería y Hogar.

Se etiquetará manualmente un subconjunto de productos, y a partir de ese conjunto se entrenarán y evaluarán distintos modelos de clasificación de texto, comparando su desempeño mediante métricas apropiadas para seleccionar el más adecuado y categorizar automáticamente el resto de los productos.

## Etapa 5 — Machine Learning

Una vez enriquecidos los datos mediante la categorización, se evaluarán posibles aplicaciones de Machine Learning para profundizar el análisis. La elección de las variables objetivo y de los modelos dependerá de las preguntas que surjan de las etapas exploratorias anteriores.

---

# 🗂️ Estructura prevista del proyecto

La estructura podrá evolucionar a medida que se incorporen nuevas etapas:

```text
proyecto-supermercados/
│
├── README.md
│
├── notebooks/
│   ├── 01_analisis_dia_carrefour.ipynb
│   └── 02_sucursales_dia_carrefour.ipynb
│
├── data/
│   ├── raw/
│   └── processed/
│       ├── productos_dia_procesado.parquet
│       └── productos_carrefour_procesado.parquet
│
├── src/
│   ├── limpieza/
│   ├── analisis/
│   ├── nlp/
│   └── ml/
│
├── outputs/
│   ├── figures/
│   └── tables/
│
└── requirements.txt
```

La estructura es orientativa y podrá modificarse conforme avance el proyecto.

---

# 🛠️ Tecnologías

El proyecto utiliza principalmente:

- **Python**
- **Pandas**
- **NumPy**
- **Matplotlib**
- **Seaborn**
- **Scikit-learn**
- **NLP / procesamiento de texto**
- **Jupyter Notebook**

Las herramientas y librerías podrán ampliarse durante las siguientes etapas.

---

# 📚 Estado del proyecto

**Estado actual:** 🟢 Etapa 1 completada · 🟡 Etapa 2 en curso

### Completado

- [x] Carga de datasets de productos
- [x] Limpieza inicial
- [x] Control de calidad
- [x] Identificación de productos comunes
- [x] Integración de Carrefour y DIA
- [x] Análisis de variabilidad de precios
- [x] Rango porcentual
- [x] Coeficiente de variación
- [x] Comparación precio de lista vs. precio efectivo
- [x] Análisis de frecuencia de promociones
- [x] Análisis de profundidad de descuentos
- [x] Análisis de `promo1`
- [x] Análisis de `promo2`
- [x] Análisis del alcance de `promo1` entre sucursales
- [x] Visualizaciones y conclusiones de la Etapa 1
- [x] Carga e integración de datasets de sucursales
- [x] Control de calidad de sucursales
- [x] Imputación de provincia en Carrefour

### En curso / próximo

- [ ] Corrección del registro de provincia inconsistente en DIA
- [ ] Normalización de formato de provincia (ISO vs. nombre completo)
- [ ] Cruce de productos con sucursales
- [ ] Comparación de precios por provincia
- [ ] Definición de canasta comparable
- [ ] Comparación del costo de la canasta
- [ ] Etiquetado manual de productos
- [ ] Preprocesamiento NLP
- [ ] Entrenamiento y evaluación de clasificadores
- [ ] Categorización automática del universo completo
- [ ] Aplicaciones de Machine Learning
- [ ] Integración de resultados finales

---

# 📖 Conclusión

La Etapa 1 estableció una base reproducible para comparar precios y promociones entre Carrefour y DIA utilizando datos reales de SEPA, mostrando que esta comparación requiere considerar más de una dimensión: la dispersión entre sucursales, el nivel de precios, la existencia de promociones, la profundidad de los descuentos y su alcance.

La Etapa 2, actualmente en curso, incorpora la dimensión geográfica al análisis: tras integrar y depurar la información de sucursales de ambas cadenas, el siguiente paso es comparar el comportamiento de precios entre provincias donde DIA y Carrefour compiten directamente.

Las etapas siguientes permitirán incorporar nuevas dimensiones —como la canasta de productos y las categorías comerciales— y posteriormente utilizar NLP y Machine Learning para enriquecer el análisis.
