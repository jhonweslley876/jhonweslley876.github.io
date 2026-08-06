from função_geral import *
import webbrowser

nome = login()
jogador = buscar_jogador(nome)
nível = jogador[2]

# carregamento inicial do jogo, regras e diálogos
carregamento()
escrever_texto('\nJogo carregado.')

time.sleep(2)
os.system('cls') # limpa o terminal para deixar a interface mais limpa
while True:
    tutorial = input('Ver tutorial? (s/n): ').lower()
    if tutorial == 's':
        regras()
        break
    elif tutorial == 'n':
        escrever_texto('Começando jogo...')
        print('')
        time.sleep(1)
        break
    else:
        print('Digite apenas "s" ou "n".')

dialogo()

cont = 1 # quant mago
força = False

player = 100 # vida do jogador
vida_mago = 100 # vida do mago
mana_player = 100 # mana do jogador
mana_mago = 100 # mana do mago

while player > 0 or vida_mago > 0: 

    magos(player, vida_mago, mana_player, mana_mago) # tabela de estatísticas dos jogadores

    baralho = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] * 4
    for c in range(10):
        random.shuffle(baralho) # embaralha aleatoriamente

    def formatar_carta(carta):
        if carta == 1:
            return 'A'
        if carta == 10:
            return random.choice(['K', 'Q', 'J'])
        return str(carta)

    cartas = [baralho.pop(), baralho.pop()] # cartas do jogador
    total = sum(cartas) # pontuação total do jogador

    tabela2 = '__________________________________________________'
    
    print(tabela2)
    print(f'Suas cartas são: {", ".join(formatar_carta(c) for c in cartas)}') # mostra as cartas
    print(f'Seu total é: {total}') # pontuação total do jogador

    while True:
        print(tabela2)
        print('┌───┬─────────┬───┬───────────┐')
        print('│ 1 │ comprar │ 2 │ finalizar │')
        print('└───┴─────────┴───┴───────────┘')
        compras = input('Digite a sua escolha:  ') # sistema de compra de cartas

        if compras == '1':
            if mana_player < 10: # se o jogador não tiver mana, para de comprar
                escrever_texto('Mana insuficiente para comprar cartas')
                time.sleep(1)
                break
            
            os.system('cls')
            print(tabela2)
            nova_carta = baralho.pop() #pega uma nova carta da lista e exclui ela da lista (igual um baralho normal)
            total += nova_carta
            cartas.append(nova_carta) # adiciona essa carta na sua mão
            mana_player -= 10

            print(f'Carta comprada: {formatar_carta(nova_carta)}.')
            print(f'Suas cartas: {", ".join(formatar_carta(c) for c in cartas)}.')
            print(f'Seu total é: {total}.')

            if total > 21:
                break

        elif compras == '2':
            os.system('cls')
            break

        else:
            os.system('cls')
            print(f'Suas cartas: {", ".join(formatar_carta(c) for c in cartas)}.')
            print(f'Seu total é: {total}.')
            escrever_texto('Digite apenas 1 para comprar ou 2 para finalizar!')

    print('__________________________________________________')

    if total == 21:
        print('Parabéns, você ganhou!')
        escrever_texto('Dano crítico por valor 21!')

        if força == True:
            for c in range(30):
                dano = random.randint(5, 30)
                print(f'\r{dano} ATK', end=' ', flush=True)
                time.sleep(0.1)

        else:
            for i in range(30): # sistema de dano
                dano = random.randint(1, 20) # escolhe aleatóriamente entre 1 e 20
                print(f'\r{dano} ATK', end=' ', flush=True) # imprime a variável na mesma linha apagando a mensagem anterior
                time.sleep(0.1)

        print(f'\nVocê: {dano} + 10 ATK')
        escrever_texto(f'\nMago sofreu {dano + 10} de dano.')
        os.system('cls')

        dano_mago(player, vida_mago, mana_player, mana_mago, total, dano + 1)
        vida_mago -= dano + 10

    else:
        os.system('cls')

        print('__________________________________________________')
        cartas_bot = [baralho.pop(), baralho.pop()]
        mago_total = sum(cartas_bot)

        print(f'Mago: {", ".join(formatar_carta(c) for c in cartas_bot)}')
        print(f'Mago: {mago_total}')

        while mago_total < 16:
            if mana_mago < 10:
                break

            nova_carta = baralho.pop()
            cartas_bot.append(nova_carta)
            mago_total += nova_carta
            mana_mago -= 10
            print(f'Bot 1 comprou: {formatar_carta(nova_carta)}')

            os.system('cls')
            print(f'Cartas do mago: {", ".join(formatar_carta(c) for c in cartas_bot)}')
            print(tabela2)

            escrever_texto(f'Valor total do mago: {mago_total}')
            print(tabela2)

            print(f'Seu total: {total}')
            print('__________________________________________________')

        if total > 21 and mago_total > 21:
            escrever_texto("ambos estouraram, passaram de 21 pontos.")
            mensagem = '-10 de HP e MANA para ambos'
            escrever_texto_na_caixa(mensagem, largura=40, velocidade=0.04)
            time.sleep(1)

            dano = 10
            os.system('cls')

            estouro_player(player, vida_mago, mana_player, mana_mago, dano)
            mana_player -= 10
            player -= 10
            
            estouro_mago(player, vida_mago, mana_player, mana_mago, dano)
            vida_mago -= 10
            mana_mago -= 10

        elif total > 21:
            os.system('cls')
            print('__________________________________________________')
            print(f'Você perdeu. Seu total de pontos é {total}.')
            print(tabela2)

            if mago_total == 21:
                print('Mago ganhou com 21!')
                print('Dano crítico por valor 21.')
                print('__________________________________________________')
                for i in range(30):
                    dano = random.randint(1, 20)
                    print(f'\r{dano} ATK', end=' ', flush=True)
                    time.sleep(0.1)
                print(f'\n{dano} + 10 ATK')
                escrever_texto(f'\nVocê sofreu {dano + 10} de dano.')
                
                os.system('cls')

                dano_player(player, vida_mago, mana_player, mana_mago, total, dano + 1)
                player -= dano + 10

            else:
                print(f'Mago: {mago_total}')
                escrever_texto('Você estourou valor, e o mago teve valor menor que 21!')

                for i in range(30):
                    dano = random.randint(1, 20)
                    print(f'\r{dano} ATK', end=' ', flush=True)
                    time.sleep(0.1)

                escrever_texto(f'\nVocê sofreu {dano} de dano.')
                
                os.system('cls')

                dano_player(player, vida_mago, mana_player, mana_mago, total, dano + 1)
                player -= dano

        elif mago_total > 21:
            print('Mago estourou o valor.')
            print('Você venceu o jogo!')
            print('__________________________________________________')
            print(f'Mago: {mago_total}')
            print(f'Seu total: {total}')
            print('__________________________________________________')

            if força == True:
                for c in range(30):
                    dano = random.randint(5, 30)
                    print(f'\r{dano} ATK', end=' ', flush=True)
                    time.sleep(0.1)

            else:
                for i in range(30): # sistema de dano
                    dano = random.randint(1, 20) # escolhe aleatóriamente entre 1 e 20
                    print(f'\r{dano} ATK', end=' ', flush=True) # imprime a variável na mesma linha apagando a mensagem anterior
                    time.sleep(0.1)

            escrever_texto(f'\nMago sofreu {dano} de dano.')

            os.system('cls')

            dano_mago(player, vida_mago, mana_player, mana_mago, total, dano + 1)
            vida_mago -= dano

        elif mago_total == 21:
            print('Mago ganhou com 21!')
            print('Dano crítico por valor 21!')
            print('__________________________________________________')
            for i in range(30):
                dano = random.randint(1, 20)
                print(f'\r{dano} ATK', end=' ', flush=True)
                time.sleep(0.1)
            print(f'\n{dano} + 10 ATK')

            escrever_texto(f'\nVocê sofreu {dano + 10} de dano.')

            os.system('cls')

            dano_player(player, vida_mago, mana_player, mana_mago, mago_total, dano + 1)
            player -= dano + 10

        elif total > mago_total:
            print('Você ganhou!')
            print('__________________________________________________')
            print(f'Mago: {mago_total}')
            print(f'Seu total: {total}')
            print('__________________________________________________')

            if força == True:
                for c in range(30):
                    dano = random.randint(5, 30)
                    print(f'\r{dano} ATK', end=' ', flush=True)
                    time.sleep(0.1)

            else:
                for i in range(30): # sistema de dano
                    dano = random.randint(1, 20) # escolhe aleatóriamente entre 1 e 20
                    print(f'\r{dano} ATK', end=' ', flush=True) # imprime a variável na mesma linha apagando a mensagem anterior
                    time.sleep(0.1)

            escrever_texto(f'\nMago sofreu {dano} de dano.')

            os.system('cls')

            dano_mago(player, vida_mago, mana_player, mana_mago, total, dano + 1)
            vida_mago -= dano

        elif mago_total > total:
            print('Mago ganhou!')
            print('__________________________________________________')
            print(f'Mago: {mago_total}')
            print(f'Seu total: {total}')
            print('__________________________________________________')

            for i in range(30):
                dano = random.randint(1, 20)
                print(f'\r{dano} ATK', end=' ', flush=True)
                time.sleep(0.1)

            escrever_texto(f'\nVocê sofreu {dano} de dano.')

            os.system('cls')

            dano_player(player, vida_mago, mana_player, mana_mago, total, dano + 1)
            player -= dano

        elif mago_total == total:
            escrever_texto('Empate, ambos perderam 10 de MANA.')
            dano = 10
            os.system('cls')

            mana_empate(player, vida_mago, mana_player, mana_mago, dano)
            mana_player -= 10
            mana_mago -= 10

    if player <= 0:
        player = 0
        os.system('cls')
        magos(player, vida_mago, mana_player, mana_mago)
        print(f'Que pena, você perdeu todo o seu HP. Tente novamente.')
        break

    elif vida_mago <= 0:
        vida_mago = 0
        os.system('cls')
        magos(player, vida_mago, mana_player, mana_mago)
        escrever_texto('Parabéns, você venceu o mago!')
        nível += 1
        atualizar_level(jogador[0], nível)
        break

    if cont == 1: 
        if vida_mago <= 15:
            os.system('cls')
            vingança(vida_mago, mana_mago) # tabela do mago para reviravolta
            mensagem = "Mago está com pouca vida, o que você deseja fazer?"
            escrever_texto_na_caixa(mensagem, largura=50, velocidade=0.03)

            print('┌───┬──────────┬───┬───────────┐')
            print('│ 1 │   matar  │ 2 │   poupar  │')
            print('└───┴──────────┴───┴───────────┘')

            escolha = int(input())
            os.system('cls')
            if escolha == 1:
                for c in range(30):
                    var = random.randint(1, 20)
                    print(f'\r{var} ATK', end=' ', flush=True)
                    time.sleep(0.1)
                time.sleep(1)
                print(' ')
                os.system('cls')

                if vida_mago <= var:
                    escrever_texto('Você acerta um golpe em cheio no mago')
                    time.sleep(1)

                    dano_mago(player, vida_mago, mana_player, mana_mago, total, var)
                    
                    escrever_texto('Você derrota o mago.')
                    time.sleep(1)

                    vida_mago = 0
                    os.system('cls')
                    magos(player, vida_mago, mana_player, mana_mago)
                    escrever_texto('Parabéns, você venceu o mago!')
                    nível += 1
                    atualizar_level(jogador[0], nível)
                    break

                elif vida_mago > var:
                    
                    os.system('cls')

                    mensagem = 'Você ataca, e ele se esquiva.'
                    escrever_texto_na_caixa(mensagem, largura = 50, velocidade = 0.03)
                    time.sleep(1)
                    
                    mensagem = 'Após isso, ele abre seu livro, e utiliza um dado de cura.'
                    escrever_texto_na_caixa(mensagem, largura =60, velocidade = 0.03)
                    time.sleep(1)

                    dano = random.randint(1, 20)
                    
                    for c in range(30):
                        vida = random.randint(1, 20)
                        print(f'\r{vida} HP', end=' ', flush=True)
                        time.sleep(0.1)
                    time.sleep(1)
                        
                    os.system('cls')
                    vingança_HP(vida_mago, mana_mago, vida)
                    vida_mago += vida
                    escrever_texto(f'Mago recuperou {vida} de HP.')

            elif escolha == 2:
                dano = random.randint(1, 100)
                dialogo_mago()

                os.system('cls')
                for c in range(dano):
                    dano = c
                    print(f'\r{c}', end=' ', flush=True) 
                    time.sleep(0.1)

                os.system('cls')
                print(f'\n Você sofreu {dano} ATK')
                time.sleep(1)
                
                dano_player(player, vida_mago, mana_player, mana_mago, total, dano + 1)
                player -= dano

                mensagem = 'Desbloqueado: Fúria arcana'
                escrever_texto_na_caixa(mensagem, largura=40, velocidade=0.03)
                time.sleep(0.3)
                escrever_texto('Enter para continuar')
                keyboard.wait('enter')
                input('')

                os.system('cls')
                escrever_texto('Descrição:')
                time.sleep(0.5)
                escrever_texto('Seus ataques agora podem dar de 5-30 de dano.')
                time.sleep(1.5)
                força = True
            else:
                print('Escolha apenas 1 ou 2!')
                time.sleep(1)
                
            cont -= 1 # vingança aparece apenas uma vez no jogo

    os.system('cls')  

    mana_player += 5
    mana_mago += 5

    if mana_player > 100:
        mana_player = 100

    if mana_mago > 100:
        mana_mago = 100

    os.system('cls')

escrever_texto('aguarde um pouco, iremos te redirecionar para um formulário de avaliação.')
time.sleep(3)

link = 'https://docs.google.com/forms/d/e/1FAIpQLSclrCTL815LdefoT2luIvsuuF1amvJRwT7iElWtdfrdmTAwbw/viewform?usp=header'
webbrowser.open(link)