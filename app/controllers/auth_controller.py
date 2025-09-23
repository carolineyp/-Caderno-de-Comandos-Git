from app import app
from flask import render_template, request, redirect, url_for, session
from app.models.usuario import Usuario

# Criamos um usuário fixo para simulação
usuario_teste = Usuario("admin", "1234")

@app.route("/")
def home():
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        nome = request.form.get("nome")
        senha = request.form.get("senha")

        if nome == usuario_teste.nome and usuario_teste.autenticar(senha):
            session["usuario"] = nome
            return redirect(url_for("bemvindo"))
        else:
            return render_template("login.html", erro="Usuário ou senha inválidos")
    
    return render_template("login.html")

@app.route("/bemvindo")
def bemvindo():
    if "usuario" in session:
        return render_template("bemvindo.html", usuario=session["usuario"])
    return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop("usuario", None)
    return redirect(url_for("login"))
