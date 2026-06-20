import hashlib
import string
import os
import secrets
import random

#Funciones
def analizar_fort(password):
    score = 0
    if len(password) >= 8:
        score+= 1
    if len(password) >= 12:
        score+= 1
    if any(c.isupper() for c in password):
        score+= 1
    if any(c.islower() for c in password):
        score+= 1
    if any(c.isdigit() for c in password):
        score+= 1
    if score<= 2:
        return "Contraseña debil"
    elif score<= 3:
        return "Contraseña intermedia"
    else:
        return "Contraseña fuerte"
    
def generar_hash(text, algorithm):
    algorithm = algorithm.lower()
    
    if algorithm == "md5":
        result = hashlib.md5(text.encode()).hexdigest()
    elif algorithm == "sha1":
        result = hashlib.sha1(text.encode()).hexdigest()
    elif algorithm == "sha256":
       result = hashlib.sha256(text.encode()).hexdigest()
    elif algorithm == "sha512":
       result = hashlib.sha512(text.encode()).hexdigest()
    else:
        result = "Algoritmo no aceptado" 
        
    return result 
    
def detectar_patrones():
    pass
def listar_algoritmos():
    pass

def validar_entrada(text):
    if text.strip() == "":
        return False 
    return True    

def guardar_resultado():
    pass

def generar_contraseña(length):
    pass
    
def mostrar_menu():
    os.system("cls" if os.name == "nt" else "clear")
    print("="* 40)
    print(" Analizador de contraseñas y hashes  ")
    print("="* 40)
    print("1. Generar hashes")
    print("2. Analizar fortalezas")
    print("3. Generar contraseña segura")
    print("4. Guardar ultimo resultado")
    print("5. Verificar hash")
    print("6. Detectar patrones comunes")
    print("7. Salir")
    print("="* 40)
mostrar_menu()
print(generar_hash("olaa","sha512<"))
print(analizar_fort("hola12345"))