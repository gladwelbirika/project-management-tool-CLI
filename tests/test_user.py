import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from models.user import User


u1 = User("Alex", "alex@email.com")
u2 = User("John", "john@email.com")

print(u1)
print(u2)

u1.add_project("CLI Tool")
print("Projects:", u1.get_projects())