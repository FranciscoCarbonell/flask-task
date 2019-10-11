from flask_task import Task
from models import *
import time

task = Task()
print(task)

@task.decorator
def proceso():
    users = Users.query.all()
    print(users)
    time.sleep(7)