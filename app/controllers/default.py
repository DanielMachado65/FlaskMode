from flask import render_template

from app.app import app
from app.models.forms import LoginForm


@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print(form.username.data)
        print(form.password.data)
        print(form.remember_me.data)
    else:
        print(form.errors)
    return render_template('login.html', form=form)



@app.route("/ola", defaults={'user': None})
@app.route("/ola/<user>")
def ola(user):
    return render_template('main.html', user=user)


# @app.route('/test', methods=['GET', 'POST'])
# def tesSt():
#     return render_template('main.html')


# passando como argumento que resulta no valor data.
@app.route("/test", defaults={'name': None})
@app.route("/test/<name>")
def test(name):
    if name:
        return "Olá: %s app" % name
    else:
        return "Olá usuário!"


# forçando a conversão, podemos fazer com int, float, string (padrão)
@app.route("/retorno/<int:id>")
def retorno(id):
    print(type(id))
    return str(id)
