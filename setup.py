from setuptools import setup, find_packages

setup(
    name='my_package',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/bomitech02/my_package',
    author='<Subomi Oyetoso',
    author_email='<soyetoso@gmail.com'
)