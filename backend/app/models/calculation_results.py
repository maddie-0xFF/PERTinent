from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from .base import Base

class CalculationResult(Base):
    __tablename__ = 'calculation_results'

    id = Column(Integer, primary_key=True, index=True)
    task_id = Column(Integer, ForeignKey('tasks.id', ondelete='CASCADE'), nullable=False)
    earliest_start = Column(Integer, nullable=False)  # Earliest start time in hours
    earliest_finish = Column(Integer, nullable=False) # Earliest finish time in hours
    latest_start = Column(Integer, nullable=False)    # Latest start time in hours
    latest_finish = Column(Integer, nullable=False)   # Latest finish time in hours
    total_float = Column(Integer, nullable=False)     # Total float in hours

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    task = relationship("Task", back_populates="calculation")