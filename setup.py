import os
from setuptools import setup, find_packages

setup(
    name='id-correction',
    version='0.2.0',
    packages=find_packages(),
    scripts=[[os.path.join(root, f) for f in files]
             for root, _, files in
             os.walk(os.path.join('id_correction', 'clis', 'bin'))][0],
)
