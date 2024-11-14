# Proyecto Cajero Automático - Registro de Clientes y Login

Este proyecto simula un cajero automático básico donde puedes registrar clientes, autenticarte con un código de tarjeta y PIN, y realizar operaciones como consultar saldo, retirar o depositar dinero.

## Requerimientos

Este programa ofrece las siguientes funcionalidades:

1. Registrar varios clientes, solicitando sus datos personales, código de tarjeta y PIN.
2. Permitir que los clientes se autentiquen con su código de tarjeta y PIN en un proceso de login.
3. Limitar los intentos de login a 3, mostrando un mensaje de error si se excede el límite.
4. Permitir al usuario realizar varias operaciones dentro del cajero automático una vez que haya iniciado sesión:
   - Consultar saldo.
   - Retirar dinero.
   - Depositar dinero.
   - Ver historial de transacciones.

## Descripción del Código

1. **Registrar Clientes**:
   - El programa pide el número de clientes a registrar y luego solicita los siguientes datos para cada cliente:
     - Nombre
     - Apellidos
     - Celular
     - Email
     - Código de tarjeta (debe ser único)
     - PIN (de  4 dígitos)
   - Los datos de cada cliente se almacenan en una lista (`clientes`), donde cada cliente tiene un identificador único (`id`), saldo inicial de 0 y un historial vacío.

2. **Login**:
   - El cliente se autentica ingresando su código de tarjeta y PIN.
   - El programa permite hasta 3 intentos fallidos antes de cerrarse.
   - Si el login es exitoso, se da la bienvenida al cliente y se permiten realizar operaciones.

3. **Operaciones**:
   - Una vez autenticado, el cliente puede realizar las siguientes operaciones:
     - Consultar su saldo.
     - Retirar dinero (si tiene saldo suficiente).
     - Depositar dinero (solo cantidades positivas).
     - Ver su historial de transacciones.
   - Las transacciones (depósitos y retiros) se registran en el historial de cada cliente.

## Flujo del Programa

1. El programa pide cuántos clientes registrarás.
2. Para cada cliente, solicita:
   - Nombre
   - Apellidos
   - Celular
   - Email
   - Código de tarjeta
   - PIN
3. Después de registrar a todos los clientes, el programa permite al usuario iniciar sesión ingresando su código de tarjeta y PIN.
4. Si el login es exitoso, el cliente puede realizar varias operaciones dentro del cajero.
5. Si se exceden 3 intentos fallidos, el programa finaliza con un mensaje de error.

## Cómo ejecutar el programa

1. Clona el repositorio o descarga el archivo `main.py`.
2. Ejecuta el archivo Python con tu intérprete de Python 3.

```bash
  python main.py
