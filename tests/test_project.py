from models.project import Project

def test_project_creation():
    project = Project("CLI Tool", "Test project")

    assert project.title == "CLI Tool"
    assert project.description == "Test project"
    assert len(project.tasks) == 0