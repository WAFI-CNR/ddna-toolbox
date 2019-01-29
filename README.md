# Digital DNA Toolbox


[![PyPI license](https://img.shields.io/pypi/l/digitaldna.svg)](https://pypi.python.org/pypi/digitaldna/)
[![PyPI download month](https://img.shields.io/pypi/dm/digitaldna.svg)](https://pypi.python.org/pypi/digitaldna/)
[![PyPI version shields.io](https://img.shields.io/pypi/v/digitaldna.svg)](https://pypi.python.org/pypi/digitaldna/)

This project was build upon the [scikit-learn template](http://contrib.scikit-learn.org/project-template/) in order to be compatible with the scikit-learn pipelines and (hyper)parameter search, while facilitating testing (including some API compliance), documentation, open source development, packaging, and continuous integration.

## Installation and Usage
To install `digitaldna`, execute:
```shell
$ pip install digitaldna
```
If the installation is successful, and `digitaldna` is correctly installed,
you should be able to execute the following in Python:
```python
from digitaldna import LongestCommonSubsequence
X = ['banana', 'ananan', 'anana', 'hanoi', 'banas']
estimator = LongestCommonSubsequence()
estimator.fit_predict(X)
```

## Getting started
Some usage examples can be found in the documentation website.

## Important Links
- [Social Fingerprinting: Detection of Spambot Groups Through DNA-Inspired Behavioral Modeling](	https://ieeexplore.ieee.org/document/7876716)
- [Exploiting Digital DNA for the Analysis of Similarities in Twitter Behaviours](https://ieeexplore.ieee.org/document/8259831)
- [Linear Time Algorithms for Generalizations of the Longest Common Substring Problem](https://link.springer.com/article/10.1007/s00453-009-9369-1)
- [Scikit-learn Template Documentation](http://contrib.scikit-learn.org/project-template/)

## Contributing
If you want to contribute you can refer to the scikit-learn template documentation:
 - [scikit-learn template homepage](http://contrib.scikit-learn.org/project-template/)
 - [scikit-learn template source code](https://github.com/scikit-learn-contrib/project-template)
 - [scikit-learn Contributing section](http://scikit-learn.org/stable/developers/contributing.html)
 
### Testing
To run a single unit test (e.g. test_lcs)
```shell
$ nosetests -v digitaldna.tests.test_lcs
```
To run all unit tests
```shell
$ nosetests -v .
```
from the project root.

### Documentation
This repository also contains the source code used to build the [documentation](https://wafi-cnr.github.io/ddna/stable/) using [Sphynx](http://www.sphinx-doc.org/en/master/). You can generate the documentation HTML files executing from the `./doc` folder the dollowing command:
```shell
$ make html
```