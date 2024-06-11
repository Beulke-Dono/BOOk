import os
import pytz
from app import app, db
from functools import wraps
from datetime import datetime
from werkzeug.utils import secure_filename
from flask import render_template, request, redirect, url_for, session, flash
from models import User, Author, Book, Genre, Book_Author, Book_Genre, SavedBooks

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


#### ROTAS

@app.route('/')
@login_required
def index():
    user_name = None
    if 'user_id' in session:
        user_id = session['user_id']
        user = User.query.get(user_id)
        if user:
            user_name = user.name
    return render_template('index.html', user_name=user_name)


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
@login_required
def usuario():
    user_name = None
    if 'user_id' in session:
        user_id = session['user_id']
        user = User.query.get(user_id)
        if user:
            user_name = user.name
    return render_template('usuario.html', user_name=user_name)

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))

@app.route('/enviar_livro')
@login_required
def enviarLivro():
    # Carregar gêneros existentes
    genres = Genre.query.all()
    user_name = None
    if 'user_id' in session:
        user_id = session['user_id']
        user = User.query.get(user_id)
        if user:
            user_name = user.name
    return render_template('enviar_livro.html', user_name=user_name, genres=genres)


@app.route('/enviar_livro', methods=['POST'])
@login_required
def envioLivro():
    if request.method == 'POST':
        name_book = request.form['name_book']
        author = request.form['author']
        overview = request.form['overview']
        genres = request.form.getlist('genres')  # Recebe uma lista de gêneros
        cover = request.files['cover']
        
        # Salvar a capa do livro
        if cover and allowed_file(cover.filename):
            filename = secure_filename(cover.filename)
            cover_path = os.path.join(app.config['COVERS_FOLDER'], filename)
            cover.save(cover_path)
        else:
            flash('Arquivo de capa inválido ou não enviado.', 'error')
            return redirect(url_for('enviarLivro'))
        
        # Data de publicação será a data de envio do livro (com reconhecimento de fuso horário)
        publication_date = datetime.now(pytz.timezone("GMT"))
        
        # Inicia uma nova transação
        try:
            db.session.begin()
            
            # Adicionar o livro ao banco de dados
            novo_livro = Book(
                name=name_book,
                overview=overview,
                release_date=publication_date,
                author=author,
                cover_image=cover_path  # Armazena o caminho da capa no banco de dados
            )
            db.session.add(novo_livro)
            db.session.flush()  # Obtém o ID do livro antes de adicionar os gêneros
            
            # Adicionar os gêneros ao banco de dados
            for genre_id in genres:
                livro_genero = Book_Genre(id_book=novo_livro.id_book, id_genre=genre_id)
                db.session.add(livro_genero)
            
            db.session.commit()  # Confirma a transação
            return redirect(url_for('usuario'))
        except Exception as e:
            db.session.rollback()  # Desfaz a transação em caso de erro
            flash('Erro ao enviar o livro: ' + str(e), 'error')
            return redirect(url_for('enviarLivro'))
