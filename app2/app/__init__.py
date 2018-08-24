from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# vai crir um arquivo.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# secrets, você pode pegar o secrets.token_hex(16)
app.config['SECRET_KEY'] = 'random-caracteres'

db = SQLAlchemy(app)

# importação de rotas.
from app2.app import routes