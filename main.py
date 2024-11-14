clientes = []

num_clientes = int(input("Número de clientes a registrar: "))

for i in range(num_clientes):
    print(f"Registrando cliente {i + 1}")
    nombres = input("Ingrese su nombre: ")
    apellidos = input("Ingrese sus apellidos: ")
    celular = input("Ingrese su número de celular: ")
    email = input("Ingrese su email: ")
    code_card = input("Ingrese un código de tarjeta (único): ")
    pin = input("Ingrese un pin de 4 dígitos: ")

    cliente = {
        "id": i + 1,
        "nombres": nombres,
        "apellidos": apellidos,
        "celular": celular,
        "email": email,
        "code-card": code_card,
        "pin": pin,
        "saldo": 0,
        "historial": [],
    }

    clientes.append(cliente)
    print(f"Cliente {i + 1} registrado exitosamente.\n")


def login():
    intentos = 0
    while intentos < 3:
        print(f"Intento {intentos + 1} de 3")
        code_card = input("Introduzca su código de tarjeta: ")
        pin = input("Introduzca su pin: ")

        for cliente in clientes:
            if cliente["code-card"] == code_card and cliente["pin"] == pin:
                print(f"Bienvenido, {cliente['nombres']} {
                      cliente['apellidos']}!")
                return cliente

        print("Código de tarjeta o pin incorrectos.")
        intentos += 1

    print("Demasiados intentos fallidos. El programa se cerrará.")
    return


cliente_session = login()

if cliente_session is not None:
    print(f"Acceso permitido para el cliente {
          cliente_session['nombres']} {cliente_session['apellidos']}.")

else:
    print("Acceso denegado.")
