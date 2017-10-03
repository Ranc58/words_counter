from setuptools import setup, find_packages
from os.path import join, dirname
import words_counter

setup(
    name='words_counter',
    version='1.3.4',
    packages=find_packages(),
    author='Vladimir Aleshin',
    author_email='rancvova@gmail.com',
    url='https://github.com/Ranc58/verbs_counter',
    license='MIT License',
    long_description=open(join(dirname(__file__), 'README.rst')).read(),
    entry_points={
        'console_scripts':
            ['words_counter = words_counter.words_counter:main']
    },
    install_requires=[
        'nltk==3.2.4',
        'GitPython==2.1.7'
    ],
    test_suite='words_counter.tests',
)
