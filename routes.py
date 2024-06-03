from app import app, db
from flask import render_template, request, redirect, url_for
from models import User, Author, Book, Genre, Book_Author, Book_Genre, SavedBooks


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro', methods=['POST'])
def cadastrar():
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        senha = request.form.get('senha')
        
        # Verifique se os campos necessários estão presentes
        if not email or not username or not senha:
            # Adicione um flash message ou uma forma de retornar um erro ao usuário
            return redirect(url_for('cadastro'))

        try:
            # Crie um novo usuário com os dados do formulário
            novo_usuario = User(email=email, name=username, password=senha)
            
            # Adicione o novo usuário ao banco de dados
            db.session.add(novo_usuario)
            db.session.commit()
            
            # Redirecione para a página inicial após o cadastro
            return redirect(url_for('index'))
        except Exception as e:
            # Trate exceções, possivelmente informando o usuário de que ocorreu um erro
            print(f"Erro ao cadastrar usuário: {e}")
            # Adicione um flash message ou uma forma de retornar um erro ao usuário
            return redirect(url_for('cadastro'))

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