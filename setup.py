import io
import os
import re

from setuptools import find_packages
from setuptools import setup


def read(filename):
    filename = os.path.join(os.path.dirname(__file__), filename)
    text_type = type(u"")
    with io.open(filename, mode="r", encoding='utf-8') as fd:
        return re.sub(text_type(r':[a-z]+:`~?(.*?)`'), text_type(r'``\1``'), 
            fd.read())


setup(
    name="earlyster_probability",
    version="0.1.1",
    url="https://github.com/earlyster/earlyster_probability",
    license='MIT',

    author="Justin Early",
    author_email="earlyster@gmail.com",

    description="A Binomial and Gaussian Distribution Probability Library",
    long_description=read("README.rst"),

    packages=['earlyster_probability'],
    zip_safe=False,
    install_requires=[],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
    ],
)
