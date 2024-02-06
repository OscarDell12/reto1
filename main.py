def registrar_usuario():
    # Solicitar información al usuario
    nombres = input("Ingrese su(s) nombre(s): ")
    apellidos = input("Ingrese su(s) apellido(s): ")
    telefono = input("Ingrese su número de teléfono: ")
    correo = input("Ingrese su correo electrónico: ")

    # Mostrar mensaje de bienvenida
    print(f"\nHola {nombres} {apellidos}, en breve recibirás un correo a {correo}.")

# Llamar a la función para registrar al usuario
registrar_usuario()