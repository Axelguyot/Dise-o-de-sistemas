from dataclasses import dataclass
from app import db

@dataclass(init=True, eq=False)
class User(db.Model):
    """
    Clase que representa un usuario del sistema con distintos perfiles.
    """
    __tablename__ = "users"
    id: int = db.Column("id", db.Integer, primary_key=True, autoincrement=True)
    firstname: str = db.Column("firstname", db.String(100), nullable=False)
    lastname: str = db.Column("lastname", db.String(100), nullable=False)
    email: str = db.Column("email", db.String(250), unique=True, nullable=False)
    password: str = db.Column("password", db.String(254), nullable=False)
    role: int = db.Column("role", db.Integer, nullable=False)
    
    
    def __eq__(self, user: object) -> bool:
        return (self.id == user.id and self.email == user.email and
                self.firstname == user.firstname and self.lastname == user.lastname and
                self.role == user.role)