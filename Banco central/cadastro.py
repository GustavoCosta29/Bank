import sqlite3


def registar_cadastro(nome, endereco, contribuinte, senha):
    try:

        banco = sqlite3.connect('bancodedados.db')
        cursor = banco.cursor()

        if nome and endereco and contribuinte and senha:
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
