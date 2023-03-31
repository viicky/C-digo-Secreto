import random

# Palabras disponibles para adivinar
palabras = ['gato', 'perro', 'elefante', 'jirafa', 'león', 'tigre', 'cocodrilo', 'pingüino', 'mono', 'rinoceronte']

def obtener_palabra():
    # Obtener una palabra aleatoria de la lista de palabras
    palabra = random.choice(palabras)
    return palabra

def jugar_ahorcado():
    print("¡Bienvenido al juego del ahorcado!")
    palabra = obtener_palabra()
    letras_adivinadas = []
    intentos = 6
    
    while intentos > 0:
        # Mostrar la palabra con las letras adivinadas hasta el momento
        palabra_mostrada = ""
        for letra in palabra:
            if letra in letras_adivinadas:
                palabra_mostrada += letra
            else:
                palabra_mostrada += "_"
        print(palabra_mostrada)
        
        # Pedir al usuario que ingrese una letra
        letra_ingresada = input("Ingresa una letra: ")
        if letra_ingresada in palabra:
            letras_adivinadas.append(letra_ingresada)
            print("¡Correcto!")
        else:
            intentos -= 1
            print("Incorrecto. Te quedan", intentos, "intentos.")
            
        # Verificar si el usuario ha adivinado todas las letras
        if set(palabra) == set(letras_adivinadas):
            print("¡Felicidades, has adivinado la palabra! La palabra era:", palabra)
            return
        
    print("¡Lo siento, has perdido! La palabra era:", palabra)

jugar_ahorcado()
