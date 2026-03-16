from fastapi import APIRouter, Depends
from sqlalchemy import Session
from app.database import get_db
from app.models.project import Project
from app.schemas.project_schema import ProjectCreate
router = APIRouter(prefix="/projects", tags=["projects"])
@router.post("/")
def create_project(project: ProjectCreate, db: Session = Depends(get_db)):
    new_project = Project(name=project.name, 
                          description=project.description
                          )
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    return new_project
@router.get("/")
def list_projects(db: Session = Depends(get_db)):
    return db.query(Project).all()

