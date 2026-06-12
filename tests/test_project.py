import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from models.project import Project


p1 = Project("CLI Tool", "Build a CLI app")

print(p1)

p1.add_task("Implement CLI")
p1.add_task("Add tests")

print(p1.get_tasks())