"""
ghgrenamer
"""

import versioneer
import os

from setuptools import setup
from setuptools.command.test import test as TestCommand

path = os.path.abspath(os.path.dirname(__file__))


class PyTest(TestCommand):

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        pytest.main(self.test_args)


with open(os.path.join(path, 'README.md'), "r") as f:
    readme = f.read()


cmdclass = versioneer.get_cmdclass()
cmdclass.update({"test": PyTest})

setup(
    name='ghgrenamer',
    version=versioneer.get_version(),
    description='Tool to rename GHG emissions or concentration names',
    long_description=readme,
    long_description_content_type="text/markdown",
    author='Robert Gieseke',
    author_email='robert.gieseke@pik-potsdam.de',
    url='https://github.com/openclimatedata/ghgrenamer',
    license='BSD',
    keywords=[],
        classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ],
    packages=['ghgrenamer'],
    tests_require=['pytest'],
    cmdclass=cmdclass
)
