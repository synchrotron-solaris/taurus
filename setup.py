#!/usr/bin/env python

##############################################################################
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
##############################################################################

import os
import imp
import sys
from distutils.version import LooseVersion
from setuptools import setup, find_packages, __version__


def get_release_info():
    name = "release"
    setup_dir = os.path.dirname(os.path.abspath(__file__))
    release_dir = os.path.join(setup_dir, 'lib', 'taurus', 'core')
    data = imp.find_module(name, [release_dir])
    ret = imp.load_module(name, *data)
    return ret

release = get_release_info()

package_dir = {'': 'lib'}

packages = find_packages(where='lib')

provides = [
    'taurus',
    # 'taurus.core',
    # 'taurus.qt',
    # 'Taurus-Tango',  # [Taurus-Tango]
    # 'Taurus-Qt',  # [Taurus-Qt]
    # 'Taurus-Qt-PyQwt',  # [Taurus-Qt-Plot]
    # 'Taurus-Qt-Synoptic',  # [Taurus-Qt-Synoptic]
    # 'Taurus-Qt-TaurusGUI',  # [Taurus-Qt-TaurusGUI]
    # 'Taurus-Qt-Editor',  # [Taurus-Qt-Editor] --> or maybe move it to sardana
    # 'Taurus-Qt-Guiqwt',  # [Taurus-Qt-Guiqwt]
]

install_requires = [
    'numpy>=1.1',
    'pint>=0.8',
    'future',
    'click',
]

#Workaround for old setuptools

if LooseVersion(__version__) < LooseVersion('20.2'):
    if sys.version_info < (3, 4):
        install_requires.append('enum34')
else:
    install_requires.append('enum34;python_version<"3.4"')


extras_require = {
    'taurus-qt': [# 'PyQt4 >=4.8',
                  # 'PyQt4.Qwt5 >=5.2.0',  # [Taurus-Qt-Plot]
                  'ply >=2.3',  # [Taurus-Qt-Synoptic]
                  'lxml >=2.1',  # [Taurus-Qt-TaurusGUI]
                  'guiqwt >=3',  # [Taurus-Qt-Guiqwt]
                  ],
    'taurus-tango': ['PyTango >=7.1',
                     ],
    'taurus-epics': ['pyepics >=3.2.4',
                     ],
    'taurus-h5file': ['h5file',
                      ],
    # separate the editor from 'taurus-qt' to avoid forcing spyder>3
    # which implies many more dependencies that may be hard on older system
    'taurus-qt-editor': ['spyder >=3',
                         ],
}

console_scripts = [
    'taurus = taurus.cli:main',
]

taurus_subcommands = [
    'testsuite = taurus.test.testsuite:testsuite_cmd',
    'config = taurus.qt.qtgui.panel.taurusconfigeditor:config_cmd',
    'qwt5 = taurus.qt.qtgui.qwt5.cli:qwt5',
    'device = taurus.qt.qtgui.panel.taurusdevicepanel:device_cmd',
    'panel = taurus.qt.qtgui.panel.taurusdevicepanel:panel_cmd',
    'gui = taurus.qt.qtgui.taurusgui.taurusgui:gui_cmd',
    'newgui = taurus.qt.qtgui.taurusgui.taurusgui:newgui_cmd',
    'designer = taurus.qt.qtdesigner.taurusdesigner:designer_cmd',
    'guiqwt = taurus.qt.qtgui.extra_guiqwt.cli:guiqwt',
    'icons = taurus.qt.qtgui.icon.catalog:icons_cmd',
    'form = taurus.qt.qtgui.panel.taurusform:form_cmd',
    'demo = taurus.qt.qtgui.panel.taurusdemo:demo_cmd',
    'logmon = taurus.core.util.remotelogmonitor:logmon_cmd',
    'qlogmon = taurus.qt.qtgui.table.qlogtable:qlogmon_cmd',
    'check-deps = taurus.core.taurushelper:check_dependencies_cmd'
]

model_selectors = [
    'Tango = taurus.qt.qtgui.panel.taurusmodelchooser:TangoModelSelectorItem',
]

formatters = [
    'taurus = taurus.qt.qtgui.base:defaultFormatter',
    'tango = taurus.core.tango.util:tangoFormatter',
    '{:2.3e} = taurus.qt.qtgui.base:expFormatter',
    '{:.5f} = taurus.qt.qtgui.base:floatFormatter',
]

entry_points = {
    'console_scripts': console_scripts,
    'taurus.cli.subcommands': taurus_subcommands,
    'taurus.qt.qtgui.panel.TaurusModelSelector.items': model_selectors,
    'taurus.qt.formatters': formatters,
}

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Console',
    'Environment :: X11 Applications :: Qt',
    'Environment :: Win32 (MS Windows)',
    'Intended Audience :: Developers',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
    'Natural Language :: English',
    'Operating System :: Microsoft :: Windows',
    'Operating System :: POSIX',
    'Operating System :: POSIX :: Linux',
    'Operating System :: Unix',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.5',
    'Topic :: Scientific/Engineering',
    'Topic :: Software Development :: Libraries',
    'Topic :: Software Development :: User Interfaces',
    'Topic :: Software Development :: Widget Sets',
]


setup(name='taurus',
      version=release.version,
      description=release.description,
      long_description=release.long_description,
      author=release.authors['Tiago_et_al'][0],
      maintainer=release.authors['Community'][0],
      maintainer_email=release.authors['Community'][1],
      url=release.url,
      download_url=release.download_url,
      platforms=release.platforms,
      license=release.license,
      keywords=release.keywords,
      packages=packages,
      package_dir=package_dir,
      classifiers=classifiers,
      include_package_data=True,
      entry_points=entry_points,
      provides=provides,
      install_requires=install_requires,
      extras_require=extras_require,
      test_suite='taurus.test.testsuite.get_taurus_suite',
      )
