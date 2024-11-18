class Usuario: # criação da classe Usuario
  def __init__(self, n, l, s): # construtor da classe Usuario e o uso dos parâmetros n para o nome, l para o login e s para a senha
    self.nome = n # atribuição do valor do parâmetro n para o atributo nome
    self.login = l # atribuição do valor do parâmetro l para o atributo login
    self.senha = s # atribuição do valor do parâmetro s para o atributo senha
  def imprimir(self): # método para imprimir informações do usuário
    print("Nome: ", self.nome) # imprime o valor do nome do usuário
    print("Login: ", self.login) # imprime o valor do login do usuário
    print("Senha: ", self.senha, "\n") # imprime o valor da senha do usuário

class Produto: # criação da classe Produto
  def __init__(self, c, d, v): # construtor da classe Produto e uso dos parâmetros c para o codigo, d para a descrição e v para valor
    self.codigo = c # atribuição do valor do parâmetro c para o atributo codigo
    self.descricao = d # atribuição do valor do parâmetro d para o atributo descricao
    self.valor = v # atribuição do valor do parâmetro v para o atributo valor
  def imprimir(self): # criação do método imprimir da classe Produto
    print("Código: ", self.codigo) # impressão do valor do atributo codigo
    print("Descrição: ", self.descricao) # impressão do valor do atributo descricao
    print("Valor: ", self.valor) # impressão do valor do atributo valor

class Eletronico(Produto): # criação da classe Eletronico que herda atributos e métodos da superclasse Produto
  def __init__(self, c, d, v, t): # construtor da classe Eletronico e uso dos parâmetros c, d e v para os atributos herdados da classe pai Produto e t para o atributo tensao
    self.tensao = t # atribuição do valor do parâmetro t para o atributo tensao
    super().__init__(c, d, v) # chamando o construtor da classe pai com os parâmetros e atributos para a classe pai Produto
  def imprimir(self): # criação do método imprimir da classe Eletronico
    super().imprimir() # chamando o método da classe pai Produto imprimir()
    print("Tensão: ", self.tensao, "\n") # impressão do valor do atributo tensao

class Vestuario(Produto): # criação da classe Vestuario que herda atributos e métodos da superclasse Produto
  def __init__(self, c, d, v, n, co, ta): # construtor da classe Vestuario e uso dos parâmetros c, d e v para os atributos herdados da classe pai Produto e n, co e ta para os atributos nome, cor e tamanho
    self.nome = n # atribuição do parâmetro n para o atributo nome
    self.cor = co # atribuição do parâmetro co para o atributo cor
    self.tamanho = ta # atribuição do parâmetro ta para o atributo tamanho
    super().__init__(c, d, v) # chamando o construtor da classe pai com os parâmetros e atributos para a classe pai Produto
  def imprimir(self): # criação do método imprimir da classe Vestuario
    super().imprimir() # chamando o método da classe pai Produto imprimir()
    print("Nome: ", self.nome)  # impressão do valor do atributo nome
    print("Cor: ", self.cor)  # impressão do valor do atributo cor
    print("Tamanho: ", self.tamanho)  # impressão do valor do atributo tamanho

class Calcado(Vestuario): # criação da classe Calcado que herda atributos e métodos da classe pai Vestuario
  def __init__(self, c, d, v, n, co, ta, ms, mps, mi): # construtor da classe Calcado e o uso dos parâmetros c, d, v, n, co e ta para os atributos herdados da classe pai Vestuario e ms, mps e mi para os atributos materialSola, materialParteSuperior e materialInterno
    self.materialSola = ms # atribuição do parâmetro ms para o atributo materialSola
    self.materialParteSuperior = mps # atribuição do parâmetro mps para o atributo materialParteSuperior
    self.materialInterno = mi # atribuição do parâmetro mi para o atributo materialInterno
    super().__init__(c, d, v, n, co, ta) # chamando o construtor da classe pai com os parâmetros e atributos para a classe pai Vestuario
  def imprimir(self): # criação do método imprimir da classe Calcado
    super().imprimir() # chamando o método da classe pai Vestuario imprimir()
    print("Material da sola: ", self.materialSola) # impressão do valor do atributo materialSola
    print("Material da Parte Superior:", self.materialParteSuperior) # impressão do valor do atributo materialParteSuperior
    print("Material Interno: ", self.materialInterno, "\n") # impressão do valor do atributo materialInterno

class Roupa(Vestuario): # criação da classe Roupa que herda atributos e métodos da classe pai Vestuario
  def __init__(self, c, d, v, n, co, ta, te): # método construtor da classe Roupa e o uso dos parâmetros c, d, v, n, co e ta para os atributos herdados da classe pai Vestuario e te para o atributo tecido
    self.tecido = te # atribuição do parâmetro te para o atributo tecido
    super().__init__(c, d, v, n, co, ta) # chamando o construtor da classe pai com os parâmetros e atributos para a classe pai Vestuario
  def imprimir(self): # criação do método imprimir da classe Roupa
    super().imprimir() # chamando o método da classe pai Vestuario imprimir()
    print("Tecido: ", self.tecido, "\n") # impressão do valor do atributo tecido

class Chapeu(Vestuario): # criação da classe Chapeu que herda atributos e métodos da classe pai Vestuario
  def __init__(self, c, d, v, n, co, ta, ti): # método construtor da classe Roupa e o uso dos parâmetros c, d, v, n, co e ta para os atributos herdados da classe pai Vestuario e ti para o atributo tipo
    self.tipo = ti # atribuição do parâmetro ti para o atributo tipo
    super().__init__(c, d, v, n, co, ta) # chamando o construtor da classe pai com os parâmetros e atributos para a classe pai Vestuario
  def imprimir(self):# criação do método imprimir da classe Chapeu
    super().imprimir() # chamando o método da classe pai Vestuario imprimir()
    print("Tipo: ", self.tipo, "\n")  # impressão do valor do atributo tipo