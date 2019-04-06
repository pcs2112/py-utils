from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='py_utils',
    url='https://github.com/pcs2112/py-utils',
    author='Vince Chavez',
    author_email='vchavez92780@gmail.com',
    # Needed to actually package something
    packages=['py_utils'],
    # Needed for dependencies
    install_requires=['numpy', 'pyodbc'],
    # *strongly* suggested for sharing
    version='0.2',
    # The license can be anything you like
    license='MIT',
    description='Utilities for python',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)
