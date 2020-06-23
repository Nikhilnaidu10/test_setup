from setuptools import setup, find_packages

setup(name='test_setup',
    version='0.0.27',
    description='testing tensorflow package intallation',
    author='Nikhilnaidu10',
    url='https://github.com/Nikhilnaidu10/test_setup',
    packages=['nlp'],
    install_requires=[
        'tensorflow'
    ]
)
