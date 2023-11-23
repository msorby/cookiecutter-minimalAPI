"""
Does the following:

1. Inits git if used
2. Deletes dockerfiles if not going to be used
3. Deletes config utils if not needed
"""
from __future__ import print_function
import os
import shutil
from subprocess import Popen
from pathlib import Path

# Get the root project directory
PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

def remove_file(filename):
    """
    generic remove file from project dir
    """
    fullpath = os.path.join(PROJECT_DIRECTORY, filename)
    if os.path.exists(fullpath):
        os.remove(fullpath)

def init_git():
    """
    Initialises git on the new project folder
    """
    GIT_COMMANDS = [
        ["git", "init"],
        ["git", "add", "."],
        ["git", "commit", "-a", "-m", "Initial Commit."]
    ]

    for command in GIT_COMMANDS:
        git = Popen(command, cwd=PROJECT_DIRECTORY)
        git.wait()


def move_githubfolder():
    """
    Moves the github folder to the top directory
    """
    sourcefolder = os.path.join(PROJECT_DIRECTORY, ".github")
    p = Path(sourcefolder).absolute()
    parent_dir = p.parents[1]
    p.rename(parent_dir / p.name)
    
    #shutil.move(os.path.join(PROJECT_DIRECTORY, .".github"), "..")

def remove_docker_files():
    """
    Removes files needed for docker if it isn't going to be used
    """
    for filename in ["Dockerfile",]:
        os.remove(os.path.join(
            PROJECT_DIRECTORY, filename
        ))

# 0. Move github folder to top directory
move_githubfolder()

# 1. Remove Dockerfiles if docker is not going to be used
if '{{ cookiecutter.use_docker }}'.lower() != 'y':
    remove_docker_files()


# 7. Initialize Git (should be run after all file have been modified or deleted)
if '{{ cookiecutter.use_git }}'.lower() == 'y':
    init_git()
else:
    remove_file(".gitignore")