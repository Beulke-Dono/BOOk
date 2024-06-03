from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config.Config')

# Configuração do SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/api.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/detalhes_livro')
def detalhes_livro():
    return render_template('detalhes_livro.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/usuario')
def usuario():
    return render_template('usuario.html')

if __name__ == '__main__':
    app.run(debug=True)
