from setuptools import find_packages, setup

setup(
    name='CAIDAtoolset',
    packages=find_packages(include=['CAIDAtoolset']),
    version='0.1.0',
    description='library for downloading and parsing CAIDA IDTK datasets',
    author='Daniel Haden',
    license='MIT',
    install_requires=['networkx', 'beautifulsoup4']
)