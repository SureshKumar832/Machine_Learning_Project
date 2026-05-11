from setuptools import find_packages, setup
from typing import List


MINUS_E_DOT = "-e ."
def get_packages(file_path : str) -> List:
    '''It will return the required packages from requirements.txt file'''
    with open(file_path) as file:
        text = file.readlines()

    requirements = [txt.strip() for txt in text]
    if MINUS_E_DOT in requirements:
        requirements.remove(MINUS_E_DOT)
    return requirements

setup(
    name = "machine-learning-project",
    author = "SureshKumar",
    author_email = "sureshkumar07930@gmail.com",
    packages = find_packages(),
    install_requires = get_packages("requirements.txt")
)