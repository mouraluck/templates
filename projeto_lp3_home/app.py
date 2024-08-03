from flask import Flask, render_template

app = Flask(__name__)

@app.route('/produtos')
def produtos():
    lista_produtos = [
        {"nome": "AmbientChá", "desc": "Este chá é milagroso", "img": "1"},
        {"nome": "CanabCreme", "desc": "Este creme é milagroso", "img": "2"},
        {"nome": "VerdeGel", "desc": "Este gel é milagroso", "img": "3"},
        {"nome": "GreenPlant", "desc": "Esta planta é milagrosa", "img": "4"},
        {"nome": "PoliVita", "desc": "Este polivitaminico é milagroso", "img": "5"},
        {"nome": "NatureLive", "desc": "Este produto é milagroso", "img": "6"},
            ]
    return render_template('produtos.html', produtos=lista_produtos)

@app.route('/termos')
def termos():
    return render_template('termos.html')

@app.route('/politica')
def politica():
    return render_template('politica.html')

@app.route('/como-utilizar')
def como_utilizar():
    return render_template('como-utilizar.html')

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/contato')
def contato():
    return render_template('contato.html')