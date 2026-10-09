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
| 3 | Comparación y análisis de precios por provincia | ✅ Completada |
| 4 | Construcción de categorías de productos | 🟡 En curso  |
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

**Estado: ✅ Completada**

La tercera etapa incorporó la dimensión territorial al análisis de precios entre DIA y Carrefour. Para ello se integró la información de productos con los datos de sucursales preparados en la Etapa 2 y se construyeron universos comparables a nivel de **producto, provincia y cadena**.

El análisis mantuvo como unidad de observación el **producto–sucursal**, pero realizó agregaciones posteriores a nivel de producto–provincia–cadena para comparar los precios de los mismos productos en territorios equivalentes.

El objetivo principal fue determinar cómo varían los precios entre DIA y Carrefour según la provincia, analizar la dispersión territorial y estudiar si los patrones observados se mantienen al cambiar la escala geográfica.

---

## 🔎 Construcción del universo comparable

La exploración inicial identificó **19.368 pares producto–provincia** con información comparable entre ambas cadenas dentro de las ocho provincias analizadas.

Antes de construir los universos definitivos se revisaron las diferencias porcentuales extremas. Se detectaron **33 pares producto–provincia** con `|diferencia_pct| > 500%`, correspondientes a **5 productos**.

Estos productos fueron excluidos de los universos posteriores para evitar que diferencias relativas excepcionalmente grandes tuvieran una influencia desproporcionada sobre los indicadores agregados. La exclusión constituye una decisión metodológica de control de valores extremos y no implica afirmar que los registros originales sean necesariamente errores.

Luego del filtrado se construyeron dos universos con cobertura completa:

| Universo | Productos | Uso |
|---|---:|---|
| 8 provincias | **1.662** | Análisis complementario de sensibilidad |
| 7 provincias, sin Jujuy | **2.220** | Universo principal |

El universo de 7 provincias incorpora **558 productos adicionales**, equivalentes a un **33,57% más** respecto del universo de 8 provincias.

Se adoptó el universo de 7 provincias como referencia principal debido a la cobertura limitada de Carrefour en Jujuy. El universo de 8 provincias se conserva como análisis de sensibilidad para observar el efecto de incluir esa provincia.

---

## 📍 Nivel medio de precios por provincia — universo flexible

Además del universo homogéneo utilizado en la comparación principal, se calculó el nivel medio de precios de cada cadena dentro de cada provincia utilizando un **universo flexible de 8 provincias**. En este análisis no se exige que cada producto esté presente en todas las provincias: solo se requiere que pueda compararse entre DIA y Carrefour dentro de una misma provincia.

Para cada combinación de `provincia + id_producto + cadena`, primero se calcula el precio medio del producto entre las sucursales disponibles. Luego se calcula la media y la mediana provincial de esos precios por producto. De esta forma, cada producto tiene el mismo peso dentro de la provincia, independientemente de cuántas sucursales lo comercialicen.

### Comparación de precios medios

La diferencia porcentual se calcula tomando a Carrefour como referencia:

`Diferencia % = (precio_DIA - precio_Carrefour) / precio_Carrefour × 100`

Los valores negativos indican un precio medio menor en DIA; los positivos indican un precio medio menor en Carrefour.

| Provincia | Precio medio DIA | Precio medio Carrefour | Diferencia |
|---|---:|---:|---:|
| CABA | $5.125,34 | $5.493,11 | **−6,70%** |
| Corrientes | $5.154,72 | $5.505,02 | **−6,36%** |
| Córdoba | $5.122,80 | $5.428,62 | **−5,63%** |
| Buenos Aires | $5.090,94 | $5.362,60 | **−5,07%** |
| Santa Fe | $5.138,23 | $5.389,65 | **−4,66%** |
| Entre Ríos | $5.103,19 | $5.284,00 | **−3,42%** |
| Salta | $5.187,37 | $5.359,54 | **−3,21%** |
| Jujuy | $4.991,47 | $4.759,10 | **+4,88%** |

En **7 de las 8 provincias**, DIA presenta un precio medio inferior al de Carrefour. La mayor diferencia favorable a DIA se observa en CABA (−6,70%), seguida por Corrientes (−6,36%) y Córdoba (−5,63%). **Jujuy es la excepción**: allí, el precio medio de DIA resulta 4,88% superior al de Carrefour.

La comparación de medianas mantiene el mismo sentido general: DIA presenta una mediana inferior en las mismas siete provincias, mientras que Jujuy conserva el patrón inverso. Esto aporta consistencia descriptiva al patrón, aunque la media continúa siendo la medida principal del proyecto.

### Ranking provincial por cadena

El ranking ordena las provincias de menor a mayor precio medio por separado para cada cadena:

- **DIA:** Jujuy, Buenos Aires, Entre Ríos, Córdoba, CABA, Santa Fe, Corrientes y Salta.
- **Carrefour:** Jujuy, Entre Ríos, Salta, Buenos Aires, Santa Fe, Córdoba, CABA y Corrientes.

Jujuy registra el menor precio medio absoluto en ambas cadenas: **$4.991,47 para DIA** y **$4.759,10 para Carrefour**. Sin embargo, eso no significa que DIA sea más barata en esa provincia: la comparación directa entre cadenas muestra lo contrario.

La distancia entre la provincia de menor y mayor precio medio es de aproximadamente **3,9% en DIA** (Jujuy frente a Salta) y **15,7% en Carrefour** (Jujuy frente a Corrientes). En este universo flexible, la amplitud territorial observada es mayor para Carrefour. Esta comparación es descriptiva y no identifica las causas de las diferencias.

El ranking debe interpretarse con una precaución: al tratarse de un universo flexible, la cantidad de productos comparables cambia entre provincias. Por ello, describe el nivel medio del conjunto disponible en cada territorio y **no equivale a comparar una canasta idéntica de productos en las ocho provincias**.

---

## 📊 Comparación de precios entre DIA y Carrefour por provincia

La comparación se realizó producto contra producto dentro de cada provincia. Para cada combinación `provincia + id_producto` se calculó el precio medio observado en cada cadena y posteriormente la diferencia porcentual:

```text
Diferencia % = (precio_DIA - precio_Carrefour) / precio_Carrefour × 100
```

Con esta definición:

- valores negativos indican que **DIA presenta un precio menor**;
- valores positivos indican que **Carrefour presenta un precio menor**.

En el universo principal de 7 provincias, la diferencia media fue negativa en todas las provincias:

| Provincia | Diferencia media DIA vs. Carrefour |
|---|---:|
| CABA | **−5,52%** |
| Corrientes | **−4,59%** |
| Córdoba | **−4,34%** |
| Buenos Aires | **−3,49%** |
| Santa Fe | **−2,52%** |
| Entre Ríos | **−1,67%** |
| Salta | **−1,42%** |

Dentro del universo comparable definido, esto indica una diferencia media favorable a DIA en las siete provincias analizadas.

La proporción de productos en los que DIA presenta un precio menor también varía territorialmente:

- Corrientes: **61,26%**
- CABA: **60,59%**
- Córdoba: **59,46%**
- Santa Fe: **53,20%**
- Entre Ríos: **52,66%**
- Buenos Aires: **47,48%**
- Salta: **44,68%**

Por lo tanto, la ventaja media de DIA no implica que sea más barato en todos los productos ni que tenga la misma intensidad en todas las provincias.

---

## 📐 Media y mediana

La **media** se mantuvo como medida principal del proyecto y la **mediana** se utilizó como medida complementaria para evaluar la robustez de las conclusiones.

Las medianas de las diferencias porcentuales en el universo de 7 provincias fueron:

| Provincia | Diferencia mediana DIA vs. Carrefour |
|---|---:|
| CABA | **−2,66%** |
| Córdoba | **−2,44%** |
| Corrientes | **−0,95%** |
| Entre Ríos | **−0,33%** |
| Santa Fe | **−0,21%** |
| Buenos Aires | **+0,13%** |
| Salta | **+0,88%** |

La diferencia entre media y mediana es relevante: mientras la media resulta favorable a DIA en las siete provincias, la mediana es mucho más cercana a cero y resulta ligeramente positiva en Buenos Aires y Salta.

Esto indica que la ventaja observada mediante la media **no es uniforme a lo largo de toda la distribución de productos** y que algunas diferencias de mayor magnitud influyen sobre el promedio.

---

## 🗺️ Sensibilidad al incluir Jujuy

El universo de 8 provincias permitió comprobar que Jujuy presenta un comportamiento diferente al resto del territorio analizado.

Los resultados para Jujuy fueron:

- diferencia media: **+8,45%**;
- diferencia mediana: **+8,28%**;
- DIA es más barato en **26,84%** de los productos;
- Carrefour es más barato en aproximadamente **70%** de los productos.

El signo positivo indica que, dentro del universo comparable de Jujuy, **Carrefour presenta precios inferiores a DIA**.

Este comportamiento modifica de manera importante la comparación general cuando Jujuy se incorpora al universo. Por este motivo, el análisis de 8 provincias se conserva como sensibilidad y el de 7 provincias se utiliza como referencia principal.

---

## 🌎 Dispersión territorial de los mismos productos

Se analizó también cómo cambia el precio de un mismo producto entre las distintas provincias.

Para ello se utilizó:

```text
rango_pct = (máximo - mínimo) / máximo × 100
```

La mediana del rango porcentual territorial fue:

| Cadena | Mediana del rango territorial |
|---|---:|
| DIA | **3,61%** |
| Carrefour | **9,21%** |

Esto muestra que, dentro del universo analizado, **Carrefour presenta una mayor dispersión territorial de precios para los mismos productos**.

El resultado es descriptivo: el rango permite medir la magnitud de la variación, pero no permite determinar por sí solo las causas de esas diferencias.

---

## 🏪 Dispersión entre sucursales dentro de cada provincia

También se estudió la variación de precios entre sucursales de una misma cadena dentro de cada provincia.

### Carrefour

| Provincia | Mediana del rango entre sucursales |
|---|---:|
| Buenos Aires | **16,20%** |
| Córdoba | **12,27%** |
| CABA | **9,73%** |
| Entre Ríos | **7,96%** |
| Santa Fe | **5,07%** |
| Salta | **0,99%** |
| Corrientes | **0%** |

### DIA

| Provincia | Mediana del rango entre sucursales |
|---|---:|
| Salta | **3,20%** |
| Buenos Aires | **1,95%** |
| CABA | **1,95%** |
| Córdoba | **0%** |
| Corrientes | **0%** |
| Entre Ríos | **0%** |
| Santa Fe | **0%** |

El patrón general muestra una mayor dispersión interna en Carrefour en varias provincias, mientras que DIA presenta valores más reducidos en la mayoría de los territorios.

Esta comparación debe interpretarse teniendo en cuenta la cantidad de sucursales disponibles. Un rango de 0% en una provincia con pocas sucursales no demuestra que una cadena mantenga precios idénticos en todo el territorio.

---

## 🧭 Análisis regional

Como complemento del análisis provincial se agruparon las ocho provincias en tres regiones:

| Región | Provincias |
|---|---|
| **METROPOLITANA** | Buenos Aires, CABA |
| **CENTRO–LITORAL** | Córdoba, Santa Fe, Entre Ríos, Corrientes |
| **NOA** | Jujuy, Salta |

El análisis regional utilizó el universo de **1.662 productos con cobertura completa en las ocho provincias**.

Para evitar que una región recibiera mayor peso simplemente por tener más provincias, primero se calculó el precio medio de cada producto dentro de cada provincia y luego se promediaron las provincias pertenecientes a cada región. De esta forma, cada provincia tiene el mismo peso dentro de su región.

Los resultados fueron:

| Región | Precio medio DIA | Precio medio Carrefour | Diferencia media |
|---|---:|---:|---:|
| CENTRO–LITORAL | $4.895,57 | $5.136,69 | **−3,34%** |
| METROPOLITANA | $4.898,10 | $5.199,96 | **−4,54%** |
| NOA | $5.012,32 | $4.985,51 | **+2,79%** |

En **METROPOLITANA** y **CENTRO–LITORAL**, DIA presenta precios medios regionales inferiores a Carrefour.

En **NOA**, Carrefour presenta un precio medio regional ligeramente inferior a DIA.

La proporción de productos en los que DIA resulta más barato también varía:

- METROPOLITANA: **58,12%**
- CENTRO–LITORAL: **55,05%**
- NOA: **30,93%**

El análisis regional confirma que la relación de precios entre ambas cadenas cambia según el territorio.

### Índice regional

Tomando como referencia 100 la región más barata de cada cadena:

**DIA**

- CENTRO–LITORAL: **100,00**
- METROPOLITANA: **100,05**
- NOA: **102,38**

**Carrefour**

- NOA: **100,00**
- CENTRO–LITORAL: **103,03**
- METROPOLITANA: **104,30**

La región de menor nivel de precios no es la misma para ambas cadenas. En DIA, Centro–Litoral y Metropolitana presentan niveles prácticamente iguales, mientras que NOA se encuentra por encima. En Carrefour, NOA es la región de menor nivel relativo y Metropolitana la de mayor nivel.

Este índice es descriptivo y no representa un índice de costo de vida, participación de mercado ni una canasta de consumo ponderada.

---

## 📌 Principales hallazgos de la Etapa 3

1. La exploración inicial identificó **19.368 pares producto–provincia** comparables. Se detectaron **33 pares extremos**, correspondientes a **5 productos**, con `|diferencia_pct| > 500%`; esos productos se excluyeron de los universos posteriores como decisión de control de valores extremos, sin afirmar que los datos originales fueran necesariamente errores.

2. Se construyeron dos universos homogéneos: **2.220 productos con cobertura completa en 7 provincias** y **1.662 productos con cobertura completa en 8 provincias**. Excluir Jujuy del requisito de cobertura completa incorpora **558 productos adicionales (+33,57%)**. El universo de 7 provincias es la referencia principal y el de 8 se conserva como sensibilidad.

3. En el **universo flexible de 8 provincias**, DIA presenta un precio medio inferior a Carrefour en 7 provincias; Jujuy es la excepción. El ranking absoluto sitúa a Jujuy como la provincia de menor precio medio para ambas cadenas, pero la comparación relativa dentro de Jujuy favorece a Carrefour. Esto demuestra que el nivel absoluto de precios y la diferencia entre cadenas son preguntas distintas.

4. En la comparación producto contra producto del **universo homogéneo de 7 provincias**, la diferencia media porcentual favorece a DIA en las siete provincias. La mediana, sin embargo, es mucho más cercana a cero y resulta ligeramente favorable a Carrefour en Buenos Aires y Salta; por eso la conclusión se refiere a la diferencia media del universo y no a una ventaja uniforme en todos los productos.

5. Jujuy presenta un comportamiento diferencial en el universo homogéneo de 8 provincias: la diferencia media es **+8,45%**, la mediana **+8,28%**, DIA es más barato en **26,84%** de los productos y Carrefour en **70,04%**. Esto respalda mantener el universo de 8 provincias como análisis de sensibilidad.

6. Carrefour presenta mayor dispersión territorial para los mismos productos: la mediana del rango porcentual entre provincias es **9,21%**, frente a **3,61%** para DIA. La dispersión entre sucursales dentro de las provincias también es generalmente mayor en Carrefour, aunque debe interpretarse teniendo en cuenta la cobertura desigual de sucursales y los casos con pocas observaciones.

7. El análisis regional, realizado sobre los **1.662 productos con cobertura completa en las ocho provincias** y otorgando el mismo peso a cada provincia dentro de su región, muestra que DIA presenta precios medios inferiores en **Metropolitana (−4,54%)** y **Centro–Litoral (−3,34%)**. En **NOA**, Carrefour presenta un precio medio inferior, con una diferencia de **+2,79%** para DIA.

8. En conjunto, los resultados muestran que la relación de precios entre DIA y Carrefour depende del territorio y de la escala de análisis. La comparación del nivel medio provincial, la comparación producto a producto y los indicadores de dispersión son complementarios y no deben interpretarse como si respondieran a una misma pregunta.

---

# 🏷️ Etapa 4 — Construcción de categorías de productos

**Estado: 🟡 En curso**

La Etapa 4 comienza una vez finalizado el análisis territorial de precios.

SEPA no proporciona directamente una clasificación comercial suficientemente estructurada para el análisis que se pretende realizar. Por este motivo, se construirá una clasificación propia de productos.

El primer paso será definir las categorías y establecer criterios claros para su asignación. Posteriormente se seleccionará una muestra de productos que será **etiquetada manualmente**.

Estas etiquetas servirán como referencia para la etapa posterior de clasificación automática mediante NLP y Machine Learning.

La categorización manual deberá mantener criterios consistentes y suficientemente claros para que las categorías puedan ser reproducidas y utilizadas como variable de análisis en las siguientes etapas.

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

La evaluación utilizará métricas apropiadas para clasificación, como Accuracy, Precision, Recall, F1-score y matriz de confusión. La elección definitiva de técnicas y modelos dependerá de los resultados obtenidos durante la experimentación.

---

# 🛒 Etapa 6 — Canasta comparable y conclusiones finales

**Estado: ⬜ Pendiente**

Una vez categorizados los productos se construirá una **canasta comparable** entre DIA y Carrefour.

La selección buscará garantizar que los productos incluidos sean comparables entre ambas cadenas y que la canasta tenga una composición coherente con el objetivo final del proyecto.

En esta etapa se realizarán:

- selección de productos;
- definición de la metodología de cálculo;
- comparación del costo de la canasta;
- análisis por cadena y provincia cuando corresponda;
- construcción de gráficos finales;
- integración de los principales hallazgos;
- documentación de limitaciones;
- elaboración de las conclusiones finales.

La canasta se construirá al final porque para ese momento estarán disponibles las dimensiones necesarias: productos, precios, sucursales, provincias y categorías.

---

# 📈 Visualizaciones

Las visualizaciones constituyen un componente transversal del proyecto.

A lo largo de las distintas etapas se utilizan gráficos para comunicar:

- distribución de precios;
- dispersión entre sucursales;
- diferencias entre precio de lista y precio efectivo;
- frecuencia y profundidad de promociones;
- alcance de promociones;
- diferencias de precios por provincia;
- comportamiento territorial y regional;
- comportamiento de categorías;
- comparación de la canasta;
- resultados finales.

Las visualizaciones se utilizan como complemento del análisis cuantitativo y se acompañan de una interpretación basada en los datos.

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
| Comparación territorial principal | Media de precio por producto–provincia–cadena |
| Universo principal Etapa 3 | 7 provincias, sin Jujuy |
| Universo de sensibilidad | 8 provincias |
| Control de valores extremos | `|diferencia_pct| > 500%` |
| Dispersión territorial | Rango porcentual entre provincias |

Las interpretaciones se plantean de forma descriptiva y se evita atribuir causalidad cuando los datos no permiten establecerla.

---

# ⚠️ Limitaciones

Los resultados del proyecto deben interpretarse teniendo en cuenta:

- Los datos corresponden a **julio de 2026** y representan el período disponible analizado.
- La comparación de precios se realiza sobre universos de productos comparables definidos metodológicamente.
- La información depende de los datos publicados por SEPA.
- Las cantidades y composición de sucursales pueden diferir entre cadenas y provincias.
- Jujuy presenta una cobertura limitada de Carrefour dentro del universo utilizado, por lo que se excluye del análisis territorial principal y se conserva como análisis de sensibilidad.
- Las diferencias de precios pueden estar relacionadas con características de las sucursales que no necesariamente están disponibles en SEPA.
- El rango porcentual es sensible a valores extremos.
- El coeficiente de variación también puede verse afectado por valores extremos.
- Se excluyeron 5 productos que presentaron al menos un caso con `|diferencia_pct| > 500%`.
- La exclusión de estos productos constituye una decisión metodológica de control de valores extremos y no demuestra que sus registros originales sean necesariamente incorrectos.
- La media es la medida principal utilizada en la comparación, mientras que la mediana se incorpora como referencia complementaria.
- La dispersión entre provincias y la dispersión entre sucursales representan fenómenos diferentes y no deben interpretarse como equivalentes.
- Valores de dispersión iguales a 0% en provincias con pocas sucursales no permiten concluir que una cadena mantenga precios idénticos en todo el territorio.
- El análisis regional otorga el mismo peso a cada provincia dentro de una región. No representa población, participación de mercado, volumen de ventas ni peso económico.
- Los precios regionales no representan el costo de una canasta de consumo ponderada.
- La comparación de precios y dispersiones es descriptiva y no permite establecer causalidad.
- El análisis detallado de promociones se realizó principalmente en la Etapa 1; la Etapa 3 utiliza el `precio_efectivo` ya construido y se concentra en la dimensión territorial.
- La categorización comercial todavía debe construirse y validarse en las siguientes etapas.
- La canasta comparable todavía no fue definida, por lo que sus criterios de selección y ponderación no forman parte de los resultados actuales.

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
│   ├── 02_sucursales_dia_carrefour.ipynb
│   └── 03_precios_por_provincias.ipynb
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
- [x] Comparación de precios por provincia.
- [x] Construcción de universos comparables de 7 y 8 provincias.
- [x] Revisión y control de diferencias porcentuales extremas.
- [x] Comparación de media y mediana.
- [x] Análisis de diferencias territoriales entre provincias.
- [x] Análisis de dispersión entre sucursales dentro de cada provincia.
- [x] Análisis regional de precios.
- [x] Visualizaciones territoriales y regionales.

### 🟡 En curso

- [ ] Construcción de categorías de productos.

### ⬜ Pendiente

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

Las tres primeras etapas establecen una base progresiva para el análisis comparativo de precios entre DIA y Carrefour.

La **Etapa 1** permitió preparar el universo de productos comunes y analizar precios y promociones, diferenciando conceptos como dispersión, precio de lista, precio efectivo, profundidad y alcance promocional.

La **Etapa 2** incorporó la dimensión geográfica, realizando una inspección detallada de las sucursales, corrigiendo inconsistencias relevantes en las referencias provinciales, normalizando los nombres y delimitando el territorio común entre ambas cadenas.

La **Etapa 3** incorporó el análisis territorial de precios. Se construyeron universos comparables de 7 y 8 provincias, se controlaron diferencias porcentuales extremas y se compararon media y mediana. Además, se incorporó un análisis flexible del nivel medio de precios por provincia y un ranking independiente para cada cadena. Estos resultados se distinguen de la comparación producto a producto en el universo homogéneo. También se analizaron la dispersión territorial entre provincias y sucursales, y las diferencias regionales, que muestran que la relación de precios entre DIA y Carrefour cambia según el territorio y la escala de análisis.

Como resultado, el proyecto dispone ahora de una base territorial preparada para continuar con la **categorización de productos**. La siguiente etapa se centrará en construir una clasificación comercial propia y generar una muestra etiquetada manualmente que pueda utilizarse posteriormente para el desarrollo del componente de **NLP y Machine Learning**.

La **Etapa 4** comienza, por lo tanto, con el análisis territorial ya cerrado y con una estructura de datos que conserva la trazabilidad necesaria para vincular posteriormente las categorías con precios, cadenas y territorios.
