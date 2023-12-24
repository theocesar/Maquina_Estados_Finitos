from enum import Enum


class State(Enum):
    # states
    Zero = 0
    One = 1
    Two = 2
    Three = 3


def transitions():
    # state transitions
    return {
        State.Zero: {'a': State.One, 'b': State.Three, 'c': State.Zero},
        State.One: {'a': State.One, 'b': State.Two, 'c': State.One},
        State.Two: {'a': State.One, 'b': State.Three, 'c': State.Two},
        State.Three: {'a': State.One, 'b': State.Three, 'c': State.Three}
    }


def validation(string):
    # primary validation
    transicoes = transitions()
    estado = State.Zero
    check = True
    aux = []

    for char in string:
      aux.append(char)

      # Checking if the character is valid
      if char in transicoes[estado]:

        # Validating e making the transitions
        if char == 'a' and estado == State.One or char == 'a' and estado == State.Two:
          check = False
          estado = transicoes[estado][char]
        else:
          estado = transicoes[estado][char]

    return aux, check, estado


def final_validation(check, estado, aux):
    # Checking if the expression is correct
    result = ''.join(aux)

    if check and estado == State.Three:
        print(f'{result}: pertence')
    else:
        print(f'{result}: não pertence')


def main():
    print('''Qual arquivo deverá ser analisado?
    [] teste1
    [] teste2
    [] teste3
    [] teste4

        Para utilizar um arquivo diferente, personalize previamente o arquivo vazio teste4 !
    ''')

    # Selecting the txt file chosen by the user
    opcao = str(input('Nome do arquivo escolhido: '))
    with open(opcao + ".txt", 'r') as arquivo:
        linha = int(arquivo.readline())

        while linha > 0:
            frase = arquivo.readline().strip()
            aux, check, estado = validation(frase)
            final_validation(check, estado, aux)

            linha -= 1


if __name__ == "__main__":
    main()
