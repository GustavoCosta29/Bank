import sqlite3



def validar_cadastro(email, senha):

    try:
        banco = sqlite3.connect('bancodedados.db')
        cursor = banco.cursor()
        cursor.execute("SELECT senha FROM cliente WHERE email = '{}'".format(email))
        senha_user = cursor.fetchall()
        banco.close()

        if senha == senha_user[0][0]:
            print("Dados de acesso validados")
            return True
        else:
            print("Erro ao validar seus dados")
            return False
    except:
        print("Erro ao validar seus dados")
        return False
