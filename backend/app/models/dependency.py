from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from .base import Base

class Dependency(Base):
    __tablename__ = 'dependencies'
    id = Column(Integer, primary_key=True)
    
    predecessor_id = Column(Integer, ForeignKey('tasks.id', ondelete='CASCADE'),
                            nullable=False
                            )
    successor_id = Column(Integer, ForeignKey('tasks.id', ondelete='CASCADE'),
                          nullable=False
                          )
    __table_args__ = (UniqueConstraint('predecessor_id', 'successor_id'),
                     )
    predecessor = relationship('Task', foreign_keys=[predecessor_id], back_populates='successors')
    successor = relationship('Task', foreign_keys=[successor_id], back_populates='predecessors')
    
    