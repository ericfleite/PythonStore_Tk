from . import obj

def AdicionarAoCarrinho(): # função para adicionar um produto ao carrinho de compras do cliente
  carrinhoDeCompraAdicionar = input("Coloque o código do produto:") # imprime no console "Coloque o código do produto:" e requisita o código do produto
  for lista in obj.listaDeObjetos: # loop para verificar se o código do produto existe entres os objetos e adiciona se o produto existir
    if lista.codigo == carrinhoDeCompraAdicionar: # condicional para vericar o código entre os objetos
      obj.listaDeCompra.append(lista) # adiciona o produto à lista de compra do cliente
      return # retorna para o main
  print("Produto inválido.\n") # caso o código do produto não está registrado entre os objetos enviará ao console "Produto inválido."

def RetirarDoCarrinho(): # função para retirar um produto do carrinho de compras do cliente
  if not obj.listaDeCompra: # verifica se a variável listaDeCompra está vazia
    print("O carrinho está vazio\n") # se estiver vázia irá imprimir no console "O carrinho está vazio"
    return # retorna para o main
  for i, lista in enumerate(obj.listaDeCompra): # loop para passar por toda lista de compra e enumerar as posições dos produtos
    print("Posição: ", i+1) # imprime a posição do produto
    lista.imprimir() # imprime as informações do produto
  try:
    carrinhoDeCompraRetirar = int(input("Digite a posição do produto na sua lista para retirar:\n")) # imprime no console "Digite a posição do produto na sua lista para retirar:" e requisita a posição do produto que ele deseja retirar
  except ValueError:
    print("Erro: Valor digitado precisa ser um número inteiro.\n")
  else:
    if 1 <= carrinhoDeCompraRetirar <= len(obj.listaDeCompra):
      print("Produto retirado:\n") # mensagem de produto retirado
      print(obj.listaDeCompra[carrinhoDeCompraRetirar - 1].imprimir()) # imprime no console o produto a ser retirado do carrinho de compras
      obj.listaDeCompra.pop(carrinhoDeCompraRetirar - 1) # retira o produto do carrinho de compras
      return # retorna vazio a função
    else: # caso a condicional não for atendida segue para a linha abaixo
      print("Posição inválida.\n") # imprime "Posição inválida" se não houver atendido a condicional if
      return # retorna vazio a função
  finally:
    return

def CarrinhoAgora(): # função para verificar o estado do carrinho
  if not obj.listaDeCompra: # verifica se a variável listaDeCompra está vazia
    print("O carrinho está vazio\n")  # se estiver vázia irá imprimir no console "O carrinho está vazio"
    return # retorna para o main
  for lista in obj.listaDeCompra: # loop para imprimir todos os produtos dentro do carrinho de compras
    lista.imprimir() # impressão do produto do estado atual do loop
  valorFinal = 0 # atribui o valor 0 para a variável listaFinal para o calculo do valor parcial do carrinho
  for lista in obj.listaDeCompra: # loop para calcular o valor parcial do carrinho
    valorFinal += lista.valor # soma o valor do produto ao resultado da variável valorFinal
  print("O valor do carrinho é: R$", valorFinal) # imprime no console "O valor do carrinho é: R$" mais o valor da variável valorFinal

def FinalizarCompra(): # função para finalizar a compra
  if not obj.listaDeCompra: # verifica se a variável listaDeCompra está vazia
    print("O carrinho está vazio\n")  # se estiver vázia irá imprimir no console "O carrinho está vazio"
    return # retorna para o main
  for lista in obj.listaDeCompra: # loop para imprimir todos os produtos dentro do carrinho de compras
    lista.imprimir() # impressão do produto do estado atual do loop
  valorFinal = 0 # atribui o valor 0 para a variável listaFinal para o calculo do valor final do carrinho
  for lista in obj.listaDeCompra: # loop para calcular o valor final do carrinho
    valorFinal += lista.valor # soma o valor do produto ao resultado da variável valorFinal
  print("O valor da compra é: R$",valorFinal) # Imprime no console "O valor da compra é: R$" mais o valor total da compra
  print("Realizar Pagamento. \n") # imprime no console "Realizar Pagamento."
  obj.listaDeCompra.clear() # limpa a lista de compras

