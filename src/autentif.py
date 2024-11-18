from . import execucaouseradm as ex
from . import funcs_adm as func
from . import obj

def Autentificado(): # função para autentificar o usuário
  primeiraAut = True # atribui true para a variável primeiraAut
  while primeiraAut: # enquanto for true a variável primeiraAut esse loop será executado
    primRequisicao = input("Digite 'l' para logar, 'c' para cadastrar uma nova conta ou 'f' para finalizar a sessão\n") # pede para o usuário escolher "l" para logar e "c" para cadastrar uma nova conta
    if primRequisicao.lower() == "c": # transforma o valor da variável primRequisicao em minusculo e compara com a string "c"
      func.AdicionarUsuario() # executa a função AdicionarUsuario
    elif primRequisicao.lower() == "l": # transforma o valor da variável primRequisicao em minusculo e compara com a string "l"
      global autentificado # cria a variável global autentificado
      autentificado = False # atribui o valor false para autentificado
      while not autentificado: # enquanto for false a variável autentificado esse loop será executado
        autentificado = AutenticarUsuario() # atribui o valor retornado da função AutenticarUsuario
      ex.Execucao() # executa a função Execucao
    elif primRequisicao.lower() == "f":
      exit()
    else: # se não for atendido as condições executa a linha abaixo
      print("Comando inválido.\n") # imprime no console "Comando inválido."

def AutenticarUsuario(): # função para autentificar o usuário
    login1 = input("Digite o login: ") # pede para o usuário digitar o login
    senha1 = input("Digite a senha: ") # pede para o usuário digitar a senha
    for usuario in obj.listaDeUsuarios: # loop para verificar todos os objetos da lista de usuários
      if obj.usuarioAdmin.login == login1 and obj.usuarioAdmin.senha == senha1: # se o usuário e a senha forem iguais as do administrador
          ex.ExecucaoAdmin() # executa a função de execução do administrador
      elif usuario.login == login1 and usuario.senha == senha1: # senão se o login e a senha pertencer a um usuário
        print("Bem-vindo(a) ", usuario.nome) # imprime "Bem-vindo(a) " concatenado com o valor do nome do usuário
        return True # retorna true a função
    print("Login ou senha incorretos.\n") # caso não atenda aos requisitos anteriores imprime "Login ou senha incorretos."
    return False # retorna false a função