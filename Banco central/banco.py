from flask import Flask, render_template, redirect, url_for, request
from cadastro import registar_cadastro
from login import validar_cadastro

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        req = request.form

        email = req['email']
        senha = req['senha']

        validacao_login = validar_cadastro(email, senha)

        if validacao_login:
            return redirect('/dashboard')
        else:
            return redirect('/login')
    else:
        print('erro ao verificar o cadastro')

    return render_template("login.html")


@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():

    if request.method == 'POST':
        req = request.form

        nome = req['nome']
        endereco = req['endereco']
        contribuinte = req['contribuinte']
        senha = req['senha']
        confirmar_senha = req['confirmar_senha']

        if senha == confirmar_senha:
            validacao_registar = registar_cadastro(nome, endereco, contribuinte, senha)
            if validacao_registar:
                return redirect('/login')
            else:
                return redirect('/cadastro')
        else:
            print('erro ao verificar as passwords')
    else:
        print('erro ao cadastrar')

    return render_template('cadastro.html')


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


if __name__ == '__main__':
    app.run(debug=True)
