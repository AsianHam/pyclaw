#!/usr/bin/env python
# encoding: utf-8
#  =====================================================================
#  Package:     petclaw
#  File:        __init__.py
#  Created:     Feb 19, 2008
#  Author:      Kyle Mandli
#  ======================================================================
"""Main petclaw package"""

import os
import logging, logging.config

# Default logging configuration file
_DEFAULT_LOG_CONFIG_PATH = os.path.join(os.path.dirname(__file__),'log.config')

# Setup loggers
logging.config.fileConfig(_DEFAULT_LOG_CONFIG_PATH)

__all__ = []

# Module imports
__all__.extend(['Controller','Data','Dimension','Grid','Solution'])
from pyclaw.controller import Controller
from pyclaw.data import Data
from pyclaw.solution import Solution
from petclaw.grid import Dimension 
from petclaw.grid import Grid 

# Sub-packages
#import evolve
#from pyclaw.evolve import *
#__all__.extend(evolve.__all__)
