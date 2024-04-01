import sqlite3



def registar_cadastro(nome, endereco, contribuinte, senha, confirmar_senha):
    try:

        banco = sqlite3.connect('bancodedados.db')
        cursor = banco.cursor()

        if nome:
            pass
        if endereco:
            pass
        if contribuinte:
            pass
        if senha == confirmar_senha:
            pass
        else:
            print('erro na validação dos dados, verifique se está corretamente!')

        cursor.execute(f"INSERT INTO cliente VALUES ('{nome}','{endereco}','{contribuinte}','{senha}')")
        banco.commit()
        banco.close()

        return True
    except:
        print('erro')
        return False


