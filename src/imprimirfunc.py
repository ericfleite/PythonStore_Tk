from . import obj

def ImprimirTodosProdutos(): # função para impressão dos produtos cadastrados
    if not obj.listaDeObjetos:  # condicional para verificar se a lista de objetos dos produtos está vazia
        print("Não há produtos cadastrados.\n") # se a lista estiver vazia imprime "Não há produtos cadastrados."
        return # retorna vazio a função
    print("Lista de Produtos:\n") # se houver produtos na lista imprime "Lista de Produtos:"
    for produto in obj.listaDeObjetos:  # loop da lista de objetos dos produtos para passar por todos os objetos cadastrados
        produto.imprimir() # imprime o produto cadastrado da vez em que o loop for estiver chamando

def ImprimirTodosUsuarios(): # função para imprimir todos os usuários
    if not obj.listaDeUsuarios:  # condicional para verificar se a lista de objetos de usuários está vazia
        print("Não há produtos cadastrados.\n") # se a lista estiver vazia imprime "Não há produtos cadastrados"
        return # retorna vazio a função
    print("Lista de Usuários:\n") # se houver usuários na lista imprime "Lista de Usuários:"
    for usuario in obj.listaDeUsuarios:  # loop para verificar a lista completa dos objetos da lista de usuários
        usuario.imprimir() # imprime o usuário cadastrado da vez