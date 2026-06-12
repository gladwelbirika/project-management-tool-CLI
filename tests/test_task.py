import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from models.task import Task


t1 = Task("Implement CLI")
t2 = Task("Write tests")

print(t1)
print(t2)

t1.mark_complete()

print(t1)