# Proyecto Cajero Automático - Registro de Clientes y Login

Este proyecto simula un sistema básico de registro de clientes y login en un cajero automático. El sistema permite registrar clientes con un código de tarjeta y un pin, y luego autenticar a los clientes mediante su código de tarjeta y pin en un proceso de login.

## Requerimientos

El programa realiza las siguientes funcionalidades:

1. Registrar una cantidad de clientes determinada por el usuario.
2. Permitir que los clientes se autentiquen mediante su código de tarjeta y pin.
3. Limitar los intentos de login a 3, con mensaje de error si se excede el límite de intentos.

## Descripción del Código

1. **Registro de Clientes**:

   - Se solicita al usuario que ingrese los datos básicos de cada cliente, como nombre, apellidos, celular, email, código de tarjeta y pin.
   - Los datos de cada cliente se almacenan en una lista de diccionarios (`clientes`), donde cada cliente tiene un identificador único (`id`), saldo inicial de 0 y un historial vacío.

2. **Login**:
   - El usuario puede intentar ingresar sus datos de login (código de tarjeta y pin) hasta 3 veces.
   - Si los datos coinciden con los registros de algún cliente, el login es exitoso y se muestra un mensaje de bienvenida.
   - Si el usuario excede los 3 intentos fallidos, el programa termina mostrando un mensaje de error.

## Flujo del Programa

1. El programa solicita cuántos clientes desea registrar.
2. Luego, para cada cliente, se piden los siguientes datos:
   - Nombre
   - Apellidos
   - Celular
   - Email
   - Código de tarjeta
   - Pin
3. Después de registrar a todos los clientes, el programa permite al usuario realizar un login ingresando su código de tarjeta y pin.
4. Si el login es exitoso, se muestra un mensaje de bienvenida con el nombre del cliente.
5. Si se exceden 3 intentos fallidos de login, el programa termina y muestra un mensaje de error.

### Cómo ejecutar

1. Clona el repositorio o descarga el archivo `main.py`.
2. Ejecuta el archivo Python usando tu interprete (se recomienda usar Python 3).

```bash
  python main.py
```
