# Lesson 3 exercise
# Fill in each TODO. From the project root, with the venv activated:
#   mypy
#   python lessons/lesson03_unions_and_pattern_matching/exercise.py

from dataclasses import dataclass
from typing import assert_never

# TODO 1: write a function `format_value` that takes `value: str | int | bool` and
# returns a str:
#   - if it's a str, return it uppercased
#   - if it's a bool, return "yes" or "no"
#   - if it's an int, return it formatted to 2 decimal places (f"{value:.2f}")
# Use match/case. Remember: check the bool case BEFORE the int case, since bool is
# a subclass of int in Python — see the README for why that ordering matters.


# TODO 2: call `format_value` with one str, one int, and one bool argument,
# printing each result.


# TODO 3: define three dataclasses for shapes:
#   Circle: radius: float
#   Rectangle: width: float, height: float
#   Triangle: base: float, height: float
# Then: Shape = Circle | Rectangle | Triangle
# (Use 3.14159 for circle area: 3.14159 * radius^2. Rectangle: width * height.
#  Triangle: 0.5 * base * height.)


# TODO 4: write a function `area` that takes a `Shape` and returns its area as a
# float, using match/case on the shape's class (as shown in the README — no "kind"
# field needed). Add a `case _:` wildcard branch calling `assert_never` for
# exhaustiveness checking.


# TODO 5: create one of each shape (a circle, a rectangle, a triangle) and print
# the area of each using your `area` function.


# TODO 6 (prove exhaustiveness works): temporarily add a 4th dataclass `Square`
# (side: float) to the `Shape` union, WITHOUT adding a case for it in `area`'s
# match. Run `mypy` and read the error pointing at your `assert_never` call. Then
# either add the missing case (return side * side) or revert the Shape union back
# to 3 members — leave the file in a state that passes `mypy`.
