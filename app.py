from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Olá mundo'

@app.route('/dados')
def dados():
    return render_template('dados.html', nome='Alba')

@app.route('/recebedados', methods=['POST'])
def recebedados():
    nome = request.form['nome']
    sobrenome = request.form['sobrenome']
    estado = request.form['estado']
    ano = request.form['ano']
    disciplinas = request.form.getlist('disciplinas')
    return render_template('recebedados.html', nome=nome, sobrenome=sobrenome, estado=estado, ano=ano, disciplinas=disciplinas)


@app.route('/verificaridade/<int:idade>')
def verificaridade(idade):
    if idade >= 18:
        return 'Você tem' + str(idade) + '. Você é MAIOR de idade'
    else:
        return 'Você tem' + str(idade) + '. Você é MENOR de idade'
