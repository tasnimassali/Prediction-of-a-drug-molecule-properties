from setuptools import setup

setup(
    name="aman",
    version="1.0.0",
    author='Tasnim Assali',
    author_email='tasnimassali20@gmail.com',
    description='The objective of this application uses a deep learning model to predict basic properties of a molecule using its fingerprint features and smiles strings.',
    packages=["hub"],
    entry_points='''
        [console_scripts]
        aman = hub.cli:main
        '''
)
