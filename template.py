'''
Automatically creates the folder structure of the project

This project structure is very much universal. Thus, we need not to always
create the project structure. Simply, execute this python file
'''

import os
from pathlib import Path
import logging

# Log for creating the structure
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:') # Log format

project_name = "cnnClassifier" # Technical project name

# List of files / folders to be created
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]

for filepath in list_of_files:
    filepath = Path(filepath) # '/' --> '\' (in paths) (Linux Path --> Windows Path)
    filedir, filename = os.path.split(filepath) # We have to separate out folders and files (from a single item)

    if filedir !="":
        os.makedirs(filedir, exist_ok=True) # if directory already created
        logging.info(f"Creating Directory; {filedir} for the file: {filename}")

    # Whether file is existing OR whether he file has some non-zero size (is there any content inside) or not
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating empty file: {filepath}")
    else: # If the file exists
        logging.info(f"{filename} already exists")

