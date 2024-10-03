from tkinter import *
from tkinter import ttk
import services


def main():
    def on_enviar():
        nome = nomeEntry.get()
        email = emailEntry.get()
        senha = senhaEntry.get()
        services.enviar_dados(nome, email, senha)
    
        # para limpar os campos 

        nomeEntry.delete(0, END)
        emailEntry.delete(0, END)
        senhaEntry.delete(0, END)
    
    def listar_usuario():
        usuarios = services.listar_usuario()

        #criar uma janela para mostrar a lista de usuarios
        janela_listar = Toplevel(janela)
        janela_listar.title('lista de usuários')
        janela_listar.geometry('600x300')

        #criar uma Treeview (visualização) da lista de usuarios
        tree = ttk.Treeview(janela_listar, columns = ('ID', 'nome', 'email'), show = 'headings')# tirar o cabeçalho
        tree.heading('ID', text = 'ID')
        tree.heading('nome', text = 'nome')
        tree.heading('nome', text = 'nome')

        #criar botao de voltar que fechará a tela de lista de usuario    
        voltar = Button(janela_listar, text = 'voltar', width = 10, command = janela_listar.destroy)
        voltar.pack(fill = BOTH, expand = True, side = BOTTOM)

        tree.pack(fill = BOTH, expand = True)

        #inserir os dados dos usuarios na treeview
        for usuario in usuarios:
            #END vai inserir o item no final da tabela
            tree.insert('', END, value = usuario)






    janela = Tk()
    janela.geometry('400x300')
    janela.title('Sistema de Gerenciamento de Usuário')

    titulo = Label(janela, text = 'CRUD', font = ('Arial black', 20))
    titulo.pack(pady = 30)
    # componentes de entrada
    #nome
    nome = Label(janela, text = 'Nome: ')
    nome.place(x= 50, y= 100)

    global nomeEntry
    nomeEntry = Entry(janela, width= 30)
    nomeEntry.place(x=100, y=100)

    #email
    global emailEntry
    email = Label(janela, text= 'Email: ')
    email.place(x=50, y=130)

    emailEntry = Entry(janela, width = 30)
    emailEntry.place(x= 100, y=130 )

    #senha
    global senhaEntry
    senha = Label(janela, text = 'Senha: ')
    senha.place(x=50, y=160)

    senhaEntry = Entry(janela, width= 30, show = '*' ) #comando show para esconder a senha
    senhaEntry.place(x= 100, y=160)

    cadastrar = Button(janela, text = 'Cadastrar', width = 10, command = on_enviar)
    cadastrar.place(x=100, y=200)

    listar = Button(janela, text = 'Listar usuários', width = 15, command = listar_usuario)
    listar.place(x=200, y= 200)

    janela.mainloop()


if __name__ == '__main__':
    main()