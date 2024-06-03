from app import app, db
from flask import render_template, request, redirect, url_for, session, flash
from models import User, Author, Book, Genre, Book_Author, Book_Genre, SavedBooks


@app.route('/')
def index():
    # if 'user_id' in session:
    #     user_id = session['user_id']
    #     user = User.query.get(user_id)
    #     return f'Bem-vindo, {user.name}!'
        return render_template('index.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/cadastro', methods=['POST'])
def cadastrar():
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        senha = request.form.get('senha')
        
        if not email or not username or not senha:
            return redirect(url_for('cadastro'))

        try:
            novo_usuario = User(email=email, name=username, password=senha)
            
            db.session.add(novo_usuario)
            db.session.commit()
            
            return redirect(url_for('index'))
        except Exception as e:
            flash(f"Erro ao cadastrar usuário: {e}", 'error')
            return redirect(url_for('cadastro'))

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def logar():
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')
        
        if not email or not senha:
            flash('Email e senha são obrigatórios!', 'error')
            return redirect(url_for('login'))
        
        # Verificar se o usuário existe no banco de dados
        user = User.query.filter_by(email=email, password=senha).first()
        
        if user:
            session['user_id'] = user.id_user
            flash('Login realizado com sucesso!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Email ou senha incorretos.', 'error')
            return redirect(url_for('login'))


@app.route('/detalhes_livro')
def detalhes_livro():
    return render_template('detalhes_livro.html')


@app.route('/usuario')
def usuario():
    return render_template('usuario.html')