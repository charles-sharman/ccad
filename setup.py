"""
Description
-----------
distutils setup.py for ccad.  View model.py for a full description of
ccad.

Author
------
View AUTHORS.

License
-------
Distributed under the GNU LESSER GENERAL PUBLIC LICENSE Version 3.
View LICENSE for details.
"""

import os, sys, glob

import distutils.core
import distutils.dir_util
import distutils.sysconfig

name = 'ccad'
version = '0.11' # Change also in display.py, doc/conf.py

# Include the documentation
prefix = 'share/doc/ccad/' # Don't like including the share prefix.
                           # Probably too linux-specific ***
data_files = [(prefix + 'html', glob.glob('doc/html/*.html')),
              (prefix + 'html/_images', glob.glob('doc/html/_images/*')),
              (prefix + 'html/_static', glob.glob('doc/html/_static/*')),
              (prefix + 'html/_sources', glob.glob('doc/html/_sources/*'))]

# Install the module
distutils.core.setup(name = name,
                     version = version,
                     url = 'UNKNOWN',
                     py_modules = ['ccad.model', 'ccad.display'],
                     package_dir = {'ccad': '.'},
                     data_files = data_files,
#                     requires = ['OCC', 'gtk']
                     requires = ['OCC', 'PyQt4']
                     )
