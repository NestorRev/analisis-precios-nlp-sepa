# Comparación de precios y promociones: DIA vs. Carrefour

## 📌 Descripción del proyecto

Este proyecto analiza y compara los precios de productos comercializados por **DIA** y **Carrefour** utilizando datos publicados por el **Sistema Electrónico de Publicidad de Precios Argentinos (SEPA)** correspondientes a **julio de 2026**.

Los datasets de productos utilizados superan en conjunto los **7,6 millones de registros**, lo que permite trabajar con un volumen significativo de datos reales y desarrollar un proyecto de análisis de datos de forma incremental.

El proyecto combina:

- preparación y limpieza de datos;
- control de calidad;
- integración de fuentes;
- análisis exploratorio de precios;
- análisis de promociones;
- normalización y validación geográfica;
- comparación de precios por provincia;
- construcción de categorías comerciales;
- procesamiento de lenguaje natural (NLP);
- clasificación automática mediante modelos de Machine Learning;
- construcción de una canasta comparable;
- visualización y comunicación de resultados.

El objetivo es construir un análisis **reproducible, documentado y basado en datos reales**, manteniendo una separación clara entre la preparación de los datos, el análisis descriptivo y las etapas posteriores de modelado.

---

## 🎯 Objetivos

Los objetivos generales del proyecto son:

- Integrar y preparar los datasets de productos de DIA y Carrefour.
- Identificar los productos presentes en ambas cadenas.
- Analizar la variabilidad de precios entre sucursales.
- Comparar precios de lista y precios efectivos.
- Analizar la frecuencia, profundidad y alcance de las promociones.
- Preparar y validar la información de sucursales para el análisis territorial.
- Identificar las provincias donde ambas cadenas tienen presencia comparable.
- Analizar las diferencias de precios entre DIA y Carrefour por provincia.
- Construir un conjunto de categorías comerciales para los productos.
- Etiquetar manualmente una muestra de productos para utilizarla como referencia.
- Aplicar técnicas de NLP y modelos de Machine Learning para completar automáticamente la categorización.
- Construir una canasta comparable entre ambas cadenas.
- Integrar los resultados en visualizaciones y conclusiones finales.

El proyecto busca demostrar competencias en:

- **Exploratory Data Analysis (EDA)**
- Limpieza y transformación de datos
- Integración de fuentes
- Análisis estadístico descriptivo
- Análisis de precios y promociones
- Normalización de datos geográficos
- Procesamiento de lenguaje natural (NLP)
- Clasificación de texto
- Machine Learning
- Visualización de datos
- Comunicación de resultados

---

## 🗺️ Etapas del proyecto

| Etapa | Contenido | Estado |
|---|---|---|
| 1 | Preparación, precios y promociones | ✅ Completada |
| 2 | Preparación de sucursales para análisis geográfico | ✅ Completada |
| 3 | Comparación y análisis de precios por provincia | 🟡 En curso |
| 4 | Construcción de categorías de productos | ⬜ Pendiente |
| 5 | Categorización de productos mediante NLP y ML | ⬜ Pendiente |
| 6 | Canasta comparable y conclusiones finales | ⬜ Pendiente |

La estructura del proyecto está organizada de manera incremental: cada etapa prepara los datos y resultados necesarios para la siguiente.

---

# 📊 Fuentes de datos

Este proyecto utiliza datos provenientes del **Sistema Electrónico de Publicidad de Precios Argentinos (SEPA)** con fecha **2026-07-03**, junto con archivos auxiliares utilizados para la normalización geográfica.

A continuación se detallan las fuentes utilizadas y su propósito.

---

## 🏛️ Provincias de Argentina — ISO 3166-2

**Archivo:** `data/metadata/provincias.csv`

**Fuente oficial:** Instituto Geográfico Nacional (IGN)

**Descarga:**  
https://infra.datos.gob.ar/catalog/modernizacion/dataset/7/distribution/7.7/download/provincias.csv

**Descripción:**

Contiene la lista de provincias de Argentina junto con sus códigos ISO 3166-2.

Se utiliza como referencia para:

- verificar los códigos provinciales presentes en SEPA;
- normalizar las referencias geográficas;
- unificar los códigos ISO con nombres de provincias;
- disponer de una nomenclatura común para el análisis posterior.

Este archivo se utiliza como **referencia geográfica auxiliar** y no reemplaza la inspección de los datos originales de SEPA.

---

## 🛒 SEPA — Sistema Electrónico de Publicidad de Precios Argentinos

**Archivos originales:**

```text
data/raw/productos_dia.csv
data/raw/productos_carrefour.csv
data/raw/sucursales_dia.csv
data/raw/sucursales_carrefour.csv
```

**Fuente:** Secretaría de Comercio de la Nación — Sistema SEPA

Los archivos contienen información relacionada con:

- productos;
- precios;
- promociones;
- identificadores de productos;
- identificadores de comercio;
- identificadores de sucursales;
- información de ubicación de las sucursales.

Los archivos de productos son de gran tamaño y se mantienen fuera del repositorio cuando su volumen dificulta su distribución.

Los archivos de sucursales son de menor tamaño y se utilizan para desarrollar el análisis geográfico.

---

## 🧹 Archivos procesados

**Carpeta:** `data/processed/`

Los archivos procesados se generan a partir de los datasets originales después de aplicar las transformaciones necesarias para el análisis.

Entre los productos procesados utilizados en las etapas posteriores se encuentran:

```text
productos_dia_procesado.parquet
productos_carrefour_procesado.parquet
```

Estos archivos contienen el universo de productos utilizado en la comparación desarrollado durante la primera etapa.

El formato **Parquet** permite trabajar con los datos procesados de manera más eficiente que con los archivos CSV originales y facilita la continuidad entre notebooks.

---

# 📏 Unidad de análisis

Para el análisis de precios, una observación representa:

> **un producto determinado en una sucursal determinada.**

La combinación:

```text
id_producto + id_sucursal
```

se utiliza como referencia para identificar una observación producto–sucursal.

Esto es importante porque un mismo producto puede aparecer en múltiples sucursales y, por lo tanto, permite estudiar la variabilidad del precio entre distintos puntos de venta.

Los productos comunes entre DIA y Carrefour se identifican mediante `id_producto`.

---

# 🔎 Etapa 1 — Preparación, precios y promociones

La primera etapa estuvo orientada a transformar los archivos originales de productos en un conjunto de datos adecuado para el análisis comparativo.

## Actividades realizadas

- Carga de los datasets.
- Tratamiento de los campos como texto durante la importación.
- Identificación y eliminación de registros que no corresponden a productos.
- Revisión de valores nulos.
- Control de duplicados.
- Identificación de productos comunes entre DIA y Carrefour.
- Selección de variables relevantes.
- Construcción del precio efectivo.
- Análisis de la dispersión de precios.
- Análisis de promociones.
- Evaluación de la profundidad y alcance de `promo1`.

Los productos comunes se identifican mediante `id_producto`, por lo que los resultados comparativos de esta etapa corresponden al **universo de productos comunes identificado en los datasets analizados**.

---

## 💰 Dispersión de precios

### Rango porcentual

Se utiliza `rango_pct` para medir la diferencia entre el precio máximo y mínimo observado para un producto:

```text
(max - min) / max × 100
```

Esta métrica representa la **brecha entre el precio mínimo y máximo como porcentaje del precio máximo**.

Un rango elevado indica una diferencia importante entre los precios extremos observados para un mismo producto.

El rango no permite por sí solo determinar el origen de una diferencia. Por ese motivo se complementa con otras métricas y con el análisis de precios de lista, precios efectivos y promociones.

---

## 📐 Coeficiente de variación

También se utiliza el **coeficiente de variación (CV)**:

```text
CV = desviación estándar / media
```

El CV permite analizar la dispersión relativa teniendo en cuenta el nivel promedio de precios.

El rango porcentual y el CV se utilizan como métricas complementarias y no representan exactamente el mismo fenómeno.

---

## 🏷️ Precio de lista y precio efectivo

El análisis diferencia entre:

- **Precio de lista**
- **Precio efectivo**

Para este proyecto, el `precio_efectivo` se construye tomando el menor valor entre el precio de lista y el precio correspondiente a `promo1`.

`promo2` se mantiene separada debido a sus características particulares y no se incorpora automáticamente al cálculo general del precio efectivo.

Esta separación permite estudiar:

1. la dispersión de los precios de lista;
2. la dispersión observada al incorporar `promo1`;
3. la profundidad de los descuentos.

La comparación entre precio de lista y precio efectivo es **descriptiva** y no se utiliza para establecer relaciones causales.

---

## 🎟️ Promociones

Las promociones se analizan separando diferentes dimensiones.

### `promo1`

Se utiliza para estudiar las promociones incorporadas al análisis del `precio_efectivo`.

Se analiza:

- frecuencia;
- profundidad del descuento;
- presencia entre sucursales;
- diferencias entre DIA y Carrefour.

### `promo2`

Se mantiene como una variable independiente.

Dentro del universo de productos comunes analizado se observó presencia de `promo2` en DIA y ausencia de registros de `promo2` en Carrefour.

Esta observación corresponde exclusivamente al **dataset y universo analizado** y no implica que una cadena no utilice ese tipo de promoción fuera de los registros considerados.

---

## 📉 Frecuencia, profundidad y alcance

El proyecto separa tres dimensiones de las promociones:

| Dimensión | Pregunta |
|---|---|
| Frecuencia | ¿Con qué frecuencia aparece una promoción? |
| Profundidad | ¿Cuánto se reduce el precio? |
| Alcance | ¿En qué proporción de sucursales aparece? |

La profundidad del descuento se calcula sobre las observaciones que presentan `promo1`.

También se analizó específicamente la proporción de descuentos superiores al **65%**, informando tanto la cantidad de observaciones como el total utilizado como denominador.

Esta separación evita asumir que un descuento elevado necesariamente se encuentra extendido a todas las sucursales.

---

## 🏪 Alcance de `promo1` entre sucursales

Para analizar los descuentos más elevados se seleccionaron los **15 productos con mayor descuento `promo1` observado** para cada cadena.

La selección se realiza tomando el máximo descuento registrado entre las sucursales de cada producto.

> Este TOP 15 identifica los mayores descuentos puntuales observados por producto. No representa necesariamente los productos con mayor descuento promedio entre sucursales.

También se calcula:

```text
frac_sucursales_con_promo
```

Esta variable representa la proporción de observaciones del producto que registra `promo1`.

Dado que se controla previamente la unicidad de `id_producto + id_sucursal`, esta proporción puede interpretarse como la proporción de sucursales observadas en las que aparece `promo1`.

---

## 📌 Principales hallazgos de la Etapa 1

Dentro del universo de productos comunes analizado:

- Carrefour presenta una **mayor heterogeneidad de precios entre sucursales** en las métricas de dispersión estudiadas.
- La comparación entre precio de lista y precio efectivo muestra que la dispersión puede analizarse desde más de una dimensión.
- DIA presenta una **mayor proporción de observaciones con promociones** cuando se consideran conjuntamente `promo1` y `promo2`.
- Al comparar exclusivamente `promo1`, la diferencia de frecuencia promocional se mantiene, aunque con una base de comparación más homogénea.
- DIA presenta una mayor profundidad promedio de `promo1` en el universo analizado.
- Carrefour presenta una proporción relativa mayor de observaciones con descuentos extremos superiores al 65%, aunque representan una fracción minoritaria de sus observaciones promocionadas.
- El análisis del alcance muestra que **profundidad y extensión de una promoción son dimensiones diferentes**.
- El rango de precios por sí solo no permite establecer el origen de las diferencias observadas.

Estas conclusiones se mantienen como resultados **descriptivos del período y universo analizados**, sin atribuir causalidad a las promociones ni a otras características comerciales.

---

# 🏪 Etapa 2 — Preparación de sucursales para análisis geográfico

La segunda etapa tuvo como objetivo preparar los datasets de sucursales de DIA y Carrefour para poder incorporar posteriormente la dimensión territorial al análisis de precios.

El trabajo no consistió simplemente en convertir códigos ISO en nombres de provincias. Fue necesario realizar una **inspección y normalización de las referencias geográficas**, ya que se detectaron inconsistencias en los datos originales.

---

## 🔍 Inspección de los códigos provinciales

Durante la inspección de los valores únicos de `sucursales_provincia` se detectaron códigos ISO utilizados de manera inconsistente.

Por este motivo, se decidió **verificar y corregir las provincias una por una**, antes de realizar la conversión definitiva a nombres.

Esta estrategia permite evitar imputaciones automáticas que podrían trasladar errores del dataset original al análisis posterior.

---

## 🧩 Función auxiliar de inspección

Dado que el procedimiento de revisión debía repetirse para distintos códigos de provincia y para ambas cadenas, se creó una función auxiliar en:

```text
src/inspeccion.py
```

La función centraliza la lógica utilizada durante la inspección de las sucursales y permite:

- reducir la duplicación de código;
- mantener los notebooks más limpios;
- aplicar un procedimiento homogéneo;
- facilitar la trazabilidad de las verificaciones;
- organizar mejor el proceso de normalización geográfica.

---

## ⚠️ Principales inconsistencias detectadas

### DIA — código `AR-J`

Se detectó que DIA utilizaba `AR-J` para sucursales de **Jujuy**, mientras que según ISO 3166-2 `AR-J` corresponde a **San Juan**.

La inspección mostró que las sucursales de DIA bajo ese código correspondían a Jujuy, por lo que fueron normalizadas como:

```text
AR-Y → JUJUY
```

Esto fue relevante porque Carrefour sí utilizaba `AR-J` para San Juan. Por lo tanto, San Juan no formaba parte del territorio común comparable entre ambas cadenas.

---

### Carrefour — código `AR-A`

Se detectaron sucursales de Carrefour asignadas a `AR-A` que pertenecían a:

- Buenos Aires;
- Salta;
- Jujuy.

Como `AR-A` corresponde a Salta, fue necesario revisar individualmente las localidades y reasignar los casos incorrectos.

Entre estas correcciones se identificó una sucursal de Jujuy que permitió incorporar correctamente a Jujuy al territorio común de comparación.

---

### Carrefour — código `AR-B`

Dentro de las sucursales asignadas a `AR-B`, correspondiente a Buenos Aires, se detectaron localidades como:

- Neuquén;
- La Pampa.

Estos registros fueron revisados y corregidos antes de continuar con la normalización.

---

### Carrefour — código `AR-C`

El código `AR-C`, correspondiente a CABA, presentaba múltiples registros pertenecientes a otras provincias.

La inspección permitió identificar sucursales de:

- Córdoba;
- San Luis;
- Buenos Aires;
- Chubut.

Las asignaciones fueron corregidas de acuerdo con la ubicación real de las sucursales.

---

## 🗺️ Normalización de nombres de provincias

Una vez corregidas las inconsistencias relevantes, se creó una columna común:

```text
provincia
```

Esta columna contiene los nombres normalizados de las provincias y se utiliza como referencia geográfica para las etapas posteriores.

La normalización incluye:

- conversión a mayúsculas;
- eliminación de tildes;
- unificación de nombres;
- ajustes específicos para mantener consistencia entre datasets.

Por ejemplo:

```text
AR-S → SANTA FE
AR-X → CORDOBA
AR-Y → JUJUY
AR-C → CABA
```

La columna original `sucursales_provincia` se conserva como referencia del dato de origen.

---

## 🌎 Verificación mediante coordenadas

Después de la normalización se realizó una verificación adicional sobre Carrefour utilizando rangos aproximados de:

- latitud;
- longitud.

Estos rangos se utilizaron como **filtros de detección de posibles anomalías**, no como límites administrativos oficiales de las provincias.

El objetivo fue localizar sucursales cuya ubicación geográfica pudiera no coincidir con la provincia asignada.

El control detectó un caso que requirió revisión:

```text
id_sucursal = 172
```

La inspección de la dirección y de las coordenadas mostró que la sucursal correspondía a **Mendoza** y no a la provincia previamente asignada.

La provincia fue corregida a:

```text
AR-M → MENDOZA
```

---

## 🛒 Exclusión de registros de tiendas online

También se verificó la existencia de registros que pudieran representar tiendas virtuales y no puntos de venta físicos.

La búsqueda se realizó sobre:

```text
sucursales_nombre
sucursales_tipo
```

utilizando patrones relacionados con términos como:

```text
e-commerce
online
web
delivery
virtual
```

En Carrefour no se detectaron coincidencias mediante este procedimiento.

En DIA se detectó un registro identificado como:

```text
id_sucursal = 90000
```

correspondiente a `eCommerce`.

Este registro fue excluido porque no representa una ubicación física y podría distorsionar el análisis territorial.

---

## 🗺️ Territorio común entre DIA y Carrefour

Una vez realizadas las correcciones, se calculó la intersección entre las provincias presentes en ambos datasets.

Se creó la variable:

```python
provincias_comunes
```

que contiene los **nombres normalizados de las 8 provincias coincidentes** entre DIA y Carrefour.

Las provincias son:

| Código ISO | Provincia normalizada |
|---|---|
| `AR-A` | SALTA |
| `AR-B` | BUENOS AIRES |
| `AR-C` | CABA |
| `AR-E` | ENTRE RIOS |
| `AR-S` | SANTA FE |
| `AR-W` | CORRIENTES |
| `AR-X` | CORDOBA |
| `AR-Y` | JUJUY |

### `provincias_coincidentes` vs. `provincias_comunes`

Durante el proceso se utilizó inicialmente una variable denominada:

```text
provincias_coincidentes
```

que contenía los **códigos ISO** de las provincias coincidentes.

Una vez creada y depurada la columna `provincia`, se decidió trabajar con los **nombres normalizados** para las etapas posteriores.

Por este motivo se creó:

```text
provincias_comunes
```

Esta variable contiene los nombres de las ocho provincias coincidentes y permite utilizar directamente la columna `provincia` ya normalizada.

---

## 🏪 Sucursales de las provincias comunes

A partir de `provincias_comunes` se construyeron dos subconjuntos:

```text
sucursales_dia_8
sucursales_carrefour_8
```

Estos datasets contienen exclusivamente las sucursales de DIA y Carrefour ubicadas en las ocho provincias comunes.

Se mantienen separados de los datasets originales para conservar la trazabilidad del proceso y permitir que las fuentes completas puedan seguir utilizándose en otros análisis.

---

## 🔗 Integración de productos y sucursales

Finalmente, los productos procesados se integraron con las sucursales correspondientes mediante `id_sucursal`.

La integración utiliza un `inner merge` para conservar únicamente las observaciones de productos pertenecientes a sucursales incluidas en el territorio común.

Se obtuvieron los siguientes resultados:

### DIA

- Sucursales en provincias coincidentes: **982**
- Sucursales presentes en el dataset integrado: **982**

### Carrefour

- Sucursales en provincias coincidentes: **648**
- Sucursales presentes en el dataset integrado: **633**
- Sucursales sin registros dentro del subconjunto de productos comunes: **15**

La diferencia de Carrefour se interpreta en relación con el recorte utilizado: `productos_carrefour_comunes` contiene únicamente el universo de productos comunes utilizado para la comparación, por lo que algunas sucursales pueden no presentar observaciones dentro de ese subconjunto aunque sí existan en el dataset completo de sucursales.

La integración deja preparados los datos para incorporar la dimensión provincial al análisis de precios.

---

# 📍 Etapa 3 — Comparación y análisis de precios por provincia

**Estado: 🟡 En curso**

Esta etapa constituye el siguiente paso del proyecto y utiliza los datasets de productos y sucursales preparados en las etapas anteriores.

El objetivo es incorporar la dimensión territorial al análisis y estudiar cómo se comportan los precios de los productos comunes entre DIA y Carrefour en las provincias donde ambas cadenas tienen presencia.

El análisis se desarrollará manteniendo como unidad de observación el **producto–sucursal**, para posteriormente construir agregaciones a nivel de producto, provincia y cadena.

Entre los análisis previstos se encuentran:

- comparación de precios entre cadenas dentro de cada provincia;
- diferencias de precios entre provincias;
- comportamiento de los mismos productos en distintas regiones;
- análisis de dispersión territorial;
- comparación de precios de lista y efectivos;
- análisis de promociones cuando resulte pertinente;
- visualizaciones por provincia y cadena.

La comparación deberá tener en cuenta que las cantidades de sucursales y la composición de productos pueden diferir entre provincias y cadenas. Por ello, las comparaciones se realizarán procurando mantener el universo de productos comparable.

---

# 🏷️ Etapa 4 — Construcción de categorías de productos

**Estado: ⬜ Pendiente**

SEPA no proporciona directamente una clasificación comercial suficientemente estructurada para el análisis que se pretende realizar.

Por este motivo, se construirá una clasificación propia de productos.

El primer paso será definir las categorías y establecer criterios claros para su asignación.

Posteriormente se seleccionará una muestra de productos que será **etiquetada manualmente**.

Estas etiquetas servirán como referencia para la etapa posterior de clasificación automática.

La categorización manual será realizada procurando que la muestra contenga variedad suficiente de descripciones y tipos de productos para que los modelos posteriores puedan aprender las características del texto.

---

# 🤖 Etapa 5 — Categorización de productos mediante NLP y ML

**Estado: ⬜ Pendiente**

Una vez construida la clasificación y etiquetada manualmente una muestra de productos, se aplicarán técnicas de **Procesamiento de Lenguaje Natural (NLP)** para transformar las descripciones comerciales en variables utilizables por modelos de Machine Learning.

El flujo previsto es:

```text
Descripciones de productos
        ↓
Limpieza y preprocesamiento de texto
        ↓
Representación numérica del texto
        ↓
Entrenamiento de modelos
        ↓
Evaluación
        ↓
Selección del modelo
        ↓
Categorización automática
```

Entre las técnicas que podrán evaluarse se encuentran representaciones como **TF-IDF** y diferentes modelos de clasificación supervisada.

La evaluación se realizará utilizando métricas apropiadas para clasificación, como:

- Accuracy;
- Precision;
- Recall;
- F1-score;
- matriz de confusión.

El modelo seleccionado se utilizará posteriormente para completar la categorización del universo de productos.

La elección definitiva de técnicas y modelos dependerá de los resultados obtenidos durante la experimentación.

---

# 🛒 Etapa 6 — Canasta comparable y conclusiones finales

**Estado: ⬜ Pendiente**

Una vez que los productos estén categorizados, se construirá una **canasta comparable** entre DIA y Carrefour.

La selección de productos buscará garantizar que los artículos incluidos sean comparables entre ambas cadenas y que la canasta tenga una composición suficientemente representativa para el objetivo del análisis.

En esta etapa se realizarán:

- selección de productos;
- definición de la metodología de cálculo;
- comparación del costo de la canasta;
- análisis por cadena y provincia cuando corresponda;
- construcción de gráficos finales;
- identificación de los resultados más relevantes;
- integración de los principales hallazgos del proyecto;
- documentación de limitaciones;
- elaboración de las conclusiones finales.

La canasta se construirá al final del proyecto porque para ese momento ya estarán disponibles las dimensiones necesarias: productos, precios, sucursales, provincias y categorías.

---

# 📈 Visualizaciones

Las visualizaciones constituyen un componente transversal del proyecto.

A lo largo de las distintas etapas se utilizarán gráficos para comunicar:

- distribución de precios;
- dispersión entre sucursales;
- diferencias entre precio de lista y precio efectivo;
- frecuencia y profundidad de promociones;
- alcance de promociones;
- diferencias de precios por provincia;
- comportamiento de categorías;
- comparación de la canasta;
- resultados finales.

Las visualizaciones se utilizarán como complemento del análisis cuantitativo y estarán acompañadas por una interpretación basada en los datos.

---

# 🧪 Criterios metodológicos

El proyecto mantiene separadas diferentes dimensiones del análisis para evitar mezclar conceptos que responden preguntas distintas.

| Dimensión | Variable / metodología |
|---|---|
| Identificación de productos comunes | `id_producto` |
| Unidad de observación | `id_producto + id_sucursal` |
| Diferencia entre precios extremos | `rango_pct` |
| Dispersión relativa | `CV` |
| Precio sin considerar `promo1` | Precio de lista |
| Precio incorporando `promo1` | `precio_efectivo` |
| Profundidad promocional | `descuento_pct` |
| Presencia de promociones | `contador_promos` |
| Presencia de `promo1` | `promo1` |
| Alcance de `promo1` | `frac_sucursales_con_promo` |
| Territorio común | `provincias_comunes` |

Las interpretaciones se plantean de forma descriptiva y se evita atribuir causalidad cuando los datos no permiten establecerla.

---

# ⚠️ Limitaciones

Los resultados del proyecto deben interpretarse teniendo en cuenta:

- Los datos corresponden a **julio de 2026** y representan el período disponible analizado.
- La comparación de precios se realiza sobre el universo de productos comunes identificado entre las cadenas.
- La información depende de los datos publicados por SEPA.
- Las cantidades y composición de sucursales pueden diferir entre cadenas y provincias.
- Las diferencias de precios pueden estar relacionadas con características de las sucursales que no necesariamente están disponibles en SEPA.
- El rango porcentual es sensible a valores extremos.
- El coeficiente de variación también puede verse afectado por valores extremos.
- `promo2` se mantiene separada de `precio_efectivo`.
- La ausencia de un tipo de promoción en el dataset no demuestra necesariamente su ausencia en la estrategia comercial general de una cadena.
- La normalización geográfica requirió correcciones manuales basadas en localidades, direcciones y coordenadas.
- Los rangos geográficos utilizados para detectar anomalías son filtros aproximados y no representan límites administrativos oficiales.
- La categorización comercial todavía no está disponible de forma directa en SEPA y deberá construirse durante las siguientes etapas.
- La canasta comparable se definirá posteriormente, por lo que sus criterios de selección todavía no forman parte de los resultados actuales.

---

# 🗂️ Estructura del proyecto

La estructura prevista del proyecto es:

```text
analisis-precios-NLP-SEPA/
│
├── README.md
│
├── data/
│   ├── raw/          # Datos originales descargados de SEPA
│   ├── processed/    # Datos procesados en formato Parquet
│   └── metadata/     # Archivos auxiliares de referencia
│
├── src/
│   ├── inspeccion.py # Funciones auxiliares de inspección
│   ├── limpieza/     # Procesos de limpieza, si fueran necesarios
│   ├── nlp/          # Procesamiento de texto
│   └── ml/           # Modelos y utilidades de ML
│
├── notebooks/
│   ├── 01_analisis_dia_carrefour.ipynb
│   └── 02_sucursales_dia_carrefour.ipynb
│
└── outputs/
    ├── figures/      # Visualizaciones
    └── tables/       # Tablas y resultados
```

La estructura podrá ampliarse durante las siguientes etapas sin modificar la organización fundamental del proyecto.

---

# 🛠️ Tecnologías

El proyecto utiliza principalmente:

- **Python**
- **Pandas**
- **NumPy**
- **Matplotlib**
- **Seaborn**
- **Scikit-learn**
- **NLTK / herramientas de procesamiento de texto**
- **Jupyter Notebook**
- **Parquet**

Las herramientas podrán ampliarse durante las etapas de NLP, Machine Learning y construcción de la canasta.

---

# 📚 Estado actual del proyecto

### ✅ Completado

- [x] Carga de datasets de productos.
- [x] Limpieza inicial.
- [x] Control de calidad.
- [x] Identificación de productos comunes.
- [x] Análisis de precios.
- [x] Rango porcentual.
- [x] Coeficiente de variación.
- [x] Precio de lista y precio efectivo.
- [x] Análisis de `promo1`.
- [x] Análisis de `promo2`.
- [x] Frecuencia y profundidad de promociones.
- [x] Análisis del alcance de `promo1`.
- [x] Preparación y limpieza de datasets de sucursales.
- [x] Normalización de provincias.
- [x] Corrección de inconsistencias geográficas relevantes.
- [x] Verificación mediante coordenadas.
- [x] Exclusión del registro de eCommerce de DIA.
- [x] Identificación de las ocho provincias comunes.
- [x] Construcción de `provincias_comunes`.
- [x] Construcción de `sucursales_dia_8`.
- [x] Construcción de `sucursales_carrefour_8`.
- [x] Integración de productos y sucursales para el territorio común.

### 🟡 En curso

- [ ] Comparación y análisis de precios por provincia.

### ⬜ Pendiente

- [ ] Construcción de categorías de productos.
- [ ] Etiquetado manual de productos.
- [ ] Procesamiento NLP.
- [ ] Entrenamiento y evaluación de modelos de clasificación.
- [ ] Categorización automática del universo de productos.
- [ ] Construcción de la canasta comparable.
- [ ] Análisis final de la canasta.
- [ ] Visualizaciones finales.
- [ ] Conclusiones y cierre del proyecto.

---

# 📖 Conclusión

Las primeras dos etapas establecen la base necesaria para continuar el proyecto con una estructura reproducible.

La **Etapa 1** permitió preparar el universo de productos comunes y analizar precios y promociones, diferenciando conceptos como dispersión, precio de lista, precio efectivo, profundidad y alcance promocional.

La **Etapa 2** incorporó la dimensión geográfica, realizando una inspección detallada de las sucursales, corrigiendo inconsistencias en las referencias provinciales, normalizando los nombres y delimitando el territorio común entre ambas cadenas.

Como resultado, se dispone de información preparada para avanzar hacia la **comparación de precios por provincia**, manteniendo la unidad de análisis producto–sucursal y conservando la trazabilidad de las transformaciones realizadas.

Las siguientes etapas incorporarán progresivamente la categorización de productos mediante etiquetado manual, NLP y Machine Learning, para finalmente construir una **canasta comparable** y reunir los principales resultados y conclusiones del proyecto.
