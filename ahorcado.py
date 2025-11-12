import random

palabras = ['Nvidia', 'Google', 'Microsoft', 'AMD', 'Intel', 'Apple', 'Samsung', 'Sony', 'Dell', 'HP']
palabra_secreta = random.choice(palabras)
letras_adivinadas = []
intentos = 3

print("Juego del Ahorcado")
while intentos > 0:
    estado_palabra = ''.join([letra if letra in letras_adivinadas else '_' for letra in palabra_secreta])
    print(f"Palabra: {estado_palabra}")
    print(f"Intentos restantes: {intentos}")
    
    letra = input("Adivina una letra: ").strip()
    
    if len(letra) != 1 or not letra.isalpha():
        print("Por favor, ingresa solo una letra.")
        continue
    
    if letra in letras_adivinadas:
        print("Ya has adivinado esa letra. Intenta con otra.")
        continue
    
    letras_adivinadas.append(letra)
    
    if letra not in palabra_secreta:
        intentos -= 1
        print("Letra incorrecta.")
    
    if all(letra in letras_adivinadas for letra in palabra_secreta):
        print(f"¡Felicidades! Has adivinado la palabra: {palabra_secreta}")
        break
else:
    print(f"Has perdido. La palabra era: {palabra_secreta}")
    print("Mejor suerte la proxima.")

def reintentar():
    global intentos, letras_adivinadas, palabra_secreta
    intentos = 3
    letras_adivinadas = []
    palabra_secreta = random.choice(palabras)
    print("Reiniciando el juego...")
