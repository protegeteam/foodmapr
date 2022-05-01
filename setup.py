from distutils.core import setup

from setuptools import find_packages

from foodmapr import __version__

classifiers = """
Development Status :: 4 - Beta
Environment :: Console
License :: OSI Approved :: GNU General Public License (GPL)
Intended Audience :: Science/Research
Topic :: Scientific/Engineering
Topic :: Scientific/Engineering :: Bio-Informatics
Programming Language :: Python :: 3.7
Programming Language :: Python :: 3.8
Programming Language :: Python :: 3.9
Programming Language :: Python :: 3.10
Operating System :: POSIX :: Linux
""".strip().split('\n')

setup(name='foodmapr',
      version=__version__,
      description='A derived work from LexMapr to map food names to ontology terms',
      author='Josef Hardi',
      author_email='josef.hardi@gmail.com',
      url='https://github.com/protegeteam/foodmapr.git',
      license='GPL-3.0',
      classifiers=classifiers,
      install_requires=[
          'inflection~=0.5',
          'nltk~=3.7',
          'python-dateutil~=2.8',
          'rdflib~=6.1',
      ],
      python_requires='>=3.7, <3.11',
      test_suite='nose.collector',
      tests_require=['nose'],
      packages=find_packages(),
      include_package_data=True,
      scripts=['bin/foodmapr']
)
