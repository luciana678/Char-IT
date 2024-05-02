## Char-IT

Descargamos la version de python

- [Python 3.8.10](https://www.python.org/downloads/release/python-3810/)

#### Paso 1 Creamos el entorno Virtual
```bash
python -m venv .venv
```

#### Paso 2 Activamos el entorno
```bash
.venv\Scripts\activate
```

En caso de no tener permisos
```bash
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

#### Instalamos las dependencias

```bash
pip install -r requirements.txt -r requirements-dev.txt
```

#### Ejecutamos el proyecto

```bash
livetw init -d
livetw dev
livetw build
```

