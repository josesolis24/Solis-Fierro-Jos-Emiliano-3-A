import mysql.connector
from mysql.connector import Error

def crear_conexion():
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            user='root',       # tu usuario de MySQL
            password='',       # tu contraseña (si tienes una, escríbela aquí)
            database='POO_project_P2'  # el nombre de tu base de datos
        )

        if conexion.is_connected():
            print("✅ Conexión MySQL exitosa")
            return conexion
    except Error as e:
        print(f"❌ Error al conectar a MySQL: {e}")
        return None


# 🔹 PRUEBA DIRECTA DE CONEXIÓN 🔹
if __name__ == "__main__":
    conexion = crear_conexion()
    if conexion:
        print("✅ Se estableció la conexión correctamente.")
        conexion.close()
        print("🔒 Conexión cerrada.")
    else:
        print("⚠️ No se pudo conectar a la base de datos.")


