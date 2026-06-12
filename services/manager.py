from models.user import User
from models.project import Project
from models.task import Task
from utils.storage import load_data, save_data


class ProjectManager:
    """
    Handles all operations between users, projects, and tasks.
    """

    def __init__(self):
        self.data = load_data()
        self.users = []

        self.load_users()

    # -------------------------
    # LOAD FROM JSON
    # -------------------------
    def load_users(self):
        """
        Load users, projects, and tasks from JSON storage.
        """
        for u in self.data.get("users", []):
            user = User(u["name"], u["email"])

            # Load projects
            for p in u.get("projects", []):
                project = Project(
                    p["title"],
                    p.get("description", "")
                )

                # Load tasks
                for t in p.get("tasks", []):
                    task = Task(t["title"])

                    if t.get("status") == "Completed":
                        task.mark_complete()

                    project.add_task(task)

                user.add_project(project)

            self.users.append(user)

    # -------------------------
    # SAVE TO JSON
    # -------------------------
    def save(self):
        data = {"users": []}

        for user in self.users:
            data["users"].append({
                "name": user.name,
                "email": user.email,
                "projects": [
                    {
                        "title": project.title,
                        "description": project.description,
                        "tasks": [
                            {
                                "title": task.title,
                                "status": task.status
                            }
                            for task in project.tasks
                        ]
                    }
                    for project in user.projects
                ]
            })

        save_data(data)

    # -------------------------
    # USER METHODS
    # -------------------------
    def add_user(self, name, email):
        user = User(name, email)
        self.users.append(user)
        self.save()
        return user

    def get_users(self):
        return self.users

    def find_user(self, name):
        for user in self.users:
            if user.name == name:
                return user
        return None

    # -------------------------
    # PROJECT METHODS
    # -------------------------
    def add_project(self, user_name, title, description=""):
        user = self.find_user(user_name)

        if not user:
            return None

        project = Project(title, description)
        user.add_project(project)

        self.save()
        return project

    # -------------------------
    # TASK METHODS
    # -------------------------
    def add_task(self, user_name, project_title, task_title):
        user = self.find_user(user_name)

        if not user:
            return None

        for project in user.projects:
            if project.title == project_title:
                task = Task(task_title)

                project.add_task(task)
                self.save()

                return task

        return None

    def complete_task(self, user_name, project_title, task_title):
        user = self.find_user(user_name)

        if not user:
            return False

        for project in user.projects:
            if project.title == project_title:
                for task in project.tasks:
                    if task.title == task_title:
                        task.mark_complete()

                        self.save()
                        return True

        return False