from flask import Flask, render_template
from models import db

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config.Config')

# Inicializar SQLAlchemy com o aplicativo
db.init_app(app)

from routes import *

if __name__ == '__main__':
    app.run(debug=True)
