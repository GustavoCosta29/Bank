from flask import Flask, redirect, url_for, request
from flask_restful import Resource, Api
from cadastro import registar_cadastro
from login import validar_cadastro, alterar_cadastro
from conta import open_account
from transacao import transation
from transacao import consulta_saldo

import random

app = Flask(__name__)
api = Api(app)

contribuinte = 0

class Banco_login(Resource):
    def post(self):
        req = request.json
        email = req['email']
        senha = req['senha']

        validacao_login = validar_cadastro(email, senha)

        if validacao_login:
            return {"logged_in": True}
        else:
            return {"logged_in": False}

    def put(self):
        req = request.json

        email = req['email']
        nova_senha = req['nova_senha']
        confirmar_nova_senha = req['confirmar_nova_senha']

        if nova_senha == confirmar_nova_senha:
            validacao_nova_senha = alterar_cadastro(email, nova_senha)
            if validacao_nova_senha:
                return {"changed_password": True}
            else:
                return {"changed_password": False}
        else:
            print('Falha na alteração da nova senha')


api.add_resource(Banco_login, '/login')


class Banco_registro(Resource):

    def post(self):

        req = request.json

        nome = req['nome']
        endereco = req['endereco']
        contribuinte = req['contribuinte']
        senha = req['senha']
        confirmar_senha = req['confirmar_senha']

        if senha == confirmar_senha:
            validacao_registar = registar_cadastro(nome, endereco, contribuinte, senha)
            if validacao_registar:
                return {"registered_in": True}
            else:
                return {"registered_in": False}
        else:
            print('erro ao verificar as passwords')


api.add_resource(Banco_registro, '/cadastro')


class Conta_cliente(Resource):
    def post(self):
        req = request.json

        agencia = '0160'
        conta = random.randint(1, 999999)
        iban = ('PT50' + repr(random.randint(1, 999999)))
        saldo = 0
        contribuinte_id = req['contribuinte_id']

        if contribuinte_id:
            account_ok = open_account(agencia, conta, iban, saldo, contribuinte_id)
            if account_ok:
                return {"account_open": True}
            else:
                return {"account_open": False}
        else:
            print('contribuinte não cadastrado')


api.add_resource(Conta_cliente, '/dashboard')


class Transacao_bancaria(Resource):

    def post(self):
        req = request.json

        conta_logged = req['conta_logged']
        conta_destinatario = req['conta_destinatario']
        valor = req['valor']

        if transation(conta_logged, conta_destinatario, valor):
            return {'message': 'Transação cadastrada com sucesso!'}
        else:
            return {'message': 'Erro ao efetuar a transação'}

    def get(self):

        req = request.json

        conta_logged = req['conta_logged']

        saldo_atual = consulta_saldo(conta_logged)

        return {'message': f'Saldo atual é de {saldo_atual:}€'}


api.add_resource(Transacao_bancaria, '/transacao')

if __name__ == '__main__':
    app.run(debug=True)
