from dataclasses import dataclass
from app import db

@dataclass(init=True, eq=False)
class Role(db.Model):
    """
    Clase que representa un Rol de usuario del sistema.
    """
    __tablename__ = "role"
    id: int = db.Column("id", db.Integer, primary_key=True, autoincrement=True)
    name: str = db.Column("firstname", db.String(100), nullable=False)
    
    
    
    def __eq__(self, role: object) -> bool:
        return (self.id == role.id and self.name == role.name)