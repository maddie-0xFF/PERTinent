from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.model.task import Task
from app.schemas.task import TaskCreate, TaskUpdate
router = APIRouter(prefix="/tasks", tags=["tasks"])
@router.post("/", response_model=Task)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    new_task = Task(Project_id=task.Project_id, name=task.name, description=task.description, status=task.status)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task
@router.get("/project/{project_id}")
def get_tasks_by_project(project_id: int, db: Session = Depends(get_db)):
    return db.query(Task).filter(Task.Project_id == project_id).all()
