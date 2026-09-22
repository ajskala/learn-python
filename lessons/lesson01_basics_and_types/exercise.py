# Lesson 1 exercise
# Fill in each TODO. From the project root, with the venv activated:
#   mypy
#   python lessons/lesson01_basics_and_types/exercise.py

# TODO 1: declare a variable `city` typed as str, set to any city name.

# TODO 2: declare a variable `population` typed as int.

# TODO 3: declare a variable `landmarks` typed as list[str] with at least two
# landmark names in `city`.

# TODO 4: write a function `describe_city` that takes (city: str, population: int)
# and returns a str like "Chicago has 2700000 people."
# Give it an explicit -> str return type.

# TODO 5: write a function `summarize` that takes `landmarks: list[str]` and returns
# a single str joining them with ", ". (Hint: ", ".join(landmarks))
# Give it an explicit return type.

# TODO 6: call both functions and print() the results.

# TODO 7 (type narrowing practice, Python's version of `unknown`): write a function
# `safe_length` that takes a parameter typed `object` (Python's closest equivalent to
# TS's `unknown` — accepts anything, gives you nothing until you narrow it) and
# returns an int: the string's length if the input is a str, otherwise 0.
# Hint: use `isinstance(value, str)` to narrow — Python's equivalent of TS's
# `typeof value === "string"` check, except it works on actual classes/instances
# rather than JS primitive tags.
