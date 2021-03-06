#!/usr/bin/env python

#############################################################################
##
# This file is part of Taurus
##
# http://taurus-scada.org
##
# Copyright 2011 CELLS / ALBA Synchrotron, Bellaterra, Spain
##
# Taurus is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
##
# Taurus is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
##
# You should have received a copy of the GNU Lesser General Public License
# along with Taurus.  If not, see <http://www.gnu.org/licenses/>.
##
#############################################################################

from __future__ import print_function
print("*" * 77)
print("""
If you are seeing this, it is because you tried to access qwtplot.py directly.
All funcionality has been moved to taurusplot.py, taurustrend.py and scales.py

The recommended way of accessing the classes that were in qwtplot.py is by
importing them from taurus.qt.qtgui.plot

If you were trying to launch a stand-alone Taurusplot or TaurusTrend from a script,
you should update such script.
""")
print("*" * 77)
