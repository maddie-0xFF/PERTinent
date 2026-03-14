from pydantic import BaseModel

class ProjectCreate(BaseModel):
    name: str
    description: str | None = None
#    class Config:
class ProjectResponse(BaseModel):
    id: int
    name: str
    description: str | None 
    class Config:
        orm_mode = True