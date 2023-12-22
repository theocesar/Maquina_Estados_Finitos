print('''Qual arquivo deverá ser analisado?
[] teste1
[] teste2
[] teste3
[] teste4

    Para utilizar um arquivo diferente, personalize previamente o arquivo vazio teste4 !
 ''')

def final_validation():
  # Checking the two conditions
  if check and estado == 1:
      for i in aux:
          print(i, end = '')
      print(': pertence')
  else:
      for i in aux:
          print(i, end = '')
      print(': não pertence')




# Selecting the txt file chosen by the user
opcao = str(input('Nome do arquivo escolhido: '))
with open(opcao + ".txt", 'r') as arquivo:
  linha = int(arquivo.readline())

  while linha > 0:
      aux = []
      frase = arquivo.readline()
      check = True
      estado = -2

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
  
      linha -= 1
  
      # There are two check marks to validate the expression.
      # One: The final state of FSM.
      # Two: The boolean value of the variable check
      # The final state of the FSM must be 1 and the boolean value must be True.
      # This is the only way an expression can be correct.
  
      final_validation()
  