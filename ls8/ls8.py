#!/usr/bin/env python3

"""Main."""

import sys
from cpu import *
# from josh import *

cpu = CPU()

# cpu.load('ls8/examples/sctest.ls8')
cpu.load()
cpu.run()