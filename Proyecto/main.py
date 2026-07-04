import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from funciones import *

last_result = [""]
def run_analizar_fort():
    password = entry_input.get()
    if validar_entrada(password):
        result = analizar_fort(password)
        label_result.config(text="Resultado:\n" + result)
        last_result[0] = result
    else:
        messagebox.showwarning("Error", "Ingrese una contraseña valida")

def run_detectar_patrones():
    password = entry_input.get()
    if validar_entrada(password):
        result = detectar_patrones(password)
        label_result.config(text="Resultado:\n" + result)
        last_result[0] = result
    else:
        messagebox.showwarning("Error", "Ingrese una contraseña valida")

def run_generar_contrasenna():
    try:
        length = int(entry_input.get())
        result = generar_contrasenna(length)
        label_result.config(text="Contraseña Generada:\n" + result)
        last_result[0] = result
    except:
        messagebox.showwarning("Error", "Ingrese un número válido")

def run_generar_hash():
    text = entry_input.get()
    algoritmo = algo_var.get()
    if validar_entrada(text):
        result = generar_hash(text, algoritmo)
        label_result.config(text=f"Hash ({algoritmo.upper()}):\n" + result)
        last_result[0] = result
    else:
        messagebox.showwarning("Error", "Ingrese un texto valido")

def run_guardar_resultado():
    if last_result[0] == "":
        messagebox.showwarning("Error", "No hay resultados aún")
    else:
        guardar_resultado(last_result[0])
        messagebox.showinfo("Guardado", "Resultado guardado en resultado.txt")


window = tk.Tk()
window.title("Analizador de Contraseñas y Hashes")
window.geometry("560x600")
window.resizable(False, False)
window.config(bg="#121212")

style = ttk.Style()
style.theme_use("clam")
style.configure("TMenubutton", background="#333", foreground="white", font=("Segoe UI", 10), arrowcolor="#00FF66")
style.map("TMenubutton", background=[("active", "#444")])

def on_enter(e):
    e.widget['background'] = '#00FF66'
    e.widget['foreground'] = '#121212'

def on_leave(e):
    e.widget['background'] = '#1f1f1f'
    e.widget['foreground'] = '#00FF66'

# Título
title_label = tk.Label(window, text="🔒 Analizador de Seguridad 🔒", font=("Segoe UI", 16, "bold"), bg="#121212", fg="#00FF66")
title_label.pack(pady=(20,10))

input_frame = tk.Frame(window, bg="#1e1e1e", bd=2, relief="raised")
input_frame.pack(pady=10, padx=20, fill="x")
tk.Label(input_frame, text="Entrada de texto o longitud:", font=("Segoe UI", 11, "bold"), bg="#1e1e1e", fg="#cccccc").pack(pady=(10,4))
entry_input = tk.Entry(input_frame, width=40, font=("Segoe UI", 12), bg="#2a2a2a", fg="white", insertbackground="white", bd=0, highlightthickness=1, highlightbackground="#444", highlightcolor="#00FF66")
entry_input.pack(pady=4, padx=10, ipady=4)

algo_frame = tk.Frame(window, bg="#121212")
algo_frame.pack(pady=8)
tk.Label(algo_frame, text="Algoritmo Hash:", font=("Segoe UI", 11), bg="#121212", fg="#ffffff").pack(side="left", padx=8)
algo_var = tk.StringVar(value="sha256")
algo_menu = ttk.OptionMenu(algo_frame, algo_var, "sha256", "md5", "sha1", "sha256", "sha512")
algo_menu.pack(side="left")

buttons_frame = tk.Frame(window, bg="#121212")
buttons_frame.pack(pady=15)

def boton(text, command):
    btn = tk.Button(buttons_frame, text=text, command=command, font=("Segoe UI", 11, "bold"),
                    bg="#1f1f1f", fg="#00FF66", activebackground="#00FF66", activeforeground="#121212",
                    bd=1, relief="groove", width=24, cursor="hand2")
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)
    return btn

btn1 = boton("Analizar Fortaleza", run_analizar_fort)
btn2 = boton("Detectar Patrones", run_detectar_patrones)
btn3 = boton("Generar Contraseña", run_generar_contrasenna)
btn4 = boton("Generar Hash", run_generar_hash)

btn1.pack(pady=6, ipady=4)
btn2.pack(pady=6, ipady=4)
btn3.pack(pady=6, ipady=4)
btn4.pack(pady=6, ipady=4)

# Guardar resultado
btn_save = tk.Button(buttons_frame, text="Guardar Último Resultado", command=run_guardar_resultado,
                     font=("Segoe UI", 11, "bold"), bg="#00BFFF", fg="#121212",
                     activebackground="#009ACD", activeforeground="#fff", bd=0, width=24, cursor="hand2")
btn_save.bind("<Enter>", on_enter)
btn_save.bind("<Leave>", on_leave)
btn_save.pack(pady=(12,4), ipady=4)

result_frame = tk.Frame(window, bg="#2a2a2a", bd=2, relief="raised")
result_frame.pack(pady=15, padx=20, fill="both", expand=True)
label_result = tk.Label(result_frame, text="Resultado", bg="#2a2a2a", fg="#00FF66", font=("Consolas", 11), wraplength=480, justify="center")
label_result.pack(padx=10, pady=10, fill="both", expand=True)
window.mainloop()