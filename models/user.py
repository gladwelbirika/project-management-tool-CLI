from models.person import Person

class User(Person):
    """
    Represents a system user who can own multiple projects.
    """

    id_counter = 1

    def __init__(self, name, email):
        super().__init__(name, email)

        self.user_id = User.id_counter
        User.id_counter += 1

        self.projects = []

    def add_project(self, project):
        self.projects.append(project)

    def get_projects(self):
        return self.projects

    def __str__(self):
        return f"User {self.user_id}: {self.name} ({len(self.projects)} projects)"