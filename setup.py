import json
from setuptools import setup, find_packages

# Succesfull test of this tutorial was conducted for:
# 'tensorflow==1.13.1', 'keras==2.2.4', 'numpy==1.16.4', 'scipy==1.1.0', 'matplotlib', 'pandas', 'seaborn', 'pymatgen==2020.3.13', 'sklearn'

with open('metainfo.json') as file:
    metainfo = json.load(file)

setup(
    name='nn_regression',
    version='1.0',
    author=', '.join(metainfo['authors']),
    author_email=metainfo['email'],
    url=metainfo['url'],
    description=metainfo['title'],
    long_description=metainfo['description'],
    packages=find_packages(),
    install_requires=['mendeleev', 'tensorflow', 'keras', 'numpy', 'scipy', 'matplotlib', 'pandas', 'seaborn', 'pymatgen', 'sklearn'],
)
