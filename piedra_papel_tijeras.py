import random


def evaluarJuego(opcionJugador, opcionMaquina, opcion):
    print ("Elegiste: " + str(opcionJugador))
    print ("maquina eligio: " + str(opcionMaquina))

    if opcion == 1:
        maq1, maq2 = 2, 3
    elif opcion == 2:
        maq1, maq2 = 3, 1
    elif opcion == 3:
        maq1, maq2 = 1, 2

    if opcionJugador == opcionMaquina:
        print('Empataste con la maquina')
    elif opcionMaquina == maq1:
        print('Perdiste jajajajaja')
    elif opcionMaquina == maq2:
        print('Ganaste uuuuhhhhh')


def run():
    menu = """
    Elige una opción:
    1 - Piedra
    2 - Papel
    3 - Tijeras
    """
    print(menu)

    try:
        opcionJugador1 = int(input('Dime tu opción: '))
        piedra, papel, tijeras = 1, 2, 3
        opcionMaquina = random.randint(1, 3)

        if opcionJugador1 == piedra:
            evaluarJuego(opcionJugador1, opcionMaquina, piedra)
        elif opcionJugador1 == papel:
            evaluarJuego(opcionJugador1, opcionMaquina, papel)
        elif opcionJugador1 == tijeras:
            evaluarJuego(opcionJugador1, opcionMaquina, tijeras)
        else:
            print("Elige una de las opciones del menu")
    except ValueError:
        print("Elige una de las opciones del menu")


if __name__ == '__main__':
    run()