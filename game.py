import random


def run():
    numeroran = random.randint(1, 100)
    numeroele = int(input('Elige un número del 1 al 100: '))
    while numeroele != numeroran:
        if numeroele < numeroran:
            print('Busca un número más grande')
        else:
            print('Busca un número más pequeño')
        numeroele = int(input('Elige otro número:  '))
    print('¡Ganaste!')


if __name__ == '__main__':
    run()