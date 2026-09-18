from datetime import datetime, timezone
from app import db

def agora():
    return datetime.now(timezone.utc)


class Usuario(db.Model):
    __tablename__ = "usuarios"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha_hash = db.Column(db.String(255), nullable=False)
    papel = db.Column(db.String(20), nullable=False, default="usuario") #usuario ou tecnico tambem

class Chamado(db.Model):
    __tablename__ = "chamados"

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(150), nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    prioridade = db.Column(db.String(20), nullable=False, default="media") # baixa, media, alta
    status = db.Column(db.String(20), nullable=False, default="aberto") # aberto, em andamento, resolvido fechado
    criado_em = db.Column(db.DateTime, default=agora)

    autor_id = db.Column(db.Integer, db.ForeignKey("usuarios.id"), nullable=False)
    tecnico_id = db.Column(db.Integer, db.ForeignKey("usuarios.id"), nullable=True)

    autor = db.relationship("Usuario", foreign_keys=[autor_id])
    tecnico = db.relationship("Usuario", foreign_keys=[tecnico_id])
    comentarios = db.relationship(
        "Comentario", back_populates="chamado", cascade="all, delete-orphan"
    )

class Comentario(db.Model):
   __tablename__ = "comentarios"

   id = db.Column(db.Integer, primary_key=True)
   texto = db.Column(db.Text, nullable=False)
   criado_em = db.Column(db.DateTime, default=agora)

   chamado_id = db.Column(db.Integer, db.ForeignKey("chamados.id"), nullable=False)
   autor_id = db.Column(db.Integer, db.ForeignKey("usuarios.id"), nullable=False)

   chamado = db.relationship("Chamado", back_populates="comentarios")
   autor = db.relationship("Usuario")