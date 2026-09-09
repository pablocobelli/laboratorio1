#!/usr/bin/env python3
"""Agrega el badge de "Open In Colab" como primera celda de cada notebook.

Sin argumentos procesa todas las notebooks de notebooks/; tambien se le pueden
pasar archivos concretos. Es idempotente: si una notebook ya tiene el badge,
la saltea.

Uso:
    python3 tools/agregar_badge_colab.py
    python3 tools/agregar_badge_colab.py notebooks/Standard_Error.ipynb
"""

import hashlib
import sys
from pathlib import Path

import nbformat

REPO = "pablocobelli/laboratorio1"
BRANCH = "main"
MARCA = "colab-badge.svg"


# El script vive en tools/, de modo que la raiz del repositorio es su carpeta padre.
RAIZ = Path(__file__).resolve().parent.parent


def badge(nombre):
    url = f"https://colab.research.google.com/github/{REPO}/blob/{BRANCH}/notebooks/{nombre}"
    return f"[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]({url})"


def id_para(nombre, ya_usados):
    base = "colab-badge-" + hashlib.sha1(nombre.encode()).hexdigest()[:8]
    identificador, n = base, 0
    while identificador in ya_usados:
        n += 1
        identificador = f"{base}-{n}"
    return identificador


def procesar(path):
    nombre = path.name
    nb = nbformat.read(path, as_version=nbformat.NO_CONVERT)
    minor, celdas_antes = nb.nbformat_minor, len(nb.cells)
    metadata_antes = sorted(nb.metadata.keys())

    if any(MARCA in (c.get("source") or "") for c in nb.cells):
        print(f"SIN CAMBIOS  {nombre}  (ya tiene badge)")
        return False

    celda = nbformat.NotebookNode(
        cell_type="markdown",
        metadata=nbformat.NotebookNode(),
        source=badge(nombre),
    )
    # El campo 'id' solo existe a partir de nbformat 4.5; en 4.0 invalida la notebook.
    if minor >= 5:
        celda["id"] = id_para(nombre, {c.get("id") for c in nb.cells if "id" in c})

    nb.cells.insert(0, celda)
    nbformat.write(nb, path, version=nbformat.NO_CONVERT)

    # Verificamos que no se haya tocado nada mas que la celda agregada.
    nb2 = nbformat.read(path, as_version=nbformat.NO_CONVERT)
    assert nb2.nbformat_minor == minor, f"cambio nbformat_minor en {nombre}"
    assert len(nb2.cells) == celdas_antes + 1, f"cambio la cantidad de celdas en {nombre}"
    assert sorted(nb2.metadata.keys()) == metadata_antes, f"cambio la metadata en {nombre}"
    nbformat.validate(nb2)

    print(f"BADGE        {nombre}  v{nb2.nbformat}.{minor}  "
          f"{celdas_antes} -> {len(nb2.cells)} celdas")
    return True


def main(argv):
    if argv:
        paths = [Path(a).resolve() for a in argv]
    else:
        paths = sorted((RAIZ / "notebooks").glob("*.ipynb"))

    if not paths:
        print("No se encontraron notebooks.")
        return 1

    modificadas = sum(procesar(p) for p in paths)
    print(f"\n{modificadas} de {len(paths)} notebooks modificadas.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
