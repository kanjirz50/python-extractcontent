from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.rst"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="extractcontent",
    version="0.0.1",
    description="",
    long_description=long_description,
    url="https://github.com/kanjirz50/python-extractcontent",
    packages=find_packages(exclude=["contrib", "docs", "tests"]),
)
