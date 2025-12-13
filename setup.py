from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:
    """
    This function will return the list of requirements
    """
    requirement_list:List[str] = []
    try:
        # open and read the requirements.txt file
        with open("requirements.txt", "r") as file:
            lines = file.readlines()
            #Process each line
            for line in lines:
                #strip whitespace and newlines
                req = line.strip()
                #ignore empty lines and comments
                if req and req != '-e .':
                    requirement_list.append(req)
    except FileNotFoundError:
        print("The requirements.txt file was not found.")
    return requirement_list
print(get_requirements())

setup(
    name="AI_Trip_Planner",
    version="0.0.1",
    author="Saran Raj",
    author_email="saranrajk261198@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)