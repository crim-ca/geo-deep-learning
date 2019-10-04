#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os
import sys
ROOT = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, ROOT)

README = ""
with open('README.md') as readme_file:
    README = readme_file.read()  # noqa

HISTORY = ""
#with open('HISTORY.md') as history_file:
#    HISTORY = history_file.read()  # noqa


def _parse_requirements(file_path, requirements, links):
    with open(file_path, 'r') as requirements_file:
        for line in requirements_file:
            if 'git+https' in line:
                pkg = line.split('#')[-1]
                links.add(line.strip())
                requirements.add(pkg.replace('egg=', '').rstrip())
            elif line.startswith('http'):
                links.add(line.strip())
            else:
                requirements.add(line.strip())


# See https://github.com/pypa/pip/issues/3610
# use set to have unique packages by name
LINKS = set()
REQUIREMENTS = set()
TEST_REQUIREMENTS = set()
_parse_requirements('requirements.txt', REQUIREMENTS, LINKS)
#_parse_requirements('requirements-py{}.txt'.format(sys.version[0]), REQUIREMENTS, LINKS)
#_parse_requirements('requirements-dev.txt', TEST_REQUIREMENTS, LINKS)
LINKS = list(LINKS)
REQUIREMENTS = list(REQUIREMENTS)
TEST_REQUIREMENTS = list(TEST_REQUIREMENTS)

raw_requirements = set()
for req in REQUIREMENTS:
    raw_req = req.split('>')[0].split('=')[0].split('<')[0].split('!')[0]
    raw_requirements.add(raw_req)
filtered_test_requirements = set()
for req in TEST_REQUIREMENTS:
    raw_req = req.split('>')[0].split('=')[0].split('<')[0].split('!')[0]
    if raw_req not in raw_requirements:
        filtered_test_requirements.add(req)
TEST_REQUIREMENTS = list(filtered_test_requirements)

PKG_ROOT = ""
PKG_NAME = "geo_deep_learning"
setup(
    # -- meta information --------------------------------------------------
    # all found via setup.cfg
    # -- Package structure -------------------------------------------------
    packages=find_packages(),
    package_dir={"": "."},
    package_data={"": ["conf", "data"]},
    include_package_data=False,
    install_requires=REQUIREMENTS,
    dependency_links=LINKS,
    zip_safe=False,
    # -- self - tests --------------------------------------------------------
    #test_suite='tests',
    #tests_require=TEST_REQUIREMENTS,
    # -- script entry points -----------------------------------------------
    #entry_points="""\
    #      [paste.app_factory]
    #      main = cli:main
    #      [console_scripts]
    #      """,
)
