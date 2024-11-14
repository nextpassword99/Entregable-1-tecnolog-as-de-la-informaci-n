import time

clientes = []


def registrar_clientes():
    num_clientes = int(input("Número de clientes a registrar: "))

    for i in range(num_clientes):
        print(f"Registro de cliente {i + 1}")
        nombres = input("Ingrese su nombre: ")
        apellidos = input("Ingrese sus apellidos: ")
        celular = input("Ingrese su número de celular: ")
        email = input("Ingrese su email: ")

        while True:
            code_card = input("Ingrese un código de tarjeta (único): ")
            if any(cliente['code-card'] == code_card for cliente in clientes):
                print(
                    "¡Error! Este código de tarjeta ya existe.")
            else:
                break

        while True:
            pin = input("Ingrese un pin de 4 dígitos: ")
            if len(pin) == 4 and pin.isdigit():
                break
            else:
                print("El PIN debe ser de 4 dígitos. Intente nuevamente.")

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
        print(f"Cliente {i + 1} registrado exitosamente.")


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

        print("Código de tarjeta o pin incorrectos. Intente nuevamente.")
        intentos += 1

    print("Demasiados intentos fallidos. El programa se cerrará.")
    return


def operaciones(cliente):
    while True:
        print("¿Qué desea hacer?")
        print("1. Consultar saldo")
        print("2. Retirar dinero")
        print("3. Depositar dinero")
        print("4. Ver historial de transacciones")
        print("5. Salir")

        opt = input("Seleccione una opción: ")

        if opt == "1":
            print(f"Su saldo actual es: ${cliente['saldo']}")

        elif opt == "2":
            cantidad = float(input("Ingrese la cantidad a retirar: "))
            if cantidad <= cliente['saldo']:
                cliente['saldo'] -= cantidad
                cliente['historial'].append(f"Retiro de ${cantidad}")
                print(f"Ha retirado ${cantidad}. Su saldo actual es: ${
                      cliente['saldo']}")
            else:
                print("Fondos insuficientes para realizar esta operación.")

        elif opt == "3":
            cantidad = float(input("Ingrese la cantidad a depositar: "))
            if cantidad > 0:
                cliente['saldo'] += cantidad
                cliente['historial'].append(f"Depósito de ${cantidad}")
                print(f"Ha depositado ${cantidad}. Su saldo actual es: ${
                      cliente['saldo']}")
            else:
                print("El depósito debe ser una cantidad positiva.")

        elif opt == "4":
            if cliente['historial']:
                print("Historial de transacciones:")
                for tsc in cliente['historial']:
                    print(tsc)
            else:
                print("No hay transacciones en su historial.")

        elif opt == "5":
            print("Gracias por utilizar el cajero automático. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intente nuevamente.")


def main():
    registrar_clientes()

    cliente_session = login()

    if cliente_session:
        print(f"Acceso permitido para el cliente {
              cliente_session['nombres']} {cliente_session['apellidos']}.")
        operaciones(cliente_session)
    else:
        print("Acceso denegado. El programa se cerrará.")


main()
