#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module performs conditional testing."""


EXPENSE = 14.23
LOOKS_NICE = True
MAX_EXPENSE = 12
GET_OUT_ALIVE = False

if LOOKS_NICE and EXPENSE <= MAX_EXPENSE:
	SACRIFICE = 'True'
elif not GET_OUT_ALIVE:
	SACRIFICE = 'False'

print SACRIFICE
