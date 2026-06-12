class Project:
    """
    Represents a project that belongs to a user.
    Each project can have multiple tasks.
    """

    id_counter = 1

    def __init__(self, title, description="", due_date=None):
        self.project_id = Project.id_counter
        Project.id_counter += 1

        self.title = title
        self.description = description
        self.due_date = due_date
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def get_tasks(self):
        return self.tasks

    def __str__(self):
        return f"Project {self.project_id}: {self.title} ({len(self.tasks)} tasks)"