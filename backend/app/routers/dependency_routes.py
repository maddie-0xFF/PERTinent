from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.dependency import Dependency
from app.schemas.dependency_schema import DependencyCreate
router = APIRouter(prefix="/dependencies", tags=["dependencies"])

@router.post("/", response_model=Dependency)
def create_dependency(dep: DependencyCreate, db: Session = Depends(get_db)):

    dependency = Dependency (predecessor_id=dep.predecessor_id,
                            successor_id=dep.successor_id
                            )
    db.add(dependency)
    db.commit()
    db.refresh(dependency)
    return dependency

