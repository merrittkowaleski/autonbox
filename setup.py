import os
import sys
from setuptools import setup, find_packages

PACKAGE_NAME = 'autonbox'
MINIMUM_PYTHON_VERSION = 3, 6


def check_python_version():
    """Exit when the Python version is too low."""
    if sys.version_info < MINIMUM_PYTHON_VERSION:
        sys.exit("Python {}.{}+ is required.".format(*MINIMUM_PYTHON_VERSION))


def read_package_variable(key):
    """Read the value of a variable from the package without importing."""
    module_path = os.path.join(PACKAGE_NAME, '__init__.py')
    with open(module_path) as module:
        for line in module:
            parts = line.strip().split(' ')
            if parts and parts[0] == key:
                return parts[-1].strip("'")
    raise KeyError("'{0}' not found in '{1}'".format(key, module_path))


def read_entry_points():
    with open('entry_points.ini') as entry_points:
        return entry_points.read()


check_python_version()
version = read_package_variable('__version__')

setup(
    name=PACKAGE_NAME,
    version=version,
    description='Auton Lab TA1 primitives',
    author=read_package_variable('__author__'),
    author_email=read_package_variable('__author_email__'),
    license='MIT',
    packages=find_packages(exclude=['docs', 'tests*']),
    install_requires=[
        'd3m',
        'Pillow>=7.1.2',
        'numpy',
        'pandas',
        'opencv-python-headless',
        'torch>=1.4.0',
        'torchvision>=0.5.0',
        'statsforecast',
        'neuralforecast>=1.3.0',
        'transformers>=4.6.0',
        'hyperopt'
    ],
    entry_points=read_entry_points(),
    url='https://github.com/autonlab/autonbox',
)
