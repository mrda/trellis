NOSE=nosetests

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
        printf "\n*** You have modified files in this repository.\n"; \
    else true; fi

tests:
	${NOSE} -s --with-coverage --cover-branches --cover-erase --cover-html --cover-package=trellis

cover:
	xdg-open cover/index.html

clean:
	find . -iname "*.pyc" -o -iname "*.pyo" -o -iname "*.so" \
           -o -iname "#*#" -delete

