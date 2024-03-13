# Proyecto-devsu
Proyecto que detalla los pasos para la automatización E2E y automatización de APIS.

## 1. Proyecto de automatizacion E2E 
Se detalla los paso de instalacion de algunas librería y la ejecucion de los test para la automatización E2E.

### Install python

- Instalar [Python](https://www.python.org/downloads/).  Asegúrate de marcar la opción "Add Python to PATH"  durante la instalación para que Python y pip puedan ser accedidos desde cualquier ubicación en tu línea de comandos.

- Verificar si está instalado mediante el comando pip

```bash
  python --version
  pip --version
```
### Configurar el proyecto 

- Clonar el proyecto: para esto abre la cmd en el directorio donde desea clonar el proyecto e ingresa el comando:
```bash
  git clone https://github.com/greisloyaga/Proyecto-devsu.git
```

### Configurar librerias

- Agregar pytest: https://docs.pytest.org/en/7.4.x/getting-started.html

```
  pip install -U pytest

```
- Verificar si está instalado mediante el comando pip

```bash
  pytest --version
```

- Agregar selenium: https://pypi.org/project/selenium/#history

```
  pip install selenium

```
- Verificar si está instalado mediante el comando pip

```bash
  selenium --version
```

### Agregar libreria de reportes 
Agregar la libreria: https://pypi.org/project/pytest-html/ para generar reportes en html, para este ejecutar el siguiente comando en el cmd

```
    pip install pytest-html
```

### Ejecutar los test desde la línea de comandos  
- Ingresar a la carpeta test
```
cd  Automatizacion-E2E/tests
```
- Ejecutar los test y generar el reporte en html:
```
pytest test_purchase.py --html=../resultss/results.html
```
- Ir a la carpet results y abrir el reporte "results.html" en el navegador para ver más información de los tests.


## 2. Proyecto de automatizacion APIS 
