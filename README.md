
# Paola Alfonso_Cohort 19

# Proyecto Urban Grocers 

## Proyecto de Pruebas de API - Creación de Kits para Usuarios

Objetivo: El objetivo de este proyecto, es automizar las pruebas 
del proceso de creacion de un kit de productos en la aplicacion 
Urban Grocers. 

El proceso se enfocara especificamente en validar el campo "name"
en la solicitud de creacion de un kit, le cual consiste en crear
un usuario en la plataforma, obtener el token de autenticacion 
(authTojen), y utilizar este toekn para crear el kit asociado al
usuario. Posteriormente, se llvara a cabo la validacion del campo
"name" siguiendo la lista de comprobacion previamente definida.
Una vez completadas las pruebas, se cargara el codigo automatizado 
en Github y se enviara al repositorio.

## Archivos del Proyecto

- **configuration.py**: Contiene las rutas de la API.
- **data.py**: Contiene los cuerpos de solicitud.
- **sender_stand_request.py**: Realiza las solicitudes HTTP.
- **create_kit_name_kit_test.py**: Contiene las pruebas positivas y negativas del campo "name".
- **README.md**: Descripción del proyecto.
- **.gitignore**: Archivos ignorados por Git.

## Cómo Ejecutar las Pruebas

1. Asegúrate de tener Python 3.x y pytest instalados.
2. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```
3. Ejecuta las pruebas:
    ```bash
    pytest
    ```

## Notas

1. Algunas pruebas pueden fallar intencionalmente debido 
a restricciones de la API (por ejemplo, el límite de caracteres en el nombre).

3. Pruebas para el parámetro "name" al crear un Kit

Necesitas tener instalados los paquetes pytest y request para ejecutar las pruebas.
Ejecuta todas las pruebas con el comando pytest.

