trellis
=======
An experiment in building a CLI for trello

Development Installation
========================

You should run this in a venv. Do something like this:

```
$ python3 -m venv ~/venv3
$ . ~/venv3/bin/activate
$ mkdir -p ~/src
$ git clone https://github.com/mrda/trellis.git
$ cd trellis
$ pip install -U pip
$ pip install -Ur requirements.txt
$ pip install -e .
```

Installing a Release
====================

That's what pypi is for!

```
$ pip install --user trellis
# Note: This will only work once a release is pushed to pypi :-)
# For now, use the Development Installation
```

Usage
=====
TBD
