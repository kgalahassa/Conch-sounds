import sys
import os
from setuptools import setup
from setuptools.command.test import test as TestCommand

import multiprocessing

import acousticsim


def readme():
    with open('README.md') as f:
        return f.read()


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ['--strict', '--verbose', '-x', '--tb=long', 'tests']
        if os.environ.get('TRAVIS', False):
            self.test_args.insert(0, '--runslow')
        self.test_suite = True

    def run_tests(self):
        if __name__ == '__main__':  # Fix for multiprocessing infinite recursion on Windows
            import pytest
            errcode = pytest.main(self.test_args)
            sys.exit(errcode)


if __name__ == '__main__':
    setup(name='acousticsim',
          version=acousticsim.__version__,
          description='Analyze acoustic similarity in Python',
          classifiers=[
              'Development Status :: 3 - Alpha',
              'Programming Language :: Python',
              'Programming Language :: Python :: 3',
              'Operating System :: OS Independent',
              'Topic :: Scientific/Engineering',
              'Topic :: Text Processing :: Linguistic',
          ],
          keywords='phonetics acoustics similarity',
          url='https://github.com/mmcauliffe/python-acoustic-similarity',
          download_url='https://github.com/mmcauliffe/python-acoustic-similarity/tarball/{}'.format(
              acousticsim.__version__),
          author='Michael McAuliffe',
          author_email='michael.e.mcauliffe@gmail.com',
          packages=['acousticsim',
                    'acousticsim.analysis',
                    'acousticsim.analysis.amplitude_envelopes',
                    'acousticsim.analysis.formants',
                    'acousticsim.analysis.intensity',
                    'acousticsim.analysis.mfcc',
                    'acousticsim.analysis.mhec',
                    'acousticsim.analysis.pitch',
                    'acousticsim.analysis.praat',
                    'acousticsim.distance',
                    'acousticsim.representations'],
          package_data={'acousticsim.analysis.pitch': ['*.praat'],
                        'acousticsim.analysis.formants': ['*.praat'],
                        'acousticsim.analysis.intensity': ['*.praat'],
                        'acousticsim.analysis.mfcc': ['*.praat']},
          install_requires=[
              'numpy',
              'scipy',
              'textgrid',
              'librosa'
          ],
          cmdclass={'test': PyTest},
          extras_require={
              'testing': ['pytest'],
          }
          )
