import re
import os.path
from setuptools import setup


ROOT = os.path.dirname(__file__)
README = open(os.path.join(ROOT, 'README.rst')).read()
INIT_PY = open(os.path.join(ROOT, 'cssselect', '__init__.py')).read()
VERSION = re.search("VERSION = '([^']+)'", INIT_PY).group(1)


setup(
    name='cssselect',
    version=VERSION,
    author='Ian Bicking',
    author_email='ianb@colorstudy.com',
    maintainer='Simon Sapin',
    maintainer_email='simon.sapin@exyr.org',
    description=
        'cssselect parses CSS3 Selectors and translates them to XPath 1.0',
    long_description=README,
    url='http://packages.python.org/cssselect/',
    license='BSD',
    packages=['cssselect'],
    test_suite='cssselect.tests',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.4',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
    ],
)
