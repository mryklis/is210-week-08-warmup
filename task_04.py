#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module measures input length and formats string."""


MYINPUT = raw_input('Tell me a story! ')
MAX_LENGTH = 80
LONGSTR = 'short'

# You code goes here

story = len(MYINPUT)

if story > MAX_LENGTH:
	LONGSTR = 'long'
	


OUTPUT = 'That certainly was a {} story!'.format(LONGSTR)
print OUTPUT
