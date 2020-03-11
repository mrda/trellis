#
# trellis top-level Makefile
#
# Copyright (C) 2020 Michael Davies <michael@the-davies.net>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA
# 02111-1307, USA.
#

NOSE=nosetests
GIT_CHANGES=$(shell git ls-files -m)

.PHONY: all tests clean check changes cover install uninstall

all: check tests changes

install:
	pip install --user -Ur requirements.txt .

uninstall:
	pip uninstall trellis

check:
	pycodestyle --show-source trellis tests

changes:
	@if [ ! "z$(GIT_CHANGES)" = "z" ]; then \
		printf "\n     **************************************************\n"; \
		printf "     * You have modified files in this repository.    *\n"; \
		printf "     * Before commiting these changes, have you upped *\n"; \
		printf "     * the version in setup.py ?                      *\n"; \
		printf "     **************************************************\n\n\n"; \
    else true; fi

tests:
	${NOSE} -s --with-coverage --cover-branches --cover-erase --cover-html --cover-package=trellis

cover:
	xdg-open cover/index.html

clean:
	find . -iname "*.pyc" -o -iname "*.pyo" -o -iname "*.so" \
           -o -iname "#*#" -delete

