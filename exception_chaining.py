"""
Exception chaining

https://docs.python.org/3/tutorial/errors.html#exception-chaining

When one exception is raised and it leads to another exception, the exceptions
are automatically chained.
"""

class ExceptionA(Exception):
    pass

class ExceptionB(Exception):
    pass

def raise_exception_a():
    raise ExceptionA("A")

def raise_exception_b(from_none: bool = False, from_explicit: bool = False):
    try:
        raise_exception_a()
    except Exception as e:
        if from_none:
            raise ExceptionB("B") from None
        elif from_explicit:
            raise ExceptionB("B") from e
        raise ExceptionB("B")

# By default, exceptions are chained
#raise_exception_b()

# And in some situations - like when multiple exceptions may be involved - it
# can be useful to explicitly chain exceptions.
#raise_exception_b(from_explicit=True)

"""
    Traceback (most recent call last):
      File "exception_chaining.py", line 21, in raise_exception_b
        raise_exception_a()
        ~~~~~~~~~~~~~~~~~^^
      File "exception_chaining.py", line 17, in raise_exception_a
        raise ExceptionA("A")
    ExceptionA: A

    During handling of the above exception, another exception occurred:

    Traceback (most recent call last):
      File "exception_chaining.py", line 25, in <module>
        raise_exception_b()
        ~~~~~~~~~~~~~~~~~^^
      File "exception_chaining.py", line 23, in raise_exception_b
        raise ExceptionB("B")
    ExceptionB: B
"""

# Chaining can be disabled by explicitly raising from `None`
#raise_exception_b(from_none=True)

"""
Traceback (most recent call last):
  File "exception_chaining.py", line 53, in <module>
    raise_exception_b(from_none=True)
    ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^
  File "exception_chaining.py", line 24, in raise_exception_b
    raise ExceptionB("B") from None
ExceptionB: B
"""
