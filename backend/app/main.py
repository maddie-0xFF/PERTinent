from fastapi import FastAPI

from app.routers import project_routes
from app.routers import task_routes
from app.routers import dependency_routes

app = FastAPI(title="ProjectPath API", version="1.0")

app.include_router(project_routes.router, prefix="/projects", tags=["Projects"])
app.include_router(task_routes.router, prefix="/tasks", tags=["Tasks"])
app.include_router(dependency_routes.router, prefix="/dependencies", tags=["Dependencies"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the ProjectPath API!"}  