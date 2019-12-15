from setuptools import setup

setup(
    name='codeforces scrapper',
    version='1.0',
    description='Get data about users from Codeforces',
    author='kokolem',
    packages=['codeforcesScrapper'],
    install_requires=['requests', 'Pillow'],
    entry_points={
        'console_scripts': ['codeforces-scrapper = codeforcesScrapper.userData:main']
    }
)
