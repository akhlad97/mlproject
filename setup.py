from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

import os

def get_requirements(file_path: str) -> List[str]:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"'{file_path}' does not exist. Please make sure requirements.txt is present.")
    
    with open(file_path) as file_obj:
        requirements = [req.strip() for req in file_obj.readlines()]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='akhlad',
    author_email='akhlad.contact@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements(r'E:\python\Projects\ML_First_Project\requirments.txt')  # ⬅️ Runtime dependencies
)
