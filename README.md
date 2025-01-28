# Slides

https://github.com/wolever/2025-python-toronto-new-in-python


## `pyproject.toml`

The `pyproject.toml` file is the modern standard for Python project metadata.

It contains both package dependencies and tooling configuration.

Created with `uv init`, `poetry new`, etc.


## UV

``uv`` is the new "hotness" in Python interpreter and package management:
https://github.com/astral-sh/uv

```bash
$ curl -LsSf https://astral.sh/uv/install.sh | baish
```

It can be used as a (mostly) drop-in replacement for ``pip`` and ``venv``,
except it's blindingly fast.

Installing Python 3.13 (0.42 seconds):

```bash
$ time uv python install 3.13
Installed Python 3.13.0rc2 in 1.60s
 + cpython-3.13.0rc2-macos-aarch64-none

0.24s user 0.42s system 40% cpu 1.618 total
```

Initializing this package's virtual environment (0.13 seconds):

```bash
$ time uv sync
Using Python 3.13.0rc2
Creating virtual environment at: .venv
Resolved 13 packages in 0.77ms
Installed 12 packages in 146ms
 + annotated-types==0.7.0
 + certifi==2024.12.14
 + charset-normalizer==3.4.1
 + idna==3.10
 + nodeenv==1.9.1
 + pydantic==2.10.6
 + pydantic-core==2.27.2
 + pyright==1.1.392.post0
 + requests==2.32.3
 + ruff==0.9.3
 + typing-extensions==4.12.2
 + urllib3==2.3.0

0.04s user 0.13s system 78% cpu 0.210 total
```

Installing from an existing `requirements.txt` (0.03 seconds):

```bash
$ uv venv
$ time uv pip sync ./requirements.txt
time uv pip sync ./requirements.txt
Resolved 5 packages in 1ms
Installed 5 packages in 7ms
 + firebase-admin==5.0.0
 + flask==2.1.0
 + flask-cors==3.0.10
 + gunicorn==20.1.0
 + werkzeug==2.3.8
0.01s user 0.03s system 115% cpu 0.032 total
```


## ruff

`ruff` is a linter and formatter compatible with `black`, but substantially
faster.

For example, in a large (~100k lines) project (0.03 seconds):

```bash
$ time uvx ruff check ./app/
time ruff check app

0.02s user 0.03s system 198% cpu 0.022 total
```

## repl improvements

https://docs.python.org/3/whatsnew/3.13.html#whatsnew313-better-interactive-interpreter

```python
>>> def foo():
...     raise Exception()
...
>>> foo()
Traceback (most recent call last):
  File "<python-input-1>", line 1, in <module>
    foo()
    ~~~^^
  File "<python-input-0>", line 2, in foo
    raise Exception()
Exception
>>>
```

(... but ipython / jupyterlab is still better for interactive use)

## `python -m sqlite3`

SQLite3 databases can be opened with stock python!

```bash
$ python -m sqlite3 holidays.sqlite3
sqlite> SELECT * FROM holidays limit 10;
('evangelic', 'TH', 'GREGORIAN', 0, 0, 'AbsoluteDate', 1, 23, None, None, None, None, None, None, None, None)
('evangelic', 'CL', 'GREGORIAN', 0, 0, 'AbsoluteDate', 10, 31, None, None, None, None, None, None, None, None)
('evangelic', 'default', 'GREGORIAN', 0, 0, 'AbsoluteDate', 1, 23, None, None, None, None, None, None, None, None)
('evangelic', 'BR', 'GREGORIAN', 0, 0, 'AbsoluteDate', 1, 23, None, None, None, None, None, None, None, None)
('stjoseph', 'MX', 'GREGORIAN', 0, 0, 'AbsoluteDate', 3, 19, None, None, None, None, None, None, None, None)
('stjoseph', 'default', 'JULIAN', 2021, 0, 'DateList', 12, 26, None, None, None, None, None, None, None, None)
('stjoseph', 'default', 'JULIAN', 2009, 0, 'DateList', 12, 27, None, None, None, None, None, None, None, None)
('stjoseph', 'default', 'JULIAN', 2019, 0, 'DateList', 12, 29, None, None, None, None, None, None, None, None)
('stjoseph', 'default', 'JULIAN', 2012, 0, 'DateList', 12, 30, None, None, None, None, None, None, None, None)
('stjoseph', 'default', 'JULIAN', 2015, 0, 'DateList', 12, 27, None, None, None, None, None, None, None, None)
```

(although note that not all SQLite3 features are supported; for example, `.tables`, `.dump`, etc)

## `cgi` has been removed from the standard library 😢

To keep living the dream of ftp-ing files to your apache server, the `standard-cgi` package is available:

```bash
$ pip install standard-cgi
```
