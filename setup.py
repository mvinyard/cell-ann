
# -- import packages: ---------------------------------------------------------
import setuptools
import re
import os
import sys


# -- fetch requirements packages: ---------------------------------------------
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

with open('cell_ann/__version__.py') as v:
    exec(v.read())


# -- run setup: ---------------------------------------------------------------
setuptools.setup(
    name="cell_ann",
    version=__version__,
    python_requires=">3.9.0",
    author="Michael E. Vinyard",
    author_email="mvinyard.ai@gmail.com",
    url="https://github.com/mvinyard/cell-ann",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    description="cell-ann: Cell approximate nearest neighbors",
    packages=setuptools.find_packages(),
    install_requires=requirements,
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python :: 3.9",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
    ],
    license="MIT",
)
