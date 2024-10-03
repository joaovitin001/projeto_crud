from tkinter import *
from tkinter import  ttk
import services

def main():
    def on_enviar():
        nome = nomeEntry.get()
        email = emailEntry.get()
        senha = senhaEntry.get()
        services.enviar_dados(nome, email, senha)

        # Para limpar os campos
        nomeEntry.delete(0, END)
        emailEntry.delete(0, END)
        senhaEntry.delete(0, END)

    def lista_usuario():
        usuario = services.listar_usuario()

        # criar uma janela para mostrar a lista de usuarios
        janela_listar = Toplevel(janela)
        janela_listar.title('Lista de usuario')
        janela_listar.geometry('600x300')

        # criar uma view (visualização) da lista de usuário headings para limpar o cabeçalho
        tree = ttk.Treeview(janela_listar, columns=('ID', 'Nome', 'Email'), show='headings')
        tree.heading('ID', text='ID')
        tree.heading('Nome', text='Nome')
        tree.heading('Email', text='Email')

        # criar botão de voltar que fechará a tela de lista de usuario
        voltar= Button(janela_listar, text='voltar', width=10, command=janela_listar.destroy)
        voltar.pack(fil=BOTH, expand=True, side=BOTTOM)

        tree.pack(fill=BOTH, expand=True)

        # inserir os dados dos usuarios na treeview
        for usuario in usuario:
            # END vai inserir o item no final da tabela
            tree.insert('',END, values=usuario)




    janela = Tk()
    janela.geometry('400x300')
    janela.title('Sistema de Gerenciameneto de usuário')


    titulo = Label(janela, text='CRUD', font=('Arial black', 20))
    titulo.pack(pady=30)
    #comonentes de entrada

    #nome
    nome = Label(janela, text='Nome:')
    nome.place(x=50, y=100)

    global nomeEntry
    nomeEntry = Entry(janela, width=30)
    nomeEntry.place(x=100, y=100)



    # Email
    global emailEntry
    email = Label(janela, text='Email:')
    email.place(x=50, y=130)

    emailEntry = Entry(janela, width=30)
    emailEntry.place(x=100, y=130)

    #Senha

    senha = Label(janela, text='Senha:' )
    senha.place(x=50, y=160)

    # Comando show para escoder a senha
    senhaEntry = Entry(janela, width=30, show='*')
    senhaEntry.place(x=100, y=160)

    cadastrar = Button(janela, text='Cadastro', width=10, command=on_enviar)
    cadastrar.place(x=100, y=200 )

    listar = Button(janela,text='Listar', width=15, command=lista_usuario)
    listar.place(x=200, y=200)

    janela.mainloop()

if __name__ == '__main__':
    main()
