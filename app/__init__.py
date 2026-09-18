from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  #conecta o python e o banco de dados olha so que legal

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "troque-isso-depois"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///comandos.db" #localizaçao do banco de dados sem instalar nada

    db.init_app(app)

    from app import models # noqa: F401

    with app.app_context():
        db.create_all()

    @app.route("/")
    def index():
        return "Sistema de comandos funcionando direitinho papae!"

    return app