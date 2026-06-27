import tkinter as tk
from tkinter import messagebox
from funciones import *

last_result = [""]

def run_analizar_fort():
    password = entry_input.get()
    if validar_entrada(password):
        result = analizar_fort(password)
        label_result.config(text="Resultado: " + result)
        last_result[0] = result
    else:
        messagebox.showwarning("Error", "Ingrese una contraseña")

def run_detectar_patrones():
    password = entry_input.get()
    if validar_entrada(password):
        result = detectar_patrones(password)
        label_result.config(text="Resultado: " + result)
        last_result[0] = result
    else:
        messagebox.showwarning("Error", "Ingrese una contraseña")

def run_generar_contrasenna():
    try:
        length = int(entry_input.get())
        result = generar_contrasenna(length)
        label_result.config(text="Generada: " + result)
        last_result[0] = result
    except:
        messagebox.showwarning("Error", "Ingrese un número válido")

def run_generar_hash():
    text = entry_input.get()
    algoritmo = algo_var.get()
    if validar_entrada(text):
        result = generar_hash(text, algoritmo)
        label_result.config(text="Hash: " + result)
        last_result[0] = result
    else:
        messagebox.showwarning("Error", "Ingrese un texto")

def run_guardar_resultado():
    if last_result[0] == "":
        messagebox.showwarning("Error", "No hay resultados aún")
    else:
        guardar_resultado(last_result[0])
        messagebox.showinfo("Guardado", "Resultado guardado en resultado.txt")

# Ventana principal
window = tk.Tk()
window.title("Analizador de Contraseñas y Hashes")
window.geometry("500x420")
window.config(bg="#1e1e1e")

# Título
tk.Label(window, text="Analizador de Contraseñas y Hashes",
         font=("Arial", 14, "bold"),
         bg="#1e1e1e", fg="white").pack(pady=10)

# Input
tk.Label(window, text="Ingrese contraseña o número:",
         bg="#1e1e1e", fg="white").pack()
entry_input = tk.Entry(window, width=40, font=("Arial", 12))
entry_input.pack(pady=5)

# Selector de algoritmo
tk.Label(window, text="Algoritmo:", bg="#1e1e1e", fg="white").pack()
algo_var = tk.StringVar(value="sha256")
tk.OptionMenu(window, algo_var, "md5", "sha1", "sha256", "sha512").pack(pady=5)

# Botones
btn = {"width": 30, "bg": "#4CAF50", "fg": "white", "font": ("Arial", 10)}

tk.Button(window, text="Analizar Fortaleza",
          command=run_analizar_fort, **btn).pack(pady=3)
tk.Button(window, text="Detectar Patrones Comunes",
          command=run_detectar_patrones, **btn).pack(pady=3)
tk.Button(window, text="Generar Contraseña (ingrese longitud)",
          command=run_generar_contrasenna, **btn).pack(pady=3)
tk.Button(window, text="Generar Hash",
          command=run_generar_hash, **btn).pack(pady=3)
tk.Button(window, text="Guardar Último Resultado",
          command=run_guardar_resultado,
          width=30, bg="#2196F3", fg="white", font=("Arial", 10)).pack(pady=3)

# Resultado
label_result = tk.Label(window, text="El resultado aparecerá aquí",
                        bg="#1e1e1e", fg="#4CAF50",
                        font=("Arial", 11), wraplength=450)
label_result.pack(pady=15)
window.mainloop()