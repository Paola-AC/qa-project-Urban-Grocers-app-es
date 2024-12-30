import configuration
import requests
import data

# Ejercicio_1. DOC_PATH - URL Completa de la documentacion
def get_docs():
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)

response = get_docs()
print(response.status_code)


# Ejercicio_2. LOG_MAIN_PATH - Utils → Logs del servidor principal.
def get_logs():
    return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH, params={"count": 20})

response = get_logs()
print(response.status_code)
print(response.headers)

# Ejercicio_3. Utils → USERS_TABLE_PATH - Recuperar información de la tabla de base de datos.
def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)

response = get_users_table()
print(response.status_code)


# TASK_1. CREATE_USER_PATH - Crear usuario
def post_new_kit(user_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=user_body,
                         headers=data.headers)

response = post_new_kit(data.user_body)
print(response.status_code)
print(response.json())


Bearer_token = response.json()
Auto_token = Bearer_token["authToken"]


# Task2. PRODUCTS_KITS_PATH  Crear un kit
def post_new_client_kit(kit_body, auth_token):
    header = data.headers.copy()
    header["Authorization"] =f"Bearer {auth_token}"
    print(header)

    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body,
                         headers=header )

response2 = post_new_client_kit(data.kit_body,Auto_token)
print(response2.status_code)
print(response2.json())



