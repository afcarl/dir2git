#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2014 Mark Lee
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from flake8.engine import get_style_guide
from flake8.main import print_report
import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def main():
    # flake8
    flake8 = get_style_guide(exclude=['.tox', 'build'])
    report = flake8.check_files([BASE_DIR])

    # TODO integration test creating a directory to be git-ified
    return print_report(report, flake8)

if __name__ == '__main__':
    sys.exit(main())
