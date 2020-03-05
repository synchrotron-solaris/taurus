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

"""
This module contains some Taurus-wide default configurations.

The idea is that the final user may edit the values here to customize certain
aspects of Taurus.
"""

#: A map for using custom widgets for certain devices in TaurusForms. It is a
#: dictionary with the following structure:
#: device_class_name:(classname_with_full_module_path, args, kwargs)
#: where the args and kwargs will be passed to the constructor of the class
T_FORM_CUSTOM_WIDGET_MAP = \
    {'SimuMotor': ('sardana.taurus.qt.qtgui.extra_pool.PoolMotorTV', (), {}),
     'Motor': ('sardana.taurus.qt.qtgui.extra_pool.PoolMotorTV', (), {}),
     'PseudoMotor': ('sardana.taurus.qt.qtgui.extra_pool.PoolMotorTV', (), {}),
     'PseudoCounter': ('sardana.taurus.qt.qtgui.extra_pool.PoolChannelTV', (), {}),
     'CTExpChannel': ('sardana.taurus.qt.qtgui.extra_pool.PoolChannelTV', (), {}),
     'ZeroDExpChannel': ('sardana.taurus.qt.qtgui.extra_pool.PoolChannelTV', (), {}),
     'OneDExpChannel': ('sardana.taurus.qt.qtgui.extra_pool.PoolChannelTV', (), {}),
     'TwoDExpChannel': ('sardana.taurus.qt.qtgui.extra_pool.PoolChannelTV', (), {}),
     'IORegister': ('sardana.taurus.qt.qtgui.extra_pool.PoolIORegisterTV', (), {})
     }

#: Compact mode for widgets
#: True sets the preferred mode of TaurusForms to use "compact" widgets
T_FORM_COMPACT = False

#: Strict RFC3986 URI names in models.
#: True makes Taurus only use the strict URI names
#: False enables a backwards-compatibility mode for pre-sep3 model names
STRICT_MODEL_NAMES = False


#: Lightweight imports:
#: True enables delayed imports (may break older code).
#: False (or commented out) for backwards compatibility
LIGHTWEIGHT_IMPORTS = False

#: Default scheme (if not defined, "tango" is assumed)
DEFAULT_SCHEME = "tango"

#: Filter old tango events:
#: Sometimes TangoAttribute can receive an event with an older timestamp
#: than its current one. See https://github.com/taurus-org/taurus/issues/216
#: True discards (Tango) events whose timestamp is older than the cached one.
#: False (or commented out) for backwards (pre 4.1) compatibility
FILTER_OLD_TANGO_EVENTS = True

#: Extra Taurus schemes. You can add a list of modules to be loaded for
#: providing support to new schemes 
#: (e.g. EXTRA_SCHEME_MODULES = ['myownschememodule']
EXTRA_SCHEME_MODULES = []

#: Custom formatter. Taurus widgets use a default formatter based on the
#: attribute type, but sometimes a custom formatter is needed.
#: IMPORTANT: setting this option in this file will affect ALL widgets
#: of ALL applications (which is probably **not** what you want, since it 
#: may have unexpected effects in some applications). 
#: Consider using the API for modifying this on a per-widget or per-class
#: basis at runtime, or using the related `--default-formatter` parameter 
#: from TaurusApplication, e.g.:
#:     $ taurus form MODEL --default-formatter='{:2.3f}'
#: The formatter can be a python format string or the name of a formatter
#: callable, e.g.
#: DEFAULT_FORMATTER = '{0}'
#: DEFAULT_FORMATTER = 'taurus.core.tango.util.tangoFormatter'
#: If not defined, taurus.qt.qtgui.base.defaultFormatter will be used


#: Default serialization mode **for the tango scheme**. Possible values are:
#: 'Serial', 'Concurrent', or 'TangoSerial' (default)
TANGO_SERIALIZATION_MODE = 'TangoSerial'

#: PLY (lex/yacc) optimization: 1=Active (default) , 0=disabled.
#: Set PLY_OPTIMIZE = 0 if you are getting yacc exceptions while loading
#: synoptics
PLY_OPTIMIZE = 1

# Taurus namespace  # TODO: NAMESPACE setting seems to be unused. remove?
NAMESPACE = 'taurus'

# ----------------------------------------------------------------------------
# Qt configuration
# ----------------------------------------------------------------------------

#: Set preferred API (if one is not already loaded)
DEFAULT_QT_API = 'pyqt'

#: Auto initialize Qt logging to python logging
QT_AUTO_INIT_LOG = True

#: Remove input hook (only valid for PyQt4)
QT_AUTO_REMOVE_INPUTHOOK = True

#: Avoid application abort on unhandled python exceptions
#: (which happens since PyQt 5.5).
#: http://pyqt.sf.net/Docs/PyQt5/incompatibilities.html#unhandled-python-exceptions
#: If True (or commented out) an except hook is added to force the old
# behaviour (exception is just printed) on pyqt5
QT_AVOID_ABORT_ON_EXCEPTION = True

#: Select the theme to be used: set the theme dir  and the theme name.
#: The path can be absolute or relative to the dir of taurus.qt.qtgui.icon
#: If not set, the dir of taurus.qt.qtgui.icon will be used
QT_THEME_DIR = ''

#: The name of the icon theme (e.g. 'Tango', 'Oxygen', etc). Default='Tango'
QT_THEME_NAME = 'Tango'

#: In Linux the QT_THEME_NAME is not applied (to respect the system theme)
#: setting QT_THEME_FORCE_ON_LINUX=True overrides this.
QT_THEME_FORCE_ON_LINUX = False

#: Full Qt designer path (including filename. Default is None, meaning:
#: - linux: look for the system designer following Qt.QLibraryInfo.BinariesPath
#: - windows: look for the system designer following
#: Qt.QLibraryInfo.BinariesPath. If this fails, taurus tries to locate binary
#: manually
QT_DESIGNER_PATH = None

#: Custom organization logo. Set the absolute path to an image file to be used as your
#: organization logo. Qt registered paths can also be used. 
#: If not set, it defaults to 'logos:taurus.png" 
#: (note that "logos:" is a Qt a registered path for "<taurus>/qt/qtgui/icon/logos/")
ORGANIZATION_LOGO = "logos:taurus.png"

# ----------------------------------------------------------------------------
# Deprecation handling:
# Note: this API is still experimental and may be subject to change
# (hence the "_" in the options)
# ----------------------------------------------------------------------------

#: set the maximum number of same-message deprecations to be logged.
#: None (or not set) indicates no limit. -1 indicates that an exception should
#: be raised instead of logging the message (useful for finding obsolete code)
_MAX_DEPRECATIONS_LOGGED = 1

