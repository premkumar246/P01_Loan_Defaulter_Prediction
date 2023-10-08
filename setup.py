from setuptools import find_packages, setup
from typing import List

hyphen = '-e .'

def get_requirements(file_path:str)->List[str]:
    
    '''
    This Function will return the requirements
    '''
    requirements = []
    
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n','') for req in requirements]

        if hyphen in requirements:
            requirements.remove(hyphen)
    
    return requirements

setup(
name='P01_LOAN_DEFAULTER_PREDICTION',
version = '0.0.1',
author='Prem_Kumar_Sanamala',
author_email='sanamalapremkumar@gmail.com',
packages=find_packages(),
install_requires = get_requirements('requirements.txt')

)