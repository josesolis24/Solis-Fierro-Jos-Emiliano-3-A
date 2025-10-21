import tkinter as tk
from tkinter import messagebox

class DashboardApp:
    def __init__(self, username):
        self.username = username
        self.root = tk.Tk()
        self.root.title(f"Bienvenido {username}")
        self.root.geometry("600x400")
        self.crear_elementos()
        self.root.mainloop()
        

    def crear_elementos(self):
        tk.Label(self.root, text=f"Hola {self.username}", font=("Arial", 22, "bold")).pack(pady=10)
        
        tk.Button(self.root, text="Ver usuario", command=self.login).pack(pady=10)
        tk.Button(self.root, text="Agregar usuario", command=self.login).pack(pady=10)
        tk.Button(self.root, text="Actualizar usuario", command=self.login).pack(pady=10)
        tk.Button(self.root, text="Eliminar usuario", command=self.login).pack(pady=10)
        tk.Button(self.root, text="Cerrar sesión", command=self.root.destroy).pack(pady=20)


    def ver_usuario(self):
       messagebox.showinfo("Lista de usuario")

    def agragar_usuario(self):
       messagebox.showinfo("Agreagar  usuario",  "Funcion")

    def Eliminar_usuario(self):
       messagebox.showinfo("Elinmiar usuario" "Funcion")

    def Cerrar_sesion(self):
       self.root.destroy()
if __name__ == "__main__":
        App = DashboardApp("")