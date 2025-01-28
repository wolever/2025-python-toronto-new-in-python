"""
f-strings - `f"Hello, {name}"` - are one of the best features to come to Python,
but historically they had some limitations:

```python
>>> names = ["foo", "bar"]
>>> f"Hello, {", ".join(names)}"
File "<stdin>", line 1
    f"Hello, {", ".join(names)}"
               ^
SyntaxError: f-string: expecting '}'
```

As of 3.12, f-strings work the way you would expect.
"""

# Nested quots
names = ["foo", "bar"]
print(f"Hello, {", ".join(names)}")


# Multi-line f-strings
print(f"Hello, {", ".join([
    "foo",
    "bar",
    "baz",
])}")

# f-strings that contain \-escapes
print(f"Hello:\n{"\n".join([
    "foo",
    "bar",
    "baz",
])}")


# And exceptions have the same helpful error messages
#print(f"Hello, {foo bar}")
#"""
#    File "f_strings.py", line 37
#        print(f"Hello, {foo bar}")
#                        ^^^^^^^
#    SyntaxError: invalid syntax. Perhaps you forgot a comma?
#"""

# Bonus tip: using !r
name = "foo"
print(f"Hello, {name!r}")
# -> "Hello, 'foo'"

# Bonus tip: number formatting
# f: float
# .1: round to 1 decimal place
print(f"{1.259:.1f}")
# -> "1.3"

# ,: comma separator
print(f"{123456:,}")
# -> "123,456"

# %: format as a percentage
# .2: round to 2 decimal places
print(f"{0.25:.2%}")
# -> "25.00%"
