"""
CookieCutter Post-Gen Hook.

See:
    https://cookiecutter.readthedocs.io/en/latest/advanced/hooks.html
"""
import os
import subprocess

TERMINATOR = "\x1b[0m"
WARNING = "\x1b[1;33m [WARNING]: "
INFO = "\x1b[1;33m [INFO]: "
HINT = "\x1b[3;33m"
SUCCESS = "\x1b[1;32m [SUCCESS]: "

DEBUG_VALUE = "debug"


def remove_celery_files():
    file_names = [
        os.path.join("project", "app", "celery.py"),
    ]
    for file_name in file_names:
        os.remove(file_name)


def init_git_repo():
    subprocess.run("git init", shell=True, check=True, stdout=open(os.devnull, "wb"))
    subprocess.run("git add -A", shell=True, check=True, stdout=open(os.devnull, "wb"))
    subprocess.run(
        "git commit -m 'Initial commit'",
        shell=True, check=True, stdout=open(os.devnull, "wb"))


def main():
    if "{{ cookiecutter.use_celery }}".lower() == "n":
        remove_celery_files()
    if "{{ cookiecutter.init_git_repo}}".lower() == "y":
        init_git_repo()

    print(SUCCESS + "Project initialized, keep up the good work!" + TERMINATOR)


if __name__ == "__main__":
    main()
