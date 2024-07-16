from flask import Flask, render_template, request, redirect, url_for

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

@app.route('/situacaofinal/<float:nota>')
def situacaofinal(nota):
    if nota >= 6.0:
        return 'Você está aprovado'
    elif nota >= 3.0:
        return 'Você está em recuperação'
    else:
        return 'Você está reprovado'

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/verificarlogin', methods=['POST'])
def verificarlogin():
    usuario = request.form['usuario']
    senha = request.form['senha']

    if usuario == 'alba' and senha=='12345':
        return redirect(url_for('arearestrita'))
    else:
        return redirect(url_for('acessonegado'))

@app.route('/arearestrita')
def arearestrita():
    return render_template('arearestrita.html')

@app.route('/acessonegado')
def acessonegado():
    return render_template('acessonegado.html')


@app.route('/verificaridade2/<int:idade>')
def verificaridade2(idade):
    return render_template('verificaridade2.html', idade=idade)

@app.route('/listadecompras')
def listadecompras():
    return render_template('listadecompras.html')

@app.route('/recebeitens', methods=['POST'])
def recebeitens():
    itens = request.form.getlist("item")
    for i in itens:
        print(i)
    
    return render_template('itens.html', itens=itens)

