from . import classes
from . import obj

def AdicionarUsuario(): # função para adicionar usuário
    nome = input("Digite o nome do usuário: ") # pede para digitar o nome do usuário que irá ser adicionado
    if len(nome) < 1:
        print("O nome não pode ficar vazio.")
        return
    login = input("Digite o login do usuário: ") # pede para digitar o login do usuário que irá ser adicionado
    if len(login) < 5:
        print("O login precisa ter pelo menos 5 caracteres.")
        return
    for usuario in obj.listaDeUsuarios: # loop para verificar toda a lista de usuários
      if usuario.login == login: # se houver registro de login que já existe
        print("Este login já está sendo utilizado.") # imprime "Este login já está sendo utilizado."
        return # retorna vazio a função
    senha = input("Digite a senha do usuário: ") # pede para digitar a senha do novo usuário
    if len(senha) < 6:
        print("A senha precisa ter pelo menos 6 caracteres.")
        return
    novoUsuario = classes.Usuario(nome, login, senha) # intância o objeto novo_usuário
    obj.listaDeUsuarios.append(novoUsuario) # adiciona o objeto novo_usuario na lista de usuários
    print("Usuário adicionado com sucesso.\n") # imprime no console "Usuário adicionado com sucesso."

def RemoverUsuario(): # função para remover usuário
    login = input("Digite o login do usuário que deseja remover: ") # pede ao usuário para digitar o login do usuário a ser removido
    for usuario in obj.listaDeUsuarios: # loop para verificar toda a lista de usuários
        if usuario.login == login and usuario.login != "Admin": # condicional para remover o usuário digitado se for igual a da lista e diferente do login do administrado segue em diante
            obj.listaDeUsuarios.remove(usuario) # remove o usuário (objeto) que atendeu as condições
            print("Usuário removido com sucesso.\n") # imprime "Usuário removido com sucesso."
            return # retorna vazio a função
    print("Usuário não encontrado.\n") # imprime "Usuário não encontrado."

def TrocarSenhaAdm(): # função para trocar senha do Administrador
    nova_senha = input("Digite a nova senha do administrador: ") # pede ao administrador digitar a nova senha 
    for usuario in obj.listaDeUsuarios: # loop para verificar a lista de usuários
        if usuario.login == "Admin": # condicional para verificar se a conta a ser trocada a senha é do administrador
            usuario.senha = nova_senha # troca a senha do administrador
            print("Senha do administrador alterada com sucesso.\n") # imprime "Senha do administrador alterada com sucesso."
            return # retorna vazio a função

def AdicionarEletronico(): # função para adicionar um novo produto eletrônico
    codigo = input("Digite o código do produto: ") # pede para o usuário digitar o código do novo produto eletrônico
    for produto in obj.listaDeObjetos: # loop para verificar a lista de objetos (produtos)
      if produto.codigo == codigo: # condicional para verificar se o codigo digitado existe no sistema
        print("Este código já está sendo utilizado.") # caso o código existe no sistema imprime "Este código já está sendo utilizado."
        return # retorna vazio a função
    descricao = input("Digite a descrição do produto: ") # pede ao usuário digitar a descrição do produto eletrônico
    try:
        valor = float(input("Digite o valor do produto: ")) # pede ao usuário digitar o valor do produto eletrônico
    except ValueError:
       print("Erro: Você digitou o valor do produto errado!\n")
    else:
        tensao = input("Digite a tensão do produto: ") # pede ao usuário digitar a tensão do produto eletrônico
        novoEletronico = classes.Eletronico(codigo, descricao, valor, tensao)  # instância o objeto novoEletronico
        obj.listaDeObjetos.append(novoEletronico) # adiciona o objeto novoEletronico na lista de produtos
        print("Produto eletrônico adicionado com sucesso.\n") # imprime no console "Produto eletrônico adicionado com sucesso."
    finally:
       return

def AdicionarCalcado(): # função para adicionar um novo calçado
    codigo = input("Digite o código do produto: ") # pede para o usuário digitar o código do novo produto calçado
    for produto in obj.listaDeObjetos: # loop para verificar a lista de objetos (produtos)
      if produto.codigo == codigo: # condicional para verificar se o codigo digitado existe no sistema
        print("Este código já está sendo utilizado.") # caso o código existe no sistema imprime "Este código já está sendo utilizado."
        return # retorna vazio a função
    descricao = input("Digite a descrição do produto: ") # pede ao usuário digitar a descrição do produto calçado
    try:
        valor = float(input("Digite o valor do produto: ")) # pede ao usuário digitar o valor do produto calçado
    except ValueError:
       print("Erro: Você digitou o valor do produto errado!\n")
    else:
        nome = input("Digite o nome do produto: ") # pede ao usuário digitar o nome do produto calçado
        cor = input("Digite a cor do produto: ") # pede ao usuário digitar a cor do produto calçado
        tamanho = input("Digite o tamanho do produto: ") # pede ao usuário digitar o tamanho do produto calçado
        materialSola = input("Digite o material da sola: ") # pede ao usuário digitar o material da sola do produto calçado
        materialParteSuperior = input("Digite o material da parte superior: ") # pede ao usuário digitar o material da parte superior do produto calçado
        materialInterno = input("Digite o material interno: ") # pede ao usuário digitar o material interno do produto calçado
        novoCalcado = classes.Calcado(codigo, descricao, valor, nome, cor, tamanho, materialSola, materialParteSuperior, materialInterno) # intancia o objeto novoCalcado
        obj.listaDeObjetos.append(novoCalcado) # adiciona o objeto novoCalcado na lista de objetos (produto)
        print("Calçado adicionado com sucesso.\n") # imprime no console "Calçado adicionado com sucesso."
    finally:
       return

def AdicionarChapeu(): # função para adicionar um novo chapéu
    codigo = input("Digite o código do produto: ") # pede para o usuário digitar o código do novo produto chapéu
    for produto in obj.listaDeObjetos: # loop para verificar a lista de objetos (produtos)
      if produto.codigo == codigo: # condicional para verificar se o codigo digitado existe no sistema
        print("Este código já está sendo utilizado.") # caso o código existe no sistema imprime "Este código já está sendo utilizado."
        return # retorna vazio a função
    descricao = input("Digite a descrição do produto: ") # pede ao usuário digitar a descrição do produto chapéu
    try:
        valor = float(input("Digite o valor do produto: ")) # pede ao usuário digitar o valor do produto chapéu
    except ValueError:
       print("Erro: Você digitou o valor do produto errado!\n")
    else:
        nome = input("Digite o nome do produto: ") # pede ao usuário digitar o nome do produto chapéu
        cor = input("Digite a cor do produto: ") # pede ao usuário digitar a cor do produto chapéu
        tamanho = input("Digite o tamanho do produto: ") # pede ao usuário digitar o tamanho do produto chapéu
        tipo = input("Digite o tipo do chapéu: ") # pede ao usuário digitar o tipo do chapéu
        novoChapeu = classes.Chapeu(codigo, descricao, valor, nome, cor, tamanho, tipo) # instância o objeto novoChapeu
        obj.listaDeObjetos.append(novoChapeu) # adiciona o objeto novoChapeu na lista de produtos
        print("Chapéu adicionado com sucesso.\n") # imprime no console "Chapéu adicionado com sucesso."
    finally:
       return

def AdicionarRoupa(): # função para adicionar uma nova roupa
    codigo = input("Digite o código do produto: ") # pede para o usuário digitar o código do novo produto chapéu
    for produto in obj.listaDeObjetos: # loop para verificar a lista de objetos (produtos)
      if produto.codigo == codigo: # condicional para verificar se o codigo digitado existe no sistema
        print("Este código já está sendo utilizado.") # caso o código existe no sistema imprime "Este código já está sendo utilizado."
        return # retorna vazio a função
    descricao = input("Digite a descrição do produto: ") # pede ao usuário digitar a descrição do novo produto roupa
    try:
        valor = float(input("Digite o valor do produto: ")) # pede ao usuário digitar o valor do produto roupa
    except ValueError:
       print("Erro: Você digitou o valor do produto errado!\n")
    else:
        nome = input("Digite o nome do produto: ") # pede ao usuário digitar o nome do novo produto roupa
        cor = input("Digite a cor do produto: ") # pede ao usuário digitar a cor do novo produto roupa
        tamanho = input("Digite o tamanho do produto: ") # pede ao usuário digitar o tamanho do novo produto roupa
        tecido = input("Digite o tipo de tecido: ") # pede ao usuário digitar o tecido do novo produto roupa
        novaRoupa = classes.Roupa(codigo, descricao, valor, nome, cor, tamanho, tecido) # instância o objeto novaRoupa
        obj.listaDeObjetos.append(novaRoupa) # adiciona o objeto novaRoupa na lista de produtos
        print("Roupa adicionada com sucesso.\n") # imprime no console "Roupa adicionada com sucesso."
    finally:
       return

def RemoverProduto(): # função para remover um produto da lista de produtos
    codigo = input("Digite o código do produto que deseja remover: ") # pede ao usuário digitar o código do produto que será retirado
    for produto in obj.listaDeObjetos: # loop para verificar a lista de objetos (lista de produtos)
        if produto.codigo == codigo: # condicional para verificar se o objeto contém o mesmo código
            obj.listaDeObjetos.remove(produto) # se for o mesmo código removerá o produto da lista
            print("Produto removido com sucesso.\n") # imprime no console "Produto removido com sucesso."
            return # retorna vazio a função
    print("Produto não encontrado.\n") # imprime "Produto não encontrado." caso não tenha encontrado o código na lista
