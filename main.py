'''
//Théo César Zanotto da Silva

Este  programa,  quando  executado,  irá  determinar  se  uma  string de
entrada  faz  parte  da  linguagem  𝐿    definida  por  𝐿 = {𝑥 | 𝑥 ∈
 {𝑎,𝑏}∗ 𝑒 𝑐𝑎𝑑𝑎 𝑎 𝑒𝑚 𝑥 é 𝑠𝑒𝑔𝑢𝑖𝑑𝑜 𝑝𝑜𝑟 𝑝𝑒𝑙𝑜 𝑚𝑒𝑛𝑜𝑠 𝑑𝑜𝑖𝑠 𝑏} segundo o alfabeto  Σ={𝑎,𝑏,𝑐}.
O  programa  que  você  desenvolverá  irá  receber  como  entrada um arquivo de texto  (.txt)
contendo várias strings. A primeira linha do arquivo indica quantas strings estão no arquivo de texto de
entrada. As linhas subsequentes contém uma string por linha.  A seguir está um exemplo das linhas que
podem existir em um arquivo de testes para o programa que você irá desenvolver:
3
abbaba
abababb
bbabbaaab
Neste  exemplo  temos  3  strings  de  entrada.  O  número  de  strings em  cada  arquivo  será
representado  por  um  número  inteiro  positivo.  A  resposta  do  seu  programa  deverá  conter  uma, e
somente uma linha de saída para cada string. Estas linhas conterão a string de entrada e o resultado
da validação conforme o formato indicado a seguir:
abbaba: não pertence.
A  saída  poderá  ser  enviada  para  um  arquivo  de  textos,  ou  para  o  terminal  padrão  e  será
composta de uma linha de saída por string de entrada. No caso do exemplo, teremos 3 linhas de saída.
Para que seu programa possa ser testado você deve criar, no mínimo, três arquivos de entrada
contendo um número diferente de strings diferentes.
'''

print('''Qual arquivo deverá ser analisado?
[] teste1
[] teste2
[] teste3
[] teste4

    Para utilizar um arquivo diferente, personalize previamente o arquivo vazio teste4 !
 ''')

# Selecting the txt file chosen by the user
opcao = str(input('Nome do arquivo escolhido: '))
arquivo = open(opcao + ".txt", 'r')

# acquiring the first line of the files to get the total number of expressions.
linha = int(arquivo.readline())

# while loop to configurate the Finite State Machine (FSM) to iterate over all the expressions.
while linha > 0:
    aux = []
    frase = arquivo.readline()
    check = True
    # one of the check marks to validate the expression. Initializes with the value True.
    estado = -2
    # initial state of the FSM.

    # Main iteration. The for loop reads character by character of the string.
    # The transitions of FSM are guided by what character is read in the for loop.
    for char in list(frase):

        # initial state
        if estado == -2:
            if char == 'a':
                aux.append(char)
                estado = -1
            if char == 'b':
                aux.append(char)
                estado = 1
            if char == 'c':
                aux.append(char)
                estado = -2

        # second state
        elif estado == -1:
            if char == 'a':
                estado = -1
                aux.append(char)
                check = False
            if char == 'b':
                estado = 0
                aux.append(char)
            if char == 'c':
                aux.append(char)
                estado = -1

        # third state
        elif estado == 0:
            if char == 'a':
                estado = -1
                aux.append(char)
                check = False
            if char == 'b':
                estado = 1
                aux.append(char)
            if char == 'c':
                aux.append(char)
                estado = 0

        # forth state
        elif estado == 1:
            if char == 'a':
                estado = -1
                aux.append(char)
            if char == 'b':
                estado = 1
                aux.append(char)
            if char == 'c':
                aux.append(char)
                estado = 1

    # Decreasing the value of this variable guarantees the correct functioning of the FSM.
    linha -= 1

    # There are two check marks to validate the expression.
    # One: The final state of FSM.
    # Two: The boolean value of the variable check
    # The final state of the FSM must be 1 and the boolean value must be True.
    # This is the only way an expression can be correct.

    # Checking the two conditions
    if check and estado == 1:
        for i in aux:
            print(i, end = '')
        print(': pertence')
    else:
        for i in aux:
            print(i, end = '')
        print(': não pertence')
