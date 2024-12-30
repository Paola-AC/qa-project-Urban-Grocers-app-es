# Proyecto Urban Grocers 

# Proyecto de Pruebas de API - Creación de Kits para Usuarios

Este proyecto tiene como objetivo realizar pruebas sobre la creación //
de kits para un usuario en una API, en especial el campo "name".
 

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

