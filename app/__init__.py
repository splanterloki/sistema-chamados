from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def index():
        return "Sistema de comandos funcionando direitinho papae!"

    return app