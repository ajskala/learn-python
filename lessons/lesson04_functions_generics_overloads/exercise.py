# Lesson 4 exercise
# Fill in each TODO. From the project root, with the venv activated:
#   mypy
#   python lessons/lesson04_functions_generics_overloads/exercise.py

from collections.abc import Sized
from typing import overload

# TODO 1: write a function `describe_item` that takes (name: str, quantity: int =
# 1, and a keyword-only `note: str | None = None`) and returns a str like
# "5x widget (backordered)" or "1x widget" if no note is given. Give it an
# explicit -> str return type. Remember: `note` must be keyword-only (use a bare
# `*` in the signature before it).


# TODO 2: call `describe_item` three ways: with just a name, with a name and
# quantity, and with a name, quantity, and note (note MUST be passed as
# note=..., not positionally). Print all three results.


# TODO 3: write a function `total` that takes any number of int arguments via
# `*args` and returns their sum. Call it with 0, 2, and 4 arguments and print
# each result.


# TODO 4: write a generic function `first_element` (PEP 695 syntax: `def
# first_element[T](...)`) that takes `items: list[T]` and returns `T | None`.
# Call it once with a list of ints and once with a list of strs, printing both
# results.


# TODO 5: write a generic function `get_length` constrained to `Sized` (`def
# get_length[T: Sized](item: T) -> int`) that returns `len(item)`. Call it with a
# str and with a list, printing both results.


# TODO 6: write a generic class `Box` (PEP 695 syntax: `class Box[T]:`) with an
# `__init__` taking `contents: T` and a `get_contents(self) -> T` method. Create
# one Box holding a str and one holding an int, and print both `.get_contents()`
# results.


# TODO 7: write an overloaded function `combine` using `@overload`:
#   - two @overload signatures: (a: str, b: str) -> str, and (a: int, b: int) -> int
#   - one real implementation covering both, that concatenates strs or adds ints
#     depending on which case applies (use isinstance checks)
# Call it once with two strs and once with two ints, printing both results. Then
# (don't leave this in the file — just try it and delete it) attempt
# `combine("a", 1)` and confirm `mypy` rejects it, proving the overloads are doing
# real work compared to a plain `str | int` union parameter.
