from tkinter import *
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

    listar = Button(janela,text='Listar', width=15)
    listar.place(x=200, y=200)

    janela.mainloop()

if __name__=='__main__':
    main()
