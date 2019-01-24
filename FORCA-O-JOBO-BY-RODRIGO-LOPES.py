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

    def escolhapalavra(self):
        self.a = random.choice(dados.banco_palavras)
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

    def hide_word(self):
        rtn = ''
        for letra in self.a:
            if letra not in self.palavras_certas:
                rtn += '-'
            else:
                rtn += letra
        return rtn

    def adivinha_palavra(self, letra):

        if letra in dados.a and letra not in dados.palavras_certas:
            dados.palavras_certas.append(letra)
        elif letra not in dados.a and letra not in dados.palavras_erradas:
            dados.palavras_erradas.append(letra)
            dados.conta_tentativa += 1
        else:
            return False
        return True

    def status(self):
        print('      A Palavra é', dados.hide_word(), 'e contém', len(dados.a), 'Letras.')
        # print()
        # for i in dados.palavras_certas:
        #     # print()
        #     print('Palavras certas', i)
        print()
        for i in dados.palavras_erradas:
            print('Palavras erradas', i)
        print()

    def perdeu(self):
        if dados.conta_tentativa == 7:
            print('●▬▬▬▬▬▬▬▬▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬▬▬▬▬▬▬▬▬●')
            print(' ░░░░░░░░░░ \033[7;30mVOCÊ PERDEU\033[m ░░░░░░░░░░░')
            print('●▬▬▬▬▬▬▬▬▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬▬▬▬▬▬▬▬▬●')
            print()

            # print('Game over! Você perdeu')
            print('A palavra era ' + dados.a)
        else:
            return False
        return True

    def fim_de_jogo(self):
        return self.ganhou() or self.perdeu()

    def ganhou(self):
        if '-' not in self.hide_word():
            # print('Você Ganhou!!!')
            # print('A palavra é ' + dados.a)
            print('●▬▬▬▬▬▬▬▬▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬▬▬▬▬▬▬▬▬●')
            print(' ░░░░░░░░░░ \033[7;30mVOCÊ GANHOU!\033[m ░░░░░░░░░░░')
            print('●▬▬▬▬▬▬▬▬▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬▬▬▬▬▬▬▬▬●')
            print()
            print('A palavra é ' + dados.a)
            return True
        return False


dados = Forca(a='')
dados.escolhapalavra()
print('\n'*3)
print('Developed by Rodrigo Lopes\nrdsilvalopes@gmail.com\n')
dados.zero()
# while not dados.ganhou():
while not dados.fim_de_jogo():

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
    letra = input('Escolha a Letra: ')
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




