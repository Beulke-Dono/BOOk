from app import app
from models import db, Genre, User

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
    
    # Criar usuário de teste
    admin = User(
        name ='admin', 
        email='admin@gmail.com', 
        password='admin123'
    )
    db.session.add(admin)

    db.session.commit()
    print("Banco de dados criados com sucesso!")
