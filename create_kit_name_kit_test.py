import sender_stand_request
import data

# Crear Usuario
def get_user_body(first_name):
    current_body = data.user_body.copy()     # Se cambia el valor del parámetro firstName
    current_body["firstName"] = first_name     # Se devuelve un nuevo diccionario con el valor firstName requerido
    return current_body


#  Crear un Kit
def get_kit_body(kit_body):
    current_body = data.kit_body.copy() # Se cambia el valor del parámetro Name
    current_body["name"] = kit_body # Se devuelve un nuevo diccionario con el valor Name requerido
    return current_body

def get_new_user_token():
    current_body = sender_stand_request.Auto_token
    return current_body

# FUNCION DE PRUEBA POSITIVA
def positive_assert(kit_body):
    user_body = get_kit_body(kit_body)
    authToken_kit = get_new_user_token()
    user_response = sender_stand_request.post_new_client_kit(user_body, authToken_kit)

    # Comprueba si el código de estado es 201
    assert user_response.status_code == 201
    # Comprueba que el campo authToken está en la respuesta y contiene un valor
    assert user_response.json() != ""

    # El resultado de la solicitud de recepción de datos de la tabla "user_model" se guarda en la variable "users_table_response"
    users_table_response = sender_stand_request.get_users_table()


    # Prueba 1. El número permitido de caracteres (1): kit_body = { "name": "a"}
def test_create_kit_2_letter_in_name_get_success_response():
    positive_assert("A")


    # Prueba 2. El número permitido de caracteres (511): kit_body = { "name":"El valor de prueba para esta comprobación será inferior a"}
def test_create_kit_511_letter_in_name_get_success_response():
    positive_assert("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc//"
                    "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab//"
                    "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda//"
                    "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcda//"
                    "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda//"
                    "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab//"
                    "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc//"
                    "dabcdabcdabcdabcdabcdabcdabcdabcdabC")

# FUNCION DE PRUEBA NEGATIVA
def negative_assert_code_400 (kit_body):
    user_body = get_kit_body(kit_body)
    authToken_kit = get_new_user_token()
    user_response = sender_stand_request.post_new_client_kit(user_body, authToken_kit)

    # Comprueba si el código de estado es 400
    assert user_response.status_code == 400
    # Comprueba que el campo authToken está en la respuesta y contiene un valor
    assert user_response.json()["code"] == 400

    # Comprueba si el atributo "message" en el cuerpo de respuesta se ve así:
    assert response.json()["message"] == "El nombre que ingresaste es incorrecto. " \
                                         "Los nombres solo pueden contener caracteres latinos,  " \
                                         "los nombres deben tener al menos 1 caracteres y no más de 511 caracteres"


    # Prueba 3. El número de caracteres es menor que la cantidad permitida (0): kit_body = { "name": "" }
def test_create_kit_No_letter_in_name_get_success_response():
    negative_assert_code_400("")


    # Prueba 4. 	El número de caracteres es mayor que la cantidad //
    # permitida (512): kit_body = { "name":"El valor de prueba para esta comprobación será inferior a” }
def test_create_kit_512_letter_in_name_get_success_response():
    negative_assert_code_400("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc//"
                             "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab//"
                             "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda//"
                             "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcd//"
                             "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd//"
                             "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd//"
                             "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd//"
                             "abcdabcdabcD")


    # Prueba 5. Se permiten caracteres especiales: kit_body = { "name": "№%@," }
def test_create_kit_caracters_letter_in_name_get_success_response():
    negative_assert_code_400("№%@,")


    # Prueba 6. Se permiten espacios: kit_body = { "name": " A Aaa " }
def test_create_kit_gaps_letter_in_name_get_success_response():
    negative_assert_code_400("A Aaa")


    # Prueba 7. Se permiten números: kit_body = { "name": "123" }
def test_create_kit_numbers_letter_in_name_get_success_response():
    negative_assert_code_400("123")

    # Prueba 8. El parámetro no se pasa en la solicitud: kit_body = { }
def test_create_kit_caracter_letter_in_name_get_success_response():
    negative_assert_code_400({ })

 # Prueba 9. Se ha pasado un tipo de parámetro diferente (número): kit_body = { "name": 123 }
def test_create_kit_fuction_letter_in_name_get_success_response():
    negative_assert_code_400({ "name": 123 })