from sqlalchemy import Column, Integer, String
from database import Base

class Ativo(Base):
    __tablename__ = "ativos"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    categoria = Column(String)
    status = Column(String, default="Ativo")