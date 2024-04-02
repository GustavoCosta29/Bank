from flask import Flask, render_template, redirect, url_for, request
from cadastro import registar_cadastro
from login import validar_cadastro, alterar_cadastro
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


@app.route('/')
def home():
    return render_template('home.html')


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


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


if __name__ == '__main__':
    app.run(debug=True)
