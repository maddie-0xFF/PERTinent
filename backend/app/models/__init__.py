from .project import Project
from .task import Task
from .dependency import Dependency
from .calculation_results import CalculationResult
# This allows us to import all models from this package when we do "from app.models import *"'
__all__ = ['Project', 'Task', 'Dependency', 'CalculationResult']
#this file is used to make it easier to import all models from a single location
#by importing the models here, we can simply do "from app.models import Project,
#Task, Dependency, CalculationResult" instead of having to import each model
#individually from their respective files.
#and also to avoid circular imports, since some models reference each other.
# #By importing them here, we ensure that all models are available when needed 
#without running into import issues.