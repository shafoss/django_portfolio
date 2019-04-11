# -*- coding: utf-8 -*-
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ENVIRONMENT_NAME = 'TESTING'
ENVIRONMENT_COLOR = 'YELLOW'

FIXTURE_DIRS = (
    os.path.join(BASE_DIR, 'fixtures'),
)
