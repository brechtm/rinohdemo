#!/usr/bin/python

import os
import sys

OPENSHIFT_PYTHON_DIR = os.environ.get('OPENSHIFT_PYTHON_DIR','.')

virtenv = os.path.join(OPENSHIFT_PYTHON_DIR, 'virtenv')
python_version = 'python{}.{}'.format(*sys.version_info)
PYTHON_EGG_CACHE = os.path.join(virtenv, 'lib', python_version,
								'site-packages')
os.environ['PYTHON_EGG_CACHE'] = PYTHON_EGG_CACHE
virtualenv = os.path.join(virtenv, 'bin','activate_this.py')
try:
	exec(open(virtualenv).read(), dict(__file__=virtualenv))
except IOError:
	pass

from flaskapp import app as application
