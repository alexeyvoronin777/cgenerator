""" cgenerator
~~~~~~~~~~
Tests for main module.
:copyright: 2016 by Alexey Voronin.
:license: GPL, see LICENSE for more details.
"""

#!/usr/bin/env

import pytest
from cgenerator import cgenerator


def test_first():
	assert cgenerator.calc(2) == 4
	
	
