#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module asks the users blood pressure, compares to range and returns fomatted string"""


ASK = raw_input('what is your BP?')
ASK = int(ASK)

LOW = range(0, 89)
IDEAL = range(90,119)
WARNING = range(120,139)
HIGH = range(140, 159)
EMERGENCY = range(160,)

if ASK in LOW:
	BP_STATUS = 'Low'
elif ASK in IDEAL:
	BP_STATUS = 'Ideal'
elif ASK in WARNING:
	BP_STATUS = 'Warning'
elif ASK in HIGH:
	BP_STATUS = 'High'
else:
	BP_STATUS = 'Emergency'

print 'Your status is currently: {}!'.format(BP_STATUS)
