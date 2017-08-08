from setuptools import setup

setup(
    name='pyscribble',
    version='0.1',
    description='A scribbletune-like library for Python3',
    url='https://github.com/blakeanedved/pyscribble',
    author='Blake Nedved',
    author_email='blakeanedved@gmail.com',
    packages=['pyscribble'],
    install_requires=[
        'midiutil'
    ],
    zip_safe=False
)