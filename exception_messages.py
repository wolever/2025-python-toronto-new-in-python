"""
Python 3.11 introduces substantial improvements to error messages.

For example, historically an exception might look like this:

    >>> distance(Point(1, 2), Point(None, 4))
    Traceback (most recent call last):
      ...
      File "../error_message_examples.py", line 13, in distance
        return sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2)
    TypeError: unsupported operand type(s) for -: 'NoneType' and 'int'

But which of `a.x` or `b.x` is `None`?
"""

from dataclasses import dataclass
from math import sqrt


@dataclass
class Point:
    x: float
    y: float

def distance(a: Point, b: Point) -> float:
    return sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2)


distance(Point(1, 2), Point(None, 4))
"""
But now:

    Traceback (most recent call last):
      File "../error_message_examples.py", line 29, in <module>
        distance(Point(1, 2), Point(None, 4))
        ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "../error_message_examples.py", line 26, in distance
        return sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2)
                     ~~~~^~~~~
    TypeError: unsupported operand type(s) for -: 'int' and 'NoneType'
"""
