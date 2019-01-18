from __future__ import print_function
import sys
from setuptools import setup, find_packages

if sys.version_info.major < 3:
    sys.exit('Sorry, Python < 3 is not supported')
    
with open('requirements.txt') as f:
    INSTALL_REQUIRES = [l.strip() for l in f.readlines() if l]


try:
    import numpy
except ImportError:
    print('numpy is required during installation')
    sys.exit(1)

try:
    import scipy
except ImportError:
    print('scipy is required during installation')
    sys.exit(1)
    
try:
    import glcr
except ImportError:
    print('glcr is required during installation')
    sys.exit(1)
    
try:
    import sklearn
except ImportError:
    print('sklearn is required during installation')
    sys.exit(1)

setup(name='digitaldna',
      version='0.0.3',
      description='A Python implementation of Digital DNA modelling (https://arxiv.org/pdf/1602.00110.pdf)',
      author='Giuseppe Gagliano',
      packages=find_packages(),
      install_requires=INSTALL_REQUIRES,
      author_email='giuseppe.gagliano@iit.cnr.it',
      )
