from ast import List
from setuptools import find_packages , setup

HYPHEN_E_DOT = '-e .'
file_path = 'requirements.txt'
def get_requirements(file_path:str)->List(str):
    ''' this funtion will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n"," ")for req in  requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements  

setup(
    name = 'Sentiment_analysis',
    version = '0.0.1',
    author ='Kashsih',
    author_email='kthakur.9703@gmail.com',
    packages = find_packages(),
    install_reqiures = get_requirements('requirements.txt')
)