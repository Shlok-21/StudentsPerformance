from setuptools import find_packages, setup
from typing import List

eDot = '-e .'

def get_requirements(file_path:str)->List[str]:
    '''This fn will return a list of requitements from the requirements.txt'''
    requirements=[]
    with open(file_path) as obj:
        requirements = obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if eDot in requirements:
            requirements.remove(eDot)
    return requirements

setup(
    name="StudentsPerformance",
    version="0.0.1",
    author='Shlok',
    author_email='shlokshivkar21@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)