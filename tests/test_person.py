import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from models.person import Person


p = Person("Alex", "alex@email.com")
print(p)