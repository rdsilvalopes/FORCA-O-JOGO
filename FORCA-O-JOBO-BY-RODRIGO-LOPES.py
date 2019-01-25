import random

class Forca(object):
    # pass

    letra = ''
    conta_tentativa = 0
    conta_acertos = 0
    palavras_erradas = []
    palavras_certas = []
    banco_palavras = ['CASA', 'LEAO', 'SAP', 'JACARE', 'CORRUPTO', 'PARALELEPIPEDO', 'CASCADURA', 'PARAGUAI']

    def __init__(self, a):
        self.a = a

    def escolhapalavra(self):  # Função que escolhe uma palavra aleatória (random.choice) no banco de palavras
        self.a = random.choice(dados.banco_palavras)  # banco_palavras é uma lista de palavras
        return self.a

    def zero(self):
        print('               o---------o ')
        print('               |         | ')
        print('                         | ')
        print('                         | ')
        print('                         | ')
        print('                         | ')
        print('                         | ')
        print('                         | ')
        print('                         | ')
        print('                    _____|_____ ')

    def cabeca(self):
        print('               o---------o ')
        print('               |         | ')
        print('            -(Õ.Õ)-      | ')
        print('                         | ')
        print('                         | ')
        print('                         | ')
        print('                         | ')
        print('                         | ')
        print('                         | ')
        print('                    _____|_____ ')

    def bracoesq(self):
        print('               o---------o ')
        print('               |         | ')
        print('            -(Õ.Õ)-      | ')
        print('              /          | ')
        print('                         | ')
        print('                         | ')
        print('                         | ')
        print('                         | ')
        print('                         | ')
        print('                    _____|_____ ')

    def bracodir(self):
        print('               o---------o ')
        print('               |         | ')
        print('            -(Õ.Õ)-      | ')
        print('              / \        | ')
        print('                         | ')
        print('                         | ')
        print('                         | ')
        print('                         | ')
        print('                         | ')
        print('                    _____|_____ ')

    def peito(self):
        print('               o---------o ')
        print('               |         | ')
        print('            -(Õ.Õ)-      | ')
        print('              /-\        | ')
        print('                         | ')
        print('                         | ')
        print('                         | ')
        print('                         | ')
        print('                         | ')
        print('                    _____|_____ ')

    def barriga(self):
        print('               o---------o ')
        print('               |         | ')
        print('            -(Õ.Õ)-      | ')
        print('              /-\        | ')
        print('               |         | ')
        print('                         | ')
        print('                         | ')
        print('                         | ')
        print('                         | ')
        print('                    _____|_____ ')

    def pernaesq(self):
        print('               o---------o ')
        print('               |         | ')
        print('            -(Õ.Õ)-      | ')
        print('              /-\        | ')
        print('               |         | ')
        print('                \        | ')
        print('                         | ')
        print('                         | ')
        print('                         | ')
        print('                    _____|_____ ')

    def pernadir(self):
        print('               o---------o ')
        print('               |         | ')
        print('            -(Õ.Õ)-      | ')
        print('              /-\        | ')
        print('               |         | ')
        print('              / \        | ')
        print('                         | ')
        print('                         | ')
        print('                         | ')
        print('                    _____|_____ ')

    def hide_word(self):  # Oculta as LETRAS se elas NÃO existirem na palavra escolhida randomicamente

        rtn = ''
        for letra in self.a:
            if letra not in self.palavras_certas:
                # Se a letra escolhida NÃO estiver na lista de palavras_certas ele oculta
                rtn += '-'  # Oculta a letra
            else:
                rtn += letra  # Mostra a lista
        return rtn

    def adivinha_palavra(self, letra):

        # Valida se a Letra está ou não na lista de palavras CERTAS e ERRADAS e adiciona a letra
        if letra in dados.a and letra not in dados.palavras_certas:
            dados.palavras_certas.append(letra)
        elif letra not in dados.a and letra not in dados.palavras_erradas:
            dados.palavras_erradas.append(letra)
            dados.conta_tentativa += 1
        else:
            return False
        return True

    def status(self):

        #  Imprime a função hide_word que vai mostrar a palavra oculta e imprime o tamanho da palavra...
        #  ... escolhida randomicamente

        print('      A Palavra é', dados.hide_word(), 'e contém', len(dados.a), 'Letras.')
        # print()
        # for i in dados.palavras_certas:
        #     # print()
        #     print('Palavras certas', i)
        print()
        for i in dados.palavras_erradas:  # Imprime as palavras erradas
            print('Palavras erradas', i)
        print()

    def perdeu(self):

        #  Se o número de tentativas ERRADAS for igual a 7 o jogo encerra.
        #  Obs.: as Tentativas certas não são contabilizadas (ver função adivinha_palavra)

        if dados.conta_tentativa == 7:
            print('●▬▬▬▬▬▬▬▬▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬▬▬▬▬▬▬▬▬●')
            print(' ░░░░░░░░░░ \033[7;30mVOCÊ PERDEU\033[m ░░░░░░░░░░░')
            print('●▬▬▬▬▬▬▬▬▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬▬▬▬▬▬▬▬▬●')
            print()
            print('A palavra era ' + dados.a)  # A final do jogo imprime a palavra escolhida randomicamente
        else:
            return False
        return True

    def fim_de_jogo(self):  # Será o Fim do jogo se você ganhar ou perder

        return self.ganhou() or self.perdeu()

    def ganhou(self):  # Se nenhum caracter '_' estiver oculto da função (hide_word) você ganhou

        if '-' not in self.hide_word():
            print('●▬▬▬▬▬▬▬▬▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬▬▬▬▬▬▬▬▬●')
            print(' ░░░░░░░░░░ \033[7;30mVOCÊ GANHOU!\033[m ░░░░░░░░░░░')
            print('●▬▬▬▬▬▬▬▬▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬▬▬▬▬▬▬▬▬●')
            print()
            print('A palavra é ' + dados.a)  # Imprime a palavra escolhida randomicamente
            return True
        return False


dados = Forca(a='')
dados.escolhapalavra()
print('\n'*3)
print('Developed by Rodrigo Lopes\nrdsilvalopes@gmail.com\n')
dados.zero()


while not dados.fim_de_jogo():  # O jogo continua ser executado até que você Ganhe ou Perca

    print()
    print('●▬▬▬▬▬▬▬▬▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬▬▬▬▬▬▬▬▬●')
    print(' ░░░░░░░░░░ \033[7;30mFORCA O JOGO\033[m ░░░░░░░░░░')
    print('●▬▬▬▬▬▬▬▬▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬▬▬▬▬▬▬▬▬●')
    print()
    print(' Você tem \033[7;30m 7 \033[m tentativas de', '\033[7;30m', dados.conta_tentativa, '\033[m' ' JOGADAS perdidas')
    dados.status()
    dados.perdeu()
    dados.ganhou()
    dados.fim_de_jogo()
    print()
    letra = input('Escolha a Letra: ').upper()
    print()
    print('\n' * 50)
    dados.adivinha_palavra(letra)

    # print(dados.conta_tentativa)
    if dados.conta_tentativa == 1:
        print('\n' * 50)
        dados.cabeca()
    elif dados.conta_tentativa == 2:
        print('\n' * 50)
        dados.bracoesq()
    elif dados.conta_tentativa == 3:
        print('\n' * 50)
        dados.bracodir()
    elif dados.conta_tentativa == 4:
        print('\n' * 50)
        dados.peito()
    elif dados.conta_tentativa == 5:
        print('\n' * 50)
        dados.barriga()
    elif dados.conta_tentativa == 6:
        print('\n' * 50)
        dados.pernaesq()
    elif dados.conta_tentativa == 7:
        print('\n' * 50)
        dados.pernadir()


print()
print('Palavras certas', dados.palavras_certas)
print('Palavras erradas', dados.palavras_erradas)




