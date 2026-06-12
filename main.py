import argparse
from services.manager import ProjectManager


def main():
    manager = ProjectManager()

    parser = argparse.ArgumentParser(description="TaskTrack CLI Tool")
    subparsers = parser.add_subparsers(dest="command")

    # ---------------- USER ----------------
    add_user = subparsers.add_parser("add-user")
    add_user.add_argument("--name", required=True)
    add_user.add_argument("--email", required=True)

    list_users = subparsers.add_parser("list-users")

    # ---------------- PROJECT ----------------
    add_project = subparsers.add_parser("add-project")
    add_project.add_argument("--user", required=True)
    add_project.add_argument("--title", required=True)
    add_project.add_argument("--description", default="")

    # ---------------- TASK ----------------
    add_task = subparsers.add_parser("add-task")
    add_task.add_argument("--user", required=True)
    add_task.add_argument("--project", required=True)
    add_task.add_argument("--title", required=True)

    complete_task = subparsers.add_parser("complete-task")
    complete_task.add_argument("--user", required=True)
    complete_task.add_argument("--project", required=True)
    complete_task.add_argument("--title", required=True)

    args = parser.parse_args()

    # ---------------- COMMAND HANDLING ----------------
    if args.command == "add-user":
        user = manager.add_user(args.name, args.email)
        print(f"User created: {user}")

    elif args.command == "list-users":
        for user in manager.get_users():
            print(user)

    elif args.command == "add-project":
        project = manager.add_project(args.user, args.title, args.description)
        if project:
            print(f"Project added: {project}")
        else:
            print("User not found")

    elif args.command == "add-task":
        task = manager.add_task(args.user, args.project, args.title)
        if task:
            print(f"Task added: {task}")
        else:
            print("User or project not found")

    elif args.command == "complete-task":
        success = manager.complete_task(args.user, args.project, args.title)
        if success:
            print("Task marked as completed")
        else:
            print("Task not found")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()