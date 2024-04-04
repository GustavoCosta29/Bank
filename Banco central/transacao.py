import sqlite3
import datetime


def transation(conta_logged, conta_destinatario, valor):
    try:

        saldo_emissor = 0
        saldo_destinatario = 0
        date = datetime.datetime.now()

        banco = sqlite3.connect('bancodedados.db')
        cursor = banco.cursor()

        cursor.execute("SELECT saldo, nome FROM contas WHERE conta = ? ",
                       (conta_logged,))

        result = cursor.fetchone()

        if result:
            saldo_emissor = result[0]
            nome = result[1]
        else:
            print("Nenhum resultado encontrado.")

        cursor.execute("SELECT saldo, nome FROM contas WHERE conta = ?", (conta_destinatario,))

        result_dest = cursor.fetchone()

        if result_dest:
            saldo_destinatario = result_dest[0]
            nome_destinatario = result_dest[1]

            if (saldo_emissor - valor) < 0:
                print("Saldo insuficiente.")
                return False
            else:
                novo_saldo_emissor = saldo_emissor - valor
                nova_saldo_destinatario = saldo_destinatario + valor

                cursor.execute("UPDATE contas SET saldo = ? WHERE conta = ? ", (novo_saldo_emissor, conta_logged))
                cursor.execute("UPDATE contas SET saldo = ? WHERE conta = ? ",
                               (nova_saldo_destinatario, conta_destinatario))
                cursor.execute(
                    "INSERT INTO transacao (data, conta_emissor, conta_destinatario, valor) VALUES (?, ?, ?, ?)",
                    (date, conta_logged, conta_destinatario, valor))

                banco.commit()
                banco.close()

                print(f'O valor de {valor} foi transferido com sucesso para a conta {conta_destinatario}')
        else:
            print("Nenhum resultado encontrado.")

        return True
    except Exception as e:
        print(f"Error occurred: {e}")
    return False


def consulta_saldo(conta_logged):

    try:

        banco = sqlite3.connect('bancodedados.db')
        cursor = banco.cursor()

        cursor.execute(f"SELECT saldo FROM contas WHERE conta = {conta_logged}")

        saldo = cursor.fetchone()[0]
        print(saldo)

        banco.close()

        return saldo
    except Exception as e:
        print(f"Error occurred: {e}")
        return False
