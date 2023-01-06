print("Hola mundo!! Soy Jose Hurtado Baeza :)")
print("Hola mundo 1!!")

# Soy un comentario
print("Hola mundo 2!!")

"""
Texto que no se va a interpretar
Texto que no se va a interpretar
Texto que no se va a interpretar
"""

# Variables
texto = "Repaso de Python con Victor"
nombre = "Jose Hurtado Baeza"
altura = "193cm"
year = 2023

#print(texto)
print(f"{texto} - {nombre} - {altura} - {year}")
print(texto + " - " + nombre + " - " + altura + " - " + str(year))

# Entrada
sitioweb = input("¿Cuál es tu página web?: ")
print("El sitio web del usuario es: " + sitioweb)

# Condiciones
"""
altura = int(input("¿Cuál es tu altura?: "))

if altura >= 180:
    print("Eres una persona alta!!")
else:
    print("Eres BAJITO!!")
"""

# Funciones

var_altura = int(input("¿Cuál es tu altura?: "))

def mostrarAltura(altura):

    resultado = ""

    if altura >= 180:
        resultado = "Eres una persona alta!!"
    else:
        resultado = "Eres BAJITO!!"
    
    return resultado

print(mostrarAltura(var_altura))

# Listas
personas = ["Jose", "Paco", "Pepe"]
print(personas[0])

for persona in personas:
    print("-" + persona)