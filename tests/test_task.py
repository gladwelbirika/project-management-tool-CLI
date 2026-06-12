from models.task import Task

def test_task_creation():
    task = Task("Build CLI")

    assert task.title == "Build CLI"
    assert task.status == "Pending"


def test_mark_complete():
    task = Task("Build CLI")

    task.mark_complete()

    assert task.status == "Completed"