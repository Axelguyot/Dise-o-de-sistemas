from dataclasses import dataclass
from app import db

@dataclass(init=True, eq=False)
class Ticket(db.Model):
    """
    Clase que representa un ticket del sistema.
    """
    __tablename__ = "ticket"
    id: int = db.Column("id", db.Integer, primary_key=True, autoincrement=True)
    category: str = db.Column("category", db.String(100), nullable=False)
    status: str = db.Column("status", db.String(100), nullable=False)
    received_date: str = db.Column("received_date", db.String(250), unique=True, nullable=False)
    completed_date: str = db.Column("completed_date", db.String(250), unique=True, nullable=False)
    description: str = db.Column(" description", db.String(250), unique=True, nullable=False)
    reply: str = db.Column("reply", db.String(250), unique=True, nullable=False)
    
    
    
    def __eq__(self, ticket: object) -> bool:
        return (self.id == ticket.id and self.category == ticket.category and
                self.status == ticket.status and self.received_date == ticket.received_date and
                self.completed_date == ticket.completed_date and 
                self.description == ticket.description and self.reply == ticket.reply)