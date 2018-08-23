from flask import render_template, flash, redirect, url_for
from flask_login import login_user, logout_user

from app.app import app, db, lm
from app.models.forms import LoginForm
from app.models.tables import User


# carregar os dados do usuário logado.
@lm.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()


@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            flash("logged in")
            return redirect(url_for('index'))
        else:
            flash("Invalid login")
    else:
        print(form.errors)
    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    flash("logged out")
    return redirect('login')


@app.route("/ola", defaults={'user': None})
@app.route("/ola/<user>")
def ola(user):
    return render_template('main.html', user=user)


# @app.route('/test', methods=['GET', 'POST'])
# def tesSt():
#     return render_template('main.html')


# passando como argumento que resulta no valor data.
@app.route("/test", defaults={'info': None})
@app.route("/test/<info>")
def test(info):
    i = User("daniel", "1234", "Daniel Machado", "danielmachado@gmass.com")
    db.session.add(i)
    db.session.commit()
    return "Foi adicionado com sucesso"


@app.route("/select", defaults={'info': None})
@app.route("/select/<info>")
def select(info):
    i = User.query.filter_by(password='1234').first()
    return i.username + i.name + i.password


# forçando a conversão, podemos fazer com int, float, string (padrão)
@app.route("/retorno/<int:id>")
def retorno(id):
    print(type(id))
    return str(id)
