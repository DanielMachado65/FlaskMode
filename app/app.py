from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_login import LoginManager

app = Flask(__name__)

# caminho de um arquivo. Passar as configurações para o Flask
app.config.from_object('config')

# padrão para se chamar de banco
db = SQLAlchemy(app)

# para fazer a imigração dos comandos - que vai cuidar das imigrações
migrate = Migrate(app, db)

# controller das informações da aplicação - vai cuidar dos comandos para inicialização, já vem pronto os proprios comandos.
manager = Manager(app)
manager.add_command('db', MigrateCommand)

# Gerenciador de Login
lm = LoginManager(app)
lm.init_app(app)

# chamando os modelos
from app.models import tables

# executando rotas>
from app.controllers import default

