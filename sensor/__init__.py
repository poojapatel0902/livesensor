from setuptools import find_packages,setup
from typing import List
def get_requirements()->List[str]:
    """
    this function will return list of requirement
    """
    requirement_list:List[str]=[]
    """"
    write a code to read requiremnets.txt file and append each requirement in requirement_list variable.
    """
    return requirement_list

setup(
    name="sensor",
    version="0.0.1",
    author="pooja",
    author_email="pooja980900@gmail.com",
    install_requires=get_requirements(),
)