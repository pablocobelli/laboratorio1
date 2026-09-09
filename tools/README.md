# tools

Utilidades de mantenimiento del repositorio. No son material del curso: los estudiantes no
necesitan nada de esta carpeta.

## `agregar_badge_colab.py`

Agrega, como primera celda de cada notebook, el badge que permite abrirla directamente en Google
Colab:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pablocobelli/laboratorio1/blob/main/notebooks/Referencia_rapida_Laboratorio_1.ipynb)

Cada badge apunta a su propia notebook, así que el enlace se arma a partir del nombre del archivo.
**Sirve sobre todo al agregar una notebook nueva**: en vez de escribir el enlace a mano, se corre
el script y queda puesto.

### Uso

Sin argumentos, recorre todas las notebooks de `notebooks/`:

```bash
python3 tools/agregar_badge_colab.py
```

También acepta archivos concretos:

```bash
python3 tools/agregar_badge_colab.py notebooks/Mi_notebook_nueva.ipynb
```

Se puede ejecutar desde cualquier directorio del repositorio. Requiere `nbformat`, que ya viene
incluido con Anaconda y con Jupyter.

### Qué hace y qué no

El script es **idempotente**: si una notebook ya tiene el badge, la deja intacta y lo informa. Se
puede correr las veces que haga falta sin miedo a duplicar nada.

Además, se limita a insertar esa única celda:

- No modifica ninguna otra celda, ni las salidas guardadas, ni la metadata de la notebook.
- Respeta la versión de cada archivo. El campo `id` de las celdas sólo existe a partir de nbformat
  4.5; en las notebooks 4.0 incluirlo las volvería inválidas, así que se agrega únicamente donde
  corresponde. En este repositorio conviven ambas versiones.
- Antes de terminar, vuelve a leer cada archivo y verifica que la versión, la cantidad de celdas y
  la metadata sean las esperadas, y lo valida con `nbformat.validate`.

Una salida típica al correrlo con todo ya en orden:

```
SIN CAMBIOS  Chi_cuadrado.ipynb  (ya tiene badge)
BADGE        Mi_notebook_nueva.ipynb  v4.5  12 -> 13 celdas

1 de 10 notebooks modificadas.
```

### Si cambia el nombre del repositorio o la rama

Los enlaces se arman con las constantes `REPO` y `BRANCH` que están al principio del script. Si
alguna vez cambian, hay que editarlas ahí y volver a generar los badges (borrando antes los
existentes, ya que el script no reescribe los que encuentra).
