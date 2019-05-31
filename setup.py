#!/usr/bin/env python
from __future__ import absolute_import
import os
import sys
from setuptools import setup, find_packages

import pyNastran
from packages import check_python_version, get_package_requirements

add_vtk_qt = True
if 'bdist_wheel' in sys.argv:
    add_vtk_qt = False

check_python_version()
install_requires = get_package_requirements(is_gui=True, add_vtk_qt=add_vtk_qt)
packages = find_packages() + ['gui/icons/*.*']
#print("packages = %s" % packages)

# set up all icons
icon_path = os.path.join('pyNastran', 'gui', 'icons')
icon_files = os.listdir(icon_path)
icon_files2 = []
for icon_file in icon_files:
    if icon_file.endswith('.png'):
        icon_files2.append(os.path.join(icon_path, icon_file))

exclude_words = []
packages = find_packages(exclude=['ez_setup', 'examples', 'tests'] + exclude_words)
for exclude_word in exclude_words:
    packages = [package for package in packages if exclude_word not in package]
#print(packages, len(packages)) # 83

setup(
    name='pyNastran',
    version=pyNastran.__version__,
    description=pyNastran.__desc__,
    long_description=pyNastran.__longdesc__,
    classifiers=[
        'Natural Language :: English',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        ], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    python_requires='>2.7.6, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, !=3.5.*',
    author=pyNastran.__author__,
    author_email=pyNastran.__email__,
    url=pyNastran.__website__,
    license=pyNastran.__license__,
    packages=packages,
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    #{'': ['license.txt']}
    #package_data={'': ['*.png']},
    #data_files=[(icon_path, icon_files2)],
    package_data={
        # https://pythonhosted.org/setuptools/setuptools.html#including-data-files
        # If any package contains *.png files, include them:
        '': ['*.png'],
        #'mypkg': ['data/*.dat'],
    },
    entry_points={
        'console_scripts': [
            #'run_nastran_double_precision = pyNastran.bdf.test.run_nastran_double_precision:cmd_line',
            'test_bdf  = pyNastran.bdf.test.test_bdf:main',
            'test_op2  = pyNastran.op2.test.test_op2:main',
            'test_op4  = pyNastran.op4.test.test_op4:main',
            #'test_abaqus = pyNastran.converters.abaqus.test_abaqus:main',
            'test_pynastrangui = pyNastran.gui.test.test_gui:main',

            'format_converter = pyNastran.converters.type_converter:cmd_line_format_converter',
            'pyNastranGUI = pyNastran.gui.gui:cmd_line',
            'bdf = pyNastran.bdf.mesh_utils.utils:cmd_line',
            'f06 = pyNastran.f06.utils:cmd_line',

            #'pyNastranv = pyNastran.dev.bdf_vectorized.solver.solver:main',
            #'test_bdfv = pyNastran.dev.bdf_vectorized.test.test_bdf_vectorized2:main',
            #'nastran_to_code_aster = pyNastran.converters.dev.code_aster.nastran_to_code_aster:main',
        ]
    },
    test_suite='pyNastran.all_tests',
)
