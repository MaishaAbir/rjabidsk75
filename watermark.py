# RJ ABID SK 2014-2015

# IPython magic function to print date/time stamps and

# various system information.

# Author: RJ ABID SK <rjabidsk75.com>

#

# License: BSD 3 clause

from setuptools import setup, find_packages

import os

import watermark

VERSION = watermark.__version__

setup(

    name='watermark',

    version=VERSION,

    license='newBSD',

    description=('IPython magic function to print date/time stamps and'

                 'various system information.'),

    author='Sebastian Raschka',

    author_email='mail@rjabidsk75.com',

    url='https://github.com/rjabidsk75/watermark',

    packages=find_packages(exclude=[]),

    install_requires=['ipython'],

    long_description="""

An IPython magic extension for printing date and time stamps, version numbers,

and hardware information.

Contact

=============

If you have any questions or comments about watermark,

please feel free to contact me via

email: mail@sebastianraschka.com

☆WhatsApp: +8801863517912

This project is hosted at https://github.com/rjabidsk75/watermark

The documentation can be found at

https://github.com/rjabidsk75/watermark/blob/master/README.md

"""

)

