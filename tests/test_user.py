from models.user import User

def test_user_creation():
    user = User("Alex", "alex@email.com")

    assert user.name == "Alex"
    assert user.email == "alex@email.com"
    assert len(user.projects) == 0


def test_add_project():
    user = User("Alex", "alex@email.com")

    user.add_project("CLI Tool")

    assert len(user.projects) == 1