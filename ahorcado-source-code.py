import tkinter as tk
import random

palabras = ['Nvidia', 'Google', 'Microsoft', 'AMD', 'Intel', 'Apple', 'Samsung', 'Sony', 'Dell', 'HP', 'Python', 'Javascript', 'Java', 'Minecraft', 'Linux', 'Obs studio']
intentos_iniciales = 3
victorias = 0
derrotas = 0

def iniciar_juego():
    global palabra_secreta, letras_adivinadas, intentos
    palabra_secreta = random.choice(palabras).upper()
    letras_adivinadas = set()
    intentos = intentos_iniciales
    label_palabra.config(text="_ " * len(palabra_secreta))
    label_intentos.config(text=f"Intentos restantes: {intentos}")
    label_mensaje.config(text="")
    boton_adivinar.config(state="normal")

def actualizar_palabra():
    estado = ' '.join([ch if ch in letras_adivinadas else '_' for ch in palabra_secreta])
    label_palabra.config(text=estado)

def adivinar_letra():
    global intentos, victorias, derrotas
    letra = entrada_letra.get().strip().upper()
    entrada_letra.delete(0, tk.END)

    if letra == "SONIC":
        letras_disponibles = [ch for ch in palabra_secreta if ch not in letras_adivinadas]
        if letras_disponibles:
            letra_revelada = random.choice(letras_disponibles)
            letras_adivinadas.add(letra_revelada)
            label_mensaje.config(text=f"Letra revelada: {letra_revelada}")
        else:
            label_mensaje.config(text="No hay letras para revelar.")
        actualizar_palabra()
        return

    if len(letra) != 1 or not letra.isalpha():
        label_mensaje.config(text="Por favor, ingresa solo una letra.")
        return

    if letra in letras_adivinadas:
        label_mensaje.config(text="Ya adivinaste esa letra.")
        return

    letras_adivinadas.add(letra)

    if letra in palabra_secreta:
        label_mensaje.config(text="¡Bien! La letra está en la palabra.")
    else:
        intentos -= 1
        label_mensaje.config(text="La letra no está en la palabra.")

    actualizar_palabra()
    label_intentos.config(text=f"Intentos restantes: {intentos}")

    if all(ch in letras_adivinadas for ch in palabra_secreta):
        label_mensaje.config(text=f"¡Felicidades! Has adivinado la palabra: {palabra_secreta}")
        boton_adivinar.config(state="disabled")
        victorias += 1
        label_victorias.config(text=f"Victorias: {victorias}")
    elif intentos <= 0:
        label_mensaje.config(text=f"Has perdido. La palabra era: {palabra_secreta}")
        boton_adivinar.config(state="disabled")
        derrotas += 1
        label_derrotas.config(text=f"Derrotas: {derrotas}")

root = tk.Tk()
root.title("Ahorcado")
root.geometry("500x400")
root.config(bg="#1e1e1e")

top_frame = tk.Frame(root, bg="#1e1e1e")
top_frame.pack(pady=20)

label_titulo = tk.Label(top_frame, text="Juego del Ahorcado", font=("Comic Sans MS", 24, "bold"), fg="#00ff00", bg="#1e1e1e")
label_titulo.pack(pady=10)

credits = tk.Label(top_frame, text="Desarrollado por Juasof14", font=("Helvetica", 5), fg="white", bg="#1e1e1e")
credits.place(relx=1.0, rely=1.0, anchor="se")

label_palabra = tk.Label(top_frame, text="", font=("Arial", 20), fg="white", bg="#1e1e1e")
label_palabra.pack(pady=5)

label_intentos = tk.Label(top_frame, text="", font=("Arial", 14), fg="red", bg="#1e1e1e")
label_intentos.pack(pady=5)

label_mensaje = tk.Label(top_frame, text="", font=("Arial", 12), fg="#ffff00", bg="#1e1e1e")
label_mensaje.pack(pady=5)

stats_frame = tk.Frame(root, bg="#1e1e1e")
stats_frame.pack(pady=5)
label_victorias = tk.Label(stats_frame, text=f"Victorias: {victorias}", font=("Arial", 12), fg="lime", bg="#1e1e1e")
label_victorias.pack(side="left", padx=10)
label_derrotas = tk.Label(stats_frame, text=f"Derrotas: {derrotas}", font=("Arial", 12), fg="red", bg="#1e1e1e")
label_derrotas.pack(side="left", padx=10)

bottom_frame = tk.Frame(root, bg="#1e1e1e")
bottom_frame.pack(pady=20)

entrada_letra = tk.Entry(bottom_frame, font=("Arial", 14))
entrada_letra.pack(side="left", padx=5)

boton_adivinar = tk.Button(bottom_frame, text="Adivinar", command=adivinar_letra)
boton_adivinar.pack(side="left", padx=5)

boton_reintentar = tk.Button(bottom_frame, text="Reintentar", command=iniciar_juego)
boton_reintentar.pack(side="left", padx=5)

iniciar_juego()

root.mainloop()
