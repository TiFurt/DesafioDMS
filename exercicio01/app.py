from conversor import Conversor
from time import sleep

while True:
    try:
        print('''
        -=-=-=-=-=-=-=-=-=-=-=-
              Conversor
        -=-=-=-=-=-=-=-=-=-=-=-''')
        medida = float(input('Digite a quantidade que deseja converter:(digite 0 para sair)'))
        if medida == 0:
            break
        print(
            """
                UNIDADE DE MEDIDA
            [1] - Milha
            [2] - Polegada
            [3] - Pé
            [4] - Centímetro
            [5] - Metro
            [6] - Quilômetro
            [0] - SAIR
            """)
        escolha = int(input('Qual a unidade de medida?'))
        if 1 <= escolha <= 6:
            if __name__ == "__main__":
                conversor = Conversor(medida, escolha)
                print(f'{conversor.medida():.2f} {conversor.uni_medida()} = {conversor.milha()} milha(s)\n'
                      f'{conversor.medida():.2f} {conversor.uni_medida()} = {conversor.polegada()} polegada(s)\n'
                      f'{conversor.medida():.2f} {conversor.uni_medida()} = {conversor.pe()} pe(s)\n'
                      f'{conversor.medida():.2f} {conversor.uni_medida()} = {conversor.centimetro()} centímetro(s)\n'
                      f'{conversor.medida():.2f} {conversor.uni_medida()} = {conversor.metro()} metro(s)\n'
                      f'{conversor.medida():.2f} {conversor.uni_medida()} = {conversor.quilometro()} quilometro(s)')
        elif escolha == 0:
            break
        else:
            print('Opção Inválida!')
        sleep(2)
    except ValueError:
        print('Digite um valor válido!')
