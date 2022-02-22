"""
Support and convert several CAN (Controller Area Network) database formats .arxml .dbc .dbf .kcd .sym fibex xls(x) ...

Canmatrix implements a "Python Can Matrix Object" which describes the can-communication
and the needed objects (Boardunits, Frames, Signals, Values, ...) Canmatrix also includes
two Tools (canconvert and cancompare) for converting and comparing CAN databases.
There are also some extract and merge options for dealing with can databases.

**supported file formats for import:**

            .dbc candb / Vector

            .dbf Busmaster (open source!)

            .kcd kayak (open source!)

            .arxml autosar system description

            .yaml dump of the python object

            .xls(x) excel xls-import, works with .xls-file generated by this lib

            .sym peak pcan can description

**supported file formats for export:**

            .dbc

            .dbf

            .kcd

            .xls(x)

            .json Canard (open source!)

            .arxml (very basic implementation)

            .yaml (dump of the python object)

            .sym

            .xml (fibex)

"""

classifiers = """\
Development Status :: 4 - Beta
Environment :: Console
License :: OSI Approved :: BSD License
Topic :: Scientific/Engineering
Programming Language :: Python
Programming Language :: Python :: 2.7
Programming Language :: Python :: 3.4
Programming Language :: Python :: 3.5
Programming Language :: Python :: 3.6
Programming Language :: Python :: 3.7
Programming Language :: Python :: 3.8
Programming Language :: Python :: 3.9
Programming Language :: Python :: 3.10
"""

from setuptools import find_packages, setup

import versioneer

doclines = __doc__.split("\n")

setup(
    name = "canmatrix",
    version = versioneer.get_version(),
    cmdclass = versioneer.get_cmdclass(),
    maintainer = "Eduard Broecker",
    maintainer_email = "eduard@gmx.de",
    url = "http://github.com/ebroecker/canmatrix",
    classifiers = list(filter(None, classifiers.split("\n"))),
    description = doclines[0],
    keywords = "CAN dbc arxml kcd dbf sym",
    long_description = "\n".join(doclines[2:]),
    license = "BSD",
    platforms = ["any"],
    install_requires = [
        "attrs>=19.2.0",
        "click",
        "enum34; python_version < '3.4'",
        "future",
        "six",
        "typing; python_version < '3.5'",
    ],
    extras_require = {
        "arxml": ["lxml"],
        "csv": [],
        "dbc": [],
        "dbf": [],
        "fibex": ["lxml"],
        "json": [],
        "kcd": ["lxml"],
        "ldf": ["ldfparser"],
        "odx": ["lxml"],
        "scapy": [],
        "sym": [],
        "test": ["pathlib2; python_version < '3.4'", "pytest"],
        "wireshark": [],
        "xls": ["xlrd", "xlwt"],
        "xlsx": ["xlsxwriter"],
        "yaml": ["pyyaml"],
    },

    packages = find_packages("src"),
    package_dir = {"": "src"},
    package_data = {"canmatrix" : ["tests/*.dbc", "tests/*.arxml", "j1939.dbc"]},
    entry_points={'console_scripts': ['cancompare = canmatrix.cli.compare:cli_compare',
                                      'canconvert = canmatrix.cli.convert:cli_convert']}
)
