from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, text
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from .base import Base

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey('projects.id'), nullable=False)
    name = Column(String(150), nullable=False)
    description = Column(text)
    duration = Column(Integer, nullable=False)        # Duration in hours

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    project = relationship("Project", back_populates="tasks")

    predecessors = relationship(
        "dependency",
        foreign_keys="[dependency.c.successor_id]",
        back_populates="successor"
    )
    successors = relationship(
        "dependency",
        foreign_keys="[dependency.c.predecessor_id]",
        back_populates="predecessor"
    )

    calculation = relationship("CalculationResult",
                               uselist=False,
                               back_populates="task",
                               cascade="all, delete-orphan"
    )