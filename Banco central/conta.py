import sqlite3


def open_account(agencia, conta, iban, saldo, contribuinte_id):
    try:

        banco = sqlite3.connect('bancodedados.db')
        cursor = banco.cursor()

        cursor.execute(f"SELECT nome FROM cliente WHERE contribuinte = '{contribuinte_id}'")
        nome = cursor.fetchone()[0]
        cursor.execute("SELECT contribuinte_id FROM contas WHERE contribuinte_id = ?", (contribuinte_id,))
        contribuinte = cursor.fetchone()

        if contribuinte == None:
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
