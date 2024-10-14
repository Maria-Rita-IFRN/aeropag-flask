from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/servicos')
def servicos():
    return render_template('servicos.html')


@app.route('/tarifas')
def tarifas():
    return render_template('tarifas.html')


@app.route('/avioes')
def avioes():
    return render_template('avioes.html')

@app.route('/clientes')
def clientes():
    return render_template('clientes.html')

@app.route('/cobrancas')
def cobrancas():
    return render_template('cobrancas.html')




if __name__ == '__main__':
    app.run(debug=True)
