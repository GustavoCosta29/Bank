import sqlite3


def open_account(agencia, conta, iban, saldo, contribuinte_id):
    try:

        banco = sqlite3.connect('bancodedados.db')
        cursor = banco.cursor()

        cursor.execute(f"SELECT * FROM cliente WHERE contribuinte = '{contribuinte_id}'")

        resultado = cursor.fetchall()

        nome = resultado[0][0]
        contribuinte = resultado[0][2]

        if contribuinte:
            cursor.execute(
                f"INSERT INTO contas VALUES ('{agencia}','{conta}','{iban}','{saldo}','{contribuinte_id}','{nome}')")
            banco.commit()
            banco.close()
        else:
            print('Este contribuinte já se encontra cadastrado')
        return True

    except:
        print('Erro ao criar a conta bancaria')
        return False
