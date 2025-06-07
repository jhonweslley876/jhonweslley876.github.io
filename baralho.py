import random
import time

valor = 100

while valor > 0:
    print(f'\nFichas totais: {valor}')
    valor2 = int(input('Digite o valor de entrada: '))
    if valor2 > valor:
        print('Fichas insuficientes.')
    else:
        valor -= valor2
        niquel = ['♥', '♦', '♣', '♠', '7']
        random.shuffle(niquel)
        random.shuffle(niquel)

        for c in range(50):
            simbolo1 = random.choice(niquel)
            simbolo2 = random.choice(niquel)
            simbolo3 = random.choice(niquel)
            print(f'\r{simbolo1}{simbolo2}{simbolo3}', end='    ', flush=True)
            time.sleep(0.05)

        if simbolo1 == simbolo2 == simbolo3:
            if simbolo1 == '7':
                print(f'\nParabéns, você ganhou {valor2 * 777}!')
                valor += valor2 * 777
                print(f'Valor atual: {valor}')
            elif simbolo1 == '♥':
                print(f'\nParabéns, você ganhou: {valor2 * 2}.')
                valor += valor2 * 2
                print(f'Valor atual: {valor}')
            elif simbolo1 == '♦':
                print(f'\nParabéns, você ganhou: {valor2 * 3}.')
                valor += valor2 * 3
                print(f'Valor atual: {valor}')
            elif simbolo1 == '♣':
                print(f'\nParabéns, você ganhou: {valor2 * 4}.')
                valor += valor2 * 4
                print(f'Valor atual: {valor}')
            elif simbolo1 == '♠':
                print(f'\nParabéns, você ganhou: {valor2 * 5}.')
                valor += valor2 * 5
                print(f'Valor atual: {valor}')
        if valor == 0:
            print('\nAs suas fichas acabaram!')