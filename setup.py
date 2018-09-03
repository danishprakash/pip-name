from setuptools import setup

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='pip-name',
    version='1.0.2',
    description='Check whether package name is available on PyPi',
    long_description=long_description,
    author='Danish Prakash',
    author_email='danishprakash@outlook.com',
    url='https://github.com/prakashdanish/pip-name',
    install_requires=[
        'requests',
    ],
    scripts=['pip-name'],
)
