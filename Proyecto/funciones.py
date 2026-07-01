import hashlib
import string
import os
import secrets

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
    
def generar_hash(text, algoritmo):
    algoritmo = algoritmo.lower()
    if algoritmo == "md5":
        result = hashlib.md5(text.encode()).hexdigest()
    elif algoritmo == "sha1":
        result = hashlib.sha1(text.encode()).hexdigest()
    elif algoritmo == "sha256":
       result = hashlib.sha256(text.encode()).hexdigest()
    elif algoritmo == "sha512":
       result = hashlib.sha512(text.encode()).hexdigest()
    else:
        result = "Algoritmo no aceptado" 
        
    return result 
    
def detectar_patrones(password):
    patrones = ["123", "234", "345", "456", "567", "678", "789",
                "abc", "bcd", "cde", "def", "efg", "fgh",
                "aaa", "bbb", "ccc", "111", "222", "333",
                "password", "admin", "qwerty", "letmein"]
    for patron in patrones:
        if patron in password:
            return "Patrones detectados: " + patron
    return "No hay patrones en su contraseña"
        
def listar_algoritmos():
    algoritmos = ["md5", "sha1", "sha256", "sha512"]
    print("Available algorithms:")
    for algoritmos in algoritmos:
        print("- " + algoritmos)

def validar_entrada(text):
    if text.strip() == "":
        return False 
    return True    

def guardar_resultado(text):
 archivo = open("C:\\Users\\Personas Invitadas\\Desktop\\I-2026-Fundamentos-Phyton-SM\\Clase 06\\resultado.txt", "a")
 archivo.write(text + "\n")
 archivo.close()
 print ("Resultados guardados con exito")

def generar_contrasenna(length):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasenna = ""
    for i in range(length):
        contrasenna += secrets.choice(caracteres)
    return contrasenna
    
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
