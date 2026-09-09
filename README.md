# Laboratorio 1 — Notebooks de Python

Notebooks de Python para ser utilizadas en el curso de Laboratorio 1, Cátedra Pablo Cobelli
(DF, FCEN, UBA).

Acá van a encontrar el material de cálculo y análisis de datos que usamos a lo largo de la
materia: desde una referencia rápida de Python para las primeras clases, hasta propagación de
errores, ajustes por cuadrados mínimos y análisis de imágenes.

## Cómo abrirlas en Google Colab

No hace falta instalar nada. Cada notebook empieza con un badge como este:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pablocobelli/laboratorio1/blob/main/notebooks/Referencia_rapida_Laboratorio_1.ipynb)

**Hagan click sobre el badge** y la notebook se abre directamente en Google Colab, lista para
ejecutar. Cada badge abre su propia notebook.

### Importante: cómo guardar sus cambios

Cuando abren una notebook desde este repositorio, la están abriendo en modo de sólo lectura:
pueden ejecutarla y modificarla, pero **si cierran la pestaña pierden todo lo que hayan hecho**.
Para conservar su trabajo, apenas la abran vayan a:

> **Archivo → Guardar una copia en Drive**

Eso les crea una copia propia en su Google Drive (en la carpeta `Colab Notebooks`), sobre la que
sí pueden trabajar y guardar normalmente con `Ctrl+S`. De ahí en más, trabajen siempre sobre esa
copia. Si prefieren guardarla en su computadora, la opción es **Archivo → Descargar → Descargar
.ipynb**.

## Cómo llevar el código a Spyder

Las notebooks son el formato que usamos para presentar el material en clase, pero el código que
contienen es Python común y corriente: si quieren ejecutarlo o modificarlo en Spyder, pueden
extraerlo sin problema. Hay tres formas, de la más simple a la más completa.

**1. Copiar y pegar.** Si sólo necesitan un fragmento (una función, un ajuste, un gráfico),
seleccionen el contenido de la celda, cópienlo y péguenlo en un archivo nuevo de Spyder. Para la
mayoría de los casos alcanza con esto.

**2. Descargar la notebook entera como script, desde Colab.** Con la notebook abierta en Colab:

> **Archivo → Descargar → Descargar .py**

Obtienen un archivo `.py` con todo el código de la notebook, en orden, y con el texto de las
celdas de markdown convertido en comentarios.

**3. Convertirla en su propia computadora.** Si tienen Anaconda instalado (que es lo que trae
Spyder), ya cuentan con la herramienta que hace esa conversión. Descarguen el archivo `.ipynb` y
desde la terminal ejecuten:

```bash
jupyter nbconvert --to python Standard_Error.ipynb
```

Eso genera `Standard_Error.py` en la misma carpeta.

### Tres detalles a tener en cuenta

Cualquiera sea el camino que elijan, hay tres cosas para revisar en el archivo resultante:

- **Las líneas que empiezan con `%`.** Van a encontrar líneas como `%matplotlib inline`: son
  instrucciones propias de las notebooks, no son Python. Si las dejan, el script no corre.
  **Bórrenlas o coméntenlas**: en Spyder no hacen falta, los gráficos aparecen solos en el panel de
  Plots. (Si descargaron el `.py` desde Colab, la misma línea aparece transformada en algo como
  `get_ipython().run_line_magic('matplotlib', 'inline')`; con esa hagan lo mismo.)

- **Los separadores `# In[ ]:`.** Marcan dónde empezaba cada celda de la notebook. Spyder también
  tiene celdas, pero las marca con `# %%`. Si reemplazan un texto por el otro (Buscar y reemplazar,
  `Ctrl+H`), van a poder ejecutar el script celda por celda con `Ctrl+Enter`, igual que en la
  notebook. Es la forma más cómoda de trabajar y se los recomiendo.

- **Los archivos de datos.** Algunas notebooks leen datos de una dirección de internet: esas
  funcionan igual en Spyder sin cambiar nada. Otras leen un archivo local (por ejemplo
  `datos.csv`); en ese caso asegúrense de que el archivo esté en la misma carpeta que el script, o
  indiquen la ruta completa.

## Contenido

### Para empezar

- **[Referencia rápida de Python y Google Colab](notebooks/Referencia_rapida_Laboratorio_1.ipynb)**
  El punto de partida de la materia. Cómo cargar librerías, ingresar datos a mano o subirlos desde
  un archivo, graficar histogramas y series de datos, trabajar con arrays de `numpy` y calcular
  promedios y desviaciones estándar. Incluye además cómo graficar una gaussiana sobre sus datos.
  Está pensada para consultar y copiar código sin timidez.

### Incertezas y propagación de errores

- **[Desviación estándar de la media (error estándar)](notebooks/Standard_Error.ipynb)**
  Qué distribución tienen los promedios cuando repetimos muchas veces un mismo experimento.
  Simulamos esas repeticiones y verificamos con histogramas de dónde sale la expresión del error
  estándar.

- **[Sympy para propagación de errores](notebooks/Sympy_para_propagacion_de_errores.ipynb)**
  Cálculo simbólico aplicado a la propagación de errores, sobre el ejemplo de medir la aceleración
  gravitatoria con un péndulo simple. Cómo obtener las derivadas parciales con `Sympy` y cómo
  evaluarlas numéricamente sin retipear las expresiones.

- **[Método de Monte Carlo para propagación de errores](notebooks/Monte_Carlo_para_propagacion_de_errores.ipynb)**
  Un método numérico alternativo a la propagación de errores tradicional, aplicado a determinar la
  densidad de un cilindro a partir de su masa y sus dimensiones. Comparamos ambos resultados y
  discutimos por qué difieren, con sus ventajas y desventajas.

### Ajustes, chi-cuadrado y p-valor

- **[Cuadrados mínimos lineales y chi-cuadrado](notebooks/Cuadrados_minimos_lineales_y_chi_cuadrado.ipynb)**
  Cómo hacer un ajuste lineal por cuadrados mínimos, graficarlo con barras de error y evaluar su
  calidad: coeficiente $R^2$, cálculo de $\chi^2$ y su p-valor, y análisis de los residuos.

- **[Chi-cuadrado: interpretación y cálculo](notebooks/Chi_cuadrado.ipynb)**
  Qué significa el $\chi^2$ y cómo se calcula el p-valor asociado, con la tabla de valores de
  referencia y su lectura.

- **[Cómo anticipar el valor de chi-cuadrado a partir del gráfico del ajuste](notebooks/Chi_cuadrado_Como_anticipar_su_valor_a_partir_del_grafico_de_ajuste.ipynb)**
  Un recorrido completo: datos, ajuste, gráfico y cálculo de $\chi^2$ y p-valor, con el objetivo de
  aprender a estimar a ojo, mirando el gráfico, si el $\chi^2$ va a dar razonable.

### Datos e imágenes

- **[Leer archivos de MotionDAQ](notebooks/Leer_archivos_de_MotionDAQ.ipynb)**
  Una función para leer los archivos exportados por el programa MotionDAQ de adquisición de datos y
  convertirlos en arrays de `numpy`, listos para graficar y analizar.

- **[Herramientas para el análisis de imágenes](notebooks/Analisis_basico_de_imagenes.ipynb)**
  Cómo es la representación digital de una foto, qué son los canales de color y cómo usarlos para
  medir. Como aplicación, calculamos el área de una hoja contando píxeles y encontrando la relación
  entre píxeles y milímetros.

- **[Frecuencia de palabras en textos](notebooks/Frecuencia_de_palabras_en_textos.ipynb)**
  Una introducción a las leyes de escala: contamos las palabras de un texto, las ordenamos por
  frecuencia y graficamos ocurrencia contra rango.
