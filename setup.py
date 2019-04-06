from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='py-utils',
    url='https://github.com/pcs2112/py-utils',
    author='Vince Chavez',
    author_email='vchavez92780@gmail.com',
    # Needed to actually package something
    packages=['py-utils'],
    # Needed for dependencies
    install_requires=['numpy', 'pyodbc'],
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    license='MIT',
    description='An example of a python package from pre-existing code',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)