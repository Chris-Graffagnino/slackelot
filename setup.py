from setuptools import setup, find_packages

from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

INSTALL_REQUIRES = ['requests', 'pytest']
EXTRAS_REQUIRE = {}

PACKAGES = find_packages(exclude=['contrib', 'docs', 'tests'])

CLASSIFIERS = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Topic :: Software Development :: Libraries :: Python Modules',
]

# Thanks to Hynek Schlawack for explaining conditional python dependencies
# https://hynek.me/articles/conditional-python-dependencies/
if int(setuptools.__version__.split(".", 1)[0]) < 18:
    assert "bdist_wheel" not in sys.argv, "setuptools 18 required for wheels."
    # For legacy setuptools + sdist.
    if sys.version_info[0:2] < (3, 3):
        INSTALL_REQUIRES.append('mock')
else:
    EXTRAS_REQUIRE[":python_version<'3.3'"] = ['mock']


if __name__ == '__main__':
    setup(
        name='slackelot',
        version='0.0.1',
        description='A simple wrapper around the Slack web api to post messages',
        long_description=long_description,
        url='https://github.com/Chris-Graffagnino/slackelot',
        author='Chris Graffagnino',
        author_email='graffwebdev@gmail.com',
        license='MIT',
        keywords='slack',
        python_requires='>=2.7',
        classifiers=CLASSIFIERS,
        install_requires=INSTALL_REQUIRES,
        extras_require=EXTRAS_REQUIRE,
        packages=PACKAGES,
    )
