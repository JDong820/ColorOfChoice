from setuptools import setup, find_packages
from color_names import __version__
import sys

if sys.version_info <= (3, 0):
    print("ERROR: color_names requires Python 3.0 or later "
          "(bleeding edge preferred)", file=sys.stderr)
    sys.exit(1)

with open('README.md') as f:
    long_description = f.read()

setup(
    name="color_names",
    version=__version__,
    description="Translate color names to specific values.",
    long_description=long_description,
    url="https://github.com/jdongian/python-color_names",
    install_requires=[
        "colour >= 0.1.2"
    ],
    author="Joshua Dong",
    author_email="jdong42@gmail.com",
    license="http://www.apache.org/licenses/LICENSE-2.0",
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
    ],
    keywords="color name colour naming conversion RGB CMYK HEX",
    packages=find_packages(),
    package_dir={'color_names': 'color_names'}#,
    #package_data={'color_names': ['data/*.json']},
)
