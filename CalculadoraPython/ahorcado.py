import random

palabras = ['Nvidia', 'Google', 'Microsoft', 'AMD', 'Intel', 'Apple', 'Samsung', 'Sony', 'Dell', 'HP']
palabra_secreta = random.choice(palabras).upper()
letras_adivinadas = set()
intentos = 3

victorias = 0
derrotas = 0
gano = False

print("Juego del Ahorcado")
while intentos > 0:
    estado_palabra = ''.join([letra if letra in letras_adivinadas else '_' for letra in palabra_secreta])
    print(f"Palabra: {estado_palabra}")
    print(f"Intentos restantes: {intentos}")
    
    letra = input("Adivina una letra: ").strip().upper()
    
    if len(letra) != 1 or not letra.isalpha():
        print("Por favor, ingresa solo una letra.")
        continue
    
    if letra in letras_adivinadas:
        print("Ya has adivinado esa letra. Intenta con otra.")
        continue

    # Registrar la letra intentada
    letras_adivinadas.add(letra)

    if letra in palabra_secreta:
        print("¡Bien! La letra está en la palabra.")
        # Verificar si se adivinaron todas las letras
        if all(ch in letras_adivinadas for ch in palabra_secreta if ch.isalpha()):
            print(f"¡Felicidades! Has adivinado la palabra: {palabra_secreta}")
            gano = True
            break
    else:
        intentos -= 1
        print("La letra no está en la palabra.")
else:
    print(f"Has perdido. La palabra era: {palabra_secreta}")
    print("Mejor suerte la proxima.")
    gano = False

def reintentar():
    global intentos, letras_adivinadas, palabra_secreta, gano
    intentos = 3
    letras_adivinadas = set()
    palabra_secreta = random.choice(palabras).upper()
    gano = False
    print("Reiniciando el juego...")

# Actualizar estadísticas según el resultado de la partida
if gano:
    victorias += 1
else:
    derrotas += 1
print(f"Victorias: {victorias}, Derrotas: {derrotas}")