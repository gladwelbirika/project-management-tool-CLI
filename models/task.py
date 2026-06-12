class Task:
    """
    Represents a task inside a project.
    """

    id_counter = 1

    def __init__(self, title, assigned_to=None):
        self.task_id = Task.id_counter
        Task.id_counter += 1

        self.title = title
        self.status = "Pending"
        self.assigned_to = assigned_to

    def mark_complete(self):
        self.status = "Completed"

    def __str__(self):
        return f"Task {self.task_id}: {self.title} [{self.status}]"