# Lesson 2 exercise
# Fill in each TODO. From the project root, with the venv activated:
#   mypy
#   python lessons/lesson02_classes_dataclasses_protocols/exercise.py

from dataclasses import dataclass
from typing import Protocol

# TODO 1: define a @dataclass `Book` with:
#   title: str
#   author: str
#   year: int
#   isbn: str | None = None   (optional, defaults to None)


# TODO 2: create a variable `my_book` of type `Book` with title/author/year filled
# in (leave isbn as its default).


# TODO 3: write a function `describe_book` that takes a `Book` and returns a str
# like "Dune by Frank Herbert (1965)". Give it an explicit -> str return type.


# TODO 4: define a @dataclass `EBook` that inherits from `Book` and adds:
#   file_size_mb: float = 0.0
# Then create a variable `my_ebook` of type `EBook` with all fields filled in.


# TODO 5: call `describe_book` with both `my_book` and `my_ebook` and print the
# results. (This works because EBook IS a Book via inheritance — this is Python's
# nominal typing working AS a benefit, not the restriction. Real structural
# typing has no notion of "is-a" at all — matching shape alone is enough. That's
# the distinction TODO 6 is about.)


# TODO 6 (nominal typing check): define a plain, unrelated @dataclass `NotABook`
# with the exact same fields as Book (title: str, author: str, year: int).
# Create an instance of it, then try passing it to `describe_book`. Run `mypy` and
# read the error — even though the shape matches exactly, it's rejected. This is
# the opposite of TS's structural typing from Lesson 2, where a matching-shape
# variable (not a literal) was accepted freely. Once you've seen the error, comment
# that call back out so the file passes `mypy` again.


# TODO 7: define a `Protocol` named `Shaped` with a single method: `area(self) ->
# float: ...` (the `...` is a literal ellipsis — it's the body, meaning "no
# implementation, this is just a signature"). Then write a plain class `Square`
# (NOT inheriting from Shaped) with an __init__ taking `side: float`, storing it as
# `self.side`, and an `area()` method returning `self.side ** 2`.
# Write a function `print_area(shape: Shaped) -> None` that prints `shape.area()`.
# Call `print_area` with a `Square` instance — this should work with no error,
# proving Square satisfies Shaped structurally despite no inheritance relationship.
