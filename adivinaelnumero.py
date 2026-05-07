import random

rangos = {
    "facil": 50,
    "medio": 100,
    "dificil": 200
}

jugar = True
None = 0

while True:
    dificultad = input("Elige la dificultad: (Facil: 50, Medio: 100, Dificil: 200): ").lower().strip()
    rango = rangos.get(dificultad, 100)
    numero_aleatorio = random.randint(1, rango)
    intentos = 0
    encontrado = False

    while not encontrado:
        while True:
            try:
                numero = int(input("Introduce un número: "))
                break
            except ValueError:
                print("Por favor, introduce un número válido.")
                
        intentos += 1
        if numero > numero_aleatorio:
            print("El número introducido es mayor que el número secreto.")
        elif numero < numero_aleatorio:
            print("El número introducido es menor que el número secreto.")
        else:
            print("¡Has adivinado el número!")
            encontrado = True
            print(f"Has necesitado {intentos} intentos.")
        
        if not encontrado:
            diferencia = abs(numero - numero_aleatorio)
            if diferencia > 40:
                print("❄️ Muy frío")
            elif diferencia > 20:
                print("🌬️ Frío")
            elif diferencia > 10:
                print("🔥 Caliente")
            else:
                print("💥 Muy caliente")

    if intentos <= 5:
        print("Puntuación + 100")
    elif intentos <= 10:
        print("Puntuación + 50")
    else:
        print("Puntuación + 30")

    if record is None or intentos < record:
        record = intentos
        print("🏆 ¡Nuevo récord!")
    else:
        print(f"Tu récord actual es de {record} intentos.")

    respuesta = input("¿Quieres jugar de nuevo? (s/n): ").lower().strip()
    if respuesta == 'n':
        print("¡Gracias por jugar!")
        break