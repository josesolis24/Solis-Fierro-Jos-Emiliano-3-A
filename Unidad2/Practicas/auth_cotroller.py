# Controlador encargado de la lógica de autenticación
# Separa la lógica del login para mantener limpia la interfaz

from database import crear_conexion

def validar_credenciales(usuario, password):
    conexion = crear_conexion()

    if not conexion:
        return False

    cursor = conexion.cursor()
    consulta = "SELECT * FROM usuarios WHERE usuario = %s AND password = %s"
    cursor.execute(consulta, (usuario, password))
    resultado = cursor.fetchone()

    cursor.close()
    conexion.close()

    if resultado:
        return True
    else:
        return False
