from . import classes

# instânciando os objetos de produtos
roupa1 = classes.Roupa("123", "Camisa", 125.25, "Camisa Mamonas Assassinas", "Preta", "GG", "Algodão") # instânciando o objeto roupa1 com os parâmetros "123", "Camisa", 125.25, "Camisa Mamonas Assassinas", "Preta", "GG", "Algodão"
roupa2 = classes.Roupa("124", "Saia", 100.00, "Saia Festa Junina", "Rosa", "M", "Algodão") # instânciando o objeto roupa2 com os parâmetros "124", "Saia", 100.00, "Saia Festa Junina", "Rosa", "M", "Algodão"
calcado1 = classes.Calcado("133", "Sapato", 150.25, "Sapato de Couro", "Preto", "40", "Borracha", "Couro", "Algodão") # instânciando o objeto calcado1 com os parâmetros "133", "Sapato", 150.25, "Sapato de Couro", "Preto", "40", "Borracha", "Couro", "Algodão"
calcado2 = classes.Calcado("134", "Tênis", 133.63, "Tênis Fake Nike", "Branco", "41", "Borracha", "Couro", "Algodão") # instânciando o objeto calcado2 com os parâmetros "134", "Tênis", 133.63, "Tênis Fake Nike", "Branco", "41", "Borracha", "Couro", "Algodão"
eletronico1 = classes.Eletronico("143", "Notebook", 1125.55, "220V") # instânciando o objeto eletronico1 com os parâmetros "143", "Notebook", 1125.55, "220V"
eletronico2 = classes.Eletronico("144", "Rádio", 60.55, "110V") # instânciando o objeto eletronico2 com os parâmetros "144", "Rádio", 60.55, "110V"
chapeu1 = classes.Chapeu("153", "Boné", 204.31, "Boné Lacoste", "Roxo", "G", "Aba Reta") # instânciando o objeto chapeu1 com os parâmetros "153", "Boné", 204.31, "Boné Lacoste", "Roxo", "G", "Aba Reta"
chapeu2 = classes.Chapeu("154", "Chapéu", 304.31, "Chapéu Cowboy", "Preto", "G", "Aba Larga") # instânciando o objeto chapeu2 com os parâmetros "154", "Chapéu", 304.31, "Chapéu Cowboy", "Preto", "G", "Aba Larga"

# instânciando os objetos dos usuários
usuario1 = classes.Usuario("Fulano da Silva", "Fulano123", "FuSilva123%") # instânciando o objeto usuario1 com o nome Fulano da Silva, o login Fulano123 e a senha FuSilva123%
usuario2 = classes.Usuario("Ciclano dos Santos", "Ciclanosantos", "Cici123@") # instânciando o objeto usuario2 com o nome Ciclano dos Santos, o login Ciclanosantos e a senha Cici123@
usuario3 = classes.Usuario("Joca Silva", "JocaBr", "JocaS234$") # instânciando o objeto usuario3 com o nome Joca Silva, o login JocaBr e a senha JocaS234$
usuarioAdmin = classes.Usuario("Administrador", "Admin", "Admin") # instânciando o objeto usuarioAdmin com o nome Administrador, login Admin e a senha Admin

# listas de objetos
listaDeObjetos = [roupa1, roupa2, calcado1, calcado2, eletronico1, eletronico2, chapeu1, chapeu2] # tupla dos objetos (produtos) da loja
listaDeCompra = [] # lista de compras do cliente
listaDeUsuarios = [usuario1, usuario2, usuario3, usuarioAdmin] # lista de usuários do sistema
