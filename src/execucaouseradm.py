import tkinter as tk
from tkinter import messagebox

# Exemplo de funções chamadas
from . import funcs_user as func  
from . import funcs_adm as afunc  
from . import imprimirfunc as imp  
from . import autentif  


BACKGROUND_COLOR = "#2e2e2e"  
BUTTON_COLOR = "#4a4a4a"      
TEXT_COLOR = "#ffffff"        
BUTTON_TEXT_COLOR = "#ffffff"  

def Execucao():  
    def AdicionarProdCarrinho():
        func.AdicionarAoCarrinho()
    
    def RemoverProdCarrinho():
        func.RetirarDoCarrinho()
    
    def Comprar():
        func.FinalizarCompra()
    
    def VerificarCarrinho():
        func.CarrinhoAgora()
    
    def VerProdutosLoja():
        imp.ImprimirTodosProdutos()
    
    def Sair():
        window.destroy()
        autentif.Autentificado()

    
    window = tk.Tk()
    window.title("Menu de Comprador")
    window.geometry("400x300")
    window.iconbitmap("C:/LojaTk/PythonStore_Tk/image/loja.ico")  
    window.configure(bg=BACKGROUND_COLOR)  

    tk.Label(window, text="Escolha uma ação:", bg=BACKGROUND_COLOR, fg=TEXT_COLOR).pack(pady=10)
    
    
    tk.Button(window, text="Adicionar Produto", command=AdicionarProdCarrinho, bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR).pack(fill=tk.X)
    tk.Button(window, text="Remover Produto", command=RemoverProdCarrinho, bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR).pack(fill=tk.X)
    tk.Button(window, text="Finalizar Compra", command=Comprar, bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR).pack(fill=tk.X)
    tk.Button(window, text="Verificar Carrinho", command=VerificarCarrinho, bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR).pack(fill=tk.X)
    tk.Button(window, text="Ver Produtos da Loja", command=VerProdutosLoja, bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR).pack(fill=tk.X)
    tk.Button(window, text="Sair", command=Sair, bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR).pack(fill=tk.X)

    window.mainloop()


def ExecucaoAdmin():  
    def AddUsuario():
        afunc.AdicionarUsuario()
    
    def RemoverUsuario():
        afunc.RemoverUsuario()
    
    def TrocarSenhaAdm():
        afunc.TrocarSenhaAdm()
    
    def ImprimirUsuarios():
        imp.ImprimirTodosUsuarios()
    
    def AdicionarProduto():
        escolha_tipo_produto()
    
    def RemoverProduto():
        afunc.RemoverProduto()
    
    def ImprimirProdutos():
        imp.ImprimirTodosProdutos()
    
    def SairAdmin():
        admin_window.destroy()
        autentif.Autentificado()
    
    def escolha_tipo_produto():
        tipo_produto = tk.Toplevel(admin_window)
        tipo_produto.title("Escolha o Tipo de Produto")
        tipo_produto.geometry("400x300")
        tipo_produto.iconbitmap("C:/LojaTk/PythonStore_Tk/image/loja.ico")
        tipo_produto.configure(bg=BACKGROUND_COLOR)

        tk.Button(tipo_produto, text="Eletrônicos", command=lambda: [afunc.AdicionarEletronico(), tipo_produto.destroy()], bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR).pack(fill=tk.X)
        tk.Button(tipo_produto, text="Calçados", command=lambda: [afunc.AdicionarCalcado(), tipo_produto.destroy()], bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR).pack(fill=tk.X)
        tk.Button(tipo_produto, text="Chapéus", command=lambda: [afunc.AdicionarChapeu(), tipo_produto.destroy()], bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR).pack(fill=tk.X)
        tk.Button(tipo_produto, text="Roupas", command=lambda: [afunc.AdicionarRoupa(), tipo_produto.destroy()], bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR).pack(fill=tk.X)
    
    
    admin_window = tk.Tk()
    admin_window.title("Menu do Administrador")
    admin_window.geometry("400x300")
    admin_window.iconbitmap("C:/LojaTk/PythonStore_Tk/image/loja.ico")
    admin_window.configure(bg=BACKGROUND_COLOR)

    tk.Label(admin_window, text="Escolha uma ação:", bg=BACKGROUND_COLOR, fg=TEXT_COLOR).pack(pady=10)

    tk.Button(admin_window, text="Adicionar Usuário", command=AddUsuario, bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR).pack(fill=tk.X)
    tk.Button(admin_window, text="Remover Usuário", command=RemoverUsuario, bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR).pack(fill=tk.X)
    tk.Button(admin_window, text="Trocar Senha do Administrador", command=TrocarSenhaAdm, bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR).pack(fill=tk.X)
    tk.Button(admin_window, text="Imprimir Usuários", command=ImprimirUsuarios, bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR).pack(fill=tk.X)
    tk.Button(admin_window, text="Adicionar Produto", command=AdicionarProduto, bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR).pack(fill=tk.X)
    tk.Button(admin_window, text="Remover Produto", command=RemoverProduto, bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR).pack(fill=tk.X)
    tk.Button(admin_window, text="Imprimir Produtos", command=ImprimirProdutos, bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR).pack(fill=tk.X)
    tk.Button(admin_window, text="Sair", command=SairAdmin, bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR).pack(fill=tk.X)

    admin_window.mainloop()

