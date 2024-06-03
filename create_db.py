from app import app
from models import db, Genre

# Lista de gêneros a serem inseridos no banco de dados
genres = [
    "Adulto", "Auto-Ajuda", "Aventura", "Ação", "Época", "Ficção", 
    "Não-Ficção", "Romance", "Suspense", "Terror"
]

with app.app_context():
    db.create_all()
    
    # Inserir os gêneros na tabela Genre
    for genre_name in genres:
        genre = Genre(name_genre=genre_name)
        db.session.add(genre)
    
    db.session.commit()
    print("Banco de dados e gêneros criados com sucesso!")
