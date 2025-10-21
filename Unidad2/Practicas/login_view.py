import tkinter as tk
from tkinter import messagebox
from auth_cotroller import validar_credenciales

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Inicio de sesión")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        # Encabezado
        tk.Label(root, text="Bienvenido al sistema", font=("Arial", 16, "bold")).pack(pady=16)

        # Campos de texto
        tk.Label(root, text="Ingrese su nombre de usuario:").pack()
        self.username_entry = tk.Entry(root)
        self.username_entry.pack(pady=5)

        tk.Label(root, text="Ingrese su contraseña:").pack()
        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.pack(pady=5)

        tk.Button(root, text="Iniciar sesión", command=self.login).pack(pady=20)

    def login(self):
        usuario = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        if not usuario or not password:
            messagebox.showerror("Faltan datos", "Por favor ingrese usuario y contraseña.")
            return

        if validar_credenciales(usuario, password):
            messagebox.showinfo("Acceso permitido", f"Bienvenido {usuario}")
            self.root.destroy()
        else:
            messagebox.showerror("Acceso denegado", "Tus datos son incorrectos")
