"""
Exception grouping provides built-in support for handling multiple exceptions
at once.

This is mostly useful for concurrent/asynchronous code, where a caller may be
waiting on the result of multiple tasks.

https://docs.python.org/3/tutorial/errors.html#raising-and-handling-multiple-unrelated-exceptions
"""


from typing import Callable


def run_functions[T](functions: list[Callable[[], T]]) -> list[T]:
    # This is an example; in practice it would likely be `asyncio.gather`
    # or `concurrent.futures.ThreadPoolExecutor`.
    results = []
    exceptions = []

    for func in functions:
        try:
            results.append(func())
        except Exception as e:
            exceptions.append(e)

    if exceptions:
        raise ExceptionGroup("Multiple exceptions occurred", exceptions)

    return results


#run_functions([
#    lambda: None.foo(),
#    lambda: 1 / 0,
#    lambda: "a" + 42,
#])

"""
  + Exception Group Traceback (most recent call last):
  |   File "exception_grouping.py", line 33, in <module>
  |     run_functions([
  |     ~~~~~~~~~~~~~^^
  |         lambda: None.foo(),
  |         ^^^^^^^^^^^^^^^^^^^
  |         lambda: 1 / 0,
  |         ^^^^^^^^^^^^^^
  |         lambda: "a" + 42,
  |         ^^^^^^^^^^^^^^^^^
  |     ])
  |     ^^
  |   File "exception_grouping.py", line 28, in run_functions
  |     raise ExceptionGroup("Multiple exceptions occurred", exceptions)
  | ExceptionGroup: Multiple exceptions occurred (3 sub-exceptions)
  +-+---------------- 1 ----------------
    | Traceback (most recent call last):
    |   File "exception_grouping.py", line 23, in run_functions
    |     results.append(func())
    |                    ~~~~^^
    |   File "exception_grouping.py", line 34, in <lambda>
    |     lambda: None.foo(),
    |             ^^^^^^^^
    | AttributeError: 'NoneType' object has no attribute 'foo'
    +---------------- 2 ----------------
    | Traceback (most recent call last):
    |   File "exception_grouping.py", line 23, in run_functions
    |     results.append(func())
    |                    ~~~~^^
    |   File "exception_grouping.py", line 35, in <lambda>
    |     lambda: 1 / 0,
    |             ~~^~~
    | ZeroDivisionError: division by zero
    +---------------- 3 ----------------
    | Traceback (most recent call last):
    |   File "exception_grouping.py", line 23, in run_functions
    |     results.append(func())
    |                    ~~~~^^
    |   File "exception_grouping.py", line 36, in <lambda>
    |     lambda: "a" + 42,
    |             ~~~~^~~~
    | TypeError: can only concatenate str (not "int") to str
    +------------------------------------
"""

def catch_group_example():
    try:
        run_functions([
            lambda: None.foo(),
            lambda: 1 / 0,
            lambda: "a" + 42,
        ])
    except* ZeroDivisionError as e:
        print("Got ZeroDivisionErrors:")
        print("  ", e.exceptions)
    except* AttributeError as e:
        print("Got AttributeErrors:")
        print("  ", e.exceptions)
    except* TypeError as e:
        print("Got TypeErrors:")
        print("  ", e.exceptions)


catch_group_example()
