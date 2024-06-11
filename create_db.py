import os
from app import app
from models import db, Genre, User, Book, Book_Genre, Author
from datetime import datetime
import pytz

with app.app_context():
    db.create_all()

    # Inserir os gêneros na tabela Genre
    genres = ["Ficção", "Não-Ficção", "Romance", "Aventura", "Terror", "Suspense", "Adulto", "Auto-Ajuda"]
    for genre_name in genres:
        genre = Genre(name_genre=genre_name)
        db.session.add(genre)

    # Criar usuário de teste
    admin = User(
        name='admin',
        email='admin@gmail.com',
        password='admin123'
    )
    db.session.add(admin)
    db.session.commit()  # Commit para garantir que admin.id_user esteja disponível

    # Salvar a capa do livro de exemplo na pasta de capas
    COVERS_FOLDER = app.config['COVERS_FOLDER']
    cover_filename = 'exemplo.jpg'
    cover_path = os.path.join(COVERS_FOLDER, cover_filename)

    # Criar autor de exemplo associado ao usuário 'admin'
    autor_exemplo = Author(
        id_user=admin.id_user,
        name_author='Autor de Exemplo'
    )
    db.session.add(autor_exemplo)
    db.session.commit()  # Commit para garantir que autor_exemplo.id_author esteja disponível

    # Criar livro de exemplo
    relative_cover_path = os.path.relpath(cover_path, start=app.static_folder)
    book_example = Book(
        name='Livro de Exemplo',
        author=autor_exemplo.name_author,
        overview='Este é um exemplo de livro',
        release_date=datetime.now(pytz.utc),
        cover_image=relative_cover_path.replace('\\', '/')  # Usar caminho relativo e barras padrão URL
    )
    db.session.add(book_example)
    db.session.commit()

    # Adicionar gêneros ao livro de exemplo
    for genre_name in genres:
        genre = Genre.query.filter_by(name_genre=genre_name).first()
        if genre:
            book_genre = Book_Genre(id_book=book_example.id_book, id_genre=genre.id_genre)
            db.session.add(book_genre)

    db.session.commit()
    print("Banco de dados criados com sucesso!")
