# Proyecto-devsu
Proyecto que detalla los pasos para la automatización E2E y automatización de APIS.

### Clonar el proyecto 

- Clonar el proyecto: para esto abre la cmd en el directorio donde desea clonar el proyecto e ingresa el comando:
```bash
  git clone https://github.com/greisloyaga/Proyecto-devsu.git
```

## 1. Proyecto de automatizacion E2E 
En este proyecto se aplica la automatización web usando Selenium. Para aplicar los casos de prueba, utilizaremos el sitio web de prueba https://www.demoblaze.com. A continuación se detalla los paso de instalacion de algunas librería y la ejecucion de los test para la automatización E2E.

## Requisitos previos
### Install python
- Instalar [Python](https://www.python.org/downloads/).  Asegúrate de marcar la opción "Add Python to PATH"  durante la instalación para que Python y pip puedan ser accedidos desde cualquier ubicación en tu línea de comandos.

- Ingresar a la terminal y verificar si está instalado mediante el comando pip

```bash
  python --version
  pip --version
```

### Configurar librerias

- Ingresar a la terminal e instalar pytest: https://docs.pytest.org/en/7.4.x/getting-started.html

```
  pip install -U pytest
```
- Ingresar a la terminal y verificar si está instalado mediante el comando pip

```bash
  pytest --version
```

- Ingresar a la terminal e instalar selenium: https://pypi.org/project/selenium/#history

```
  pip install selenium
```
- Verificar si está instalado mediante el comando pip

```bash
  selenium --version
```

### Agregar libreria de reportes 
Agregar la libreria: https://pypi.org/project/pytest-html/ para generar reportes en html, para este ejecutar el siguiente comando en la terminal

```
    pip install pytest-html
```

## Ejecutar los test desde la línea de comandos  
- Ingresar a la carpeta test
```
cd  Automatizacion-E2E/tests
```
- Ingresar a la terminal, ejecutar los test y generar el reporte en html:
```
pytest test_purchase.py --html=../results/results.html
```
- Ir a la carpet results y abrir el reporte "results.html" en el navegador para ver más información de los tests.


## 2. Proyecto de automatizacion APIS 
En este proyecto se aplican la automatización de APIS mediante Karate. Para aplicar los casos de prueba, utilizaremos el sitio web de prueba https://petstore.swagger.io, que proporciona un servidor de pruebas donde se realizar solicitudes GET, PUT, POST y DELETE.

## Requisitos previos
El proyecto está desarrollado en Java con Maven por lo que instalará el siguiente software:

-  [Oracle Java 8 SDK](https://www.oracle.com/java/technologies/)
- [Apache Maven](https://maven.apache.org/)
- Tu IDE favorito, como [Intellij IDEA](https://www.jetbrains.com/) para abrir el proyecto.  

## Ejecutar las pruebas localmente
- Ingresar a la carpeta raíz y luego ir a la carpeta Automatizacion-Apis
```
cd Proyecto-Apis
```
- Ingresar a la terminal el siguiente comando:
```
mvn clean install
```
- Ingresar a la terminal y ejecutar los features:
```
mvn clean test -Dtest=KarateRunnerTest
```
- Ir a la carpeta de reportes:
```
cd target/karate-reports
```
- Ingresar a la terminal y abrir el reporte
```
start karate-summary.html
```