# ToDoEr

Requerimientos
--------------

#### Python y MySQL
Este sistema requiere python 2.7 y pip para ejecutarse. Se asume que ya
tiene python en esta versión y pip instalado en su equipo. De no ser así
busque un instructivo en python.org sobre como instalar estos requerimientos
en su sistema.

MySQL server también es requerido en su versión 5.6.x. Instalelo siguiendo las
instrucciones que se encuentran en el sitio del desarrollador del producto en
caso de aún no tenerlo instalado.

#### Librerias

Se utilizará *pip* para instalar las dependencias de código. Se requieren las
siguientes librerias

```
pip install Flask pony gunicorn
```

Note que pueden ser necesarios privilegios de administrador para que la instalación
sea exitosa.

Corriendo el sistema
--------------------

Abra una terminal y ejecute el siguiente comando

```
./start_server
```

Si desea detener el servidor, presione `Ctrl+C` en la terminal.


Modificando parametros del proyecto
-----------------------------------

Puede ser necesario modificar los parametros con los que inicia la aplicación, tal como la base de datos inicial, o el puerto en el que corre. Para ello dispone del
archivo `config.ini` en la carpeta `src`.

Agregando entidades al proyecto
-------------------------------

Si agrega una nueva entidad al proyecto recuerde agregar su import correspondiente
en `src/models/__init__.py`.
