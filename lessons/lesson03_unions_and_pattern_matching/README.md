# Lesson 3 — Unions, `match`/`case`, and Class-Based Discriminated Unions

## Union types — same syntax you've already used

`str | int | bool` — you already saw this shape in Lesson 1 (`str | None`). Nothing
new here conceptually, just using it with more than two members:

```python
def format_value(value: str | int | bool) -> str:
    ...
```

## Narrowing, recap: `isinstance`

You did this in Lesson 1's `safe_length`. It still works fine for unions with more
members:

```python
if isinstance(value, str):
    ...
elif isinstance(value, int):
    ...
```

## `match` / `case` — Python's structural pattern matching (3.10+)

This is the new tool for this lesson, and it's the closest thing Python has to
TS's `switch` on a discriminated union — except more powerful, because it can
match on an object's *type and attributes* directly, not just a single tag field:

```python
def format_value(value: str | int | bool) -> str:
    match value:
        case str():
            return value.upper()
        case bool():
            return "yes" if value else "no"
        case int():
            return f"{value:.2f}"
        case _:
            raise ValueError(f"Unhandled type: {type(value)}")
```

`case str():` matches if `value` is an instance of `str` (same check as
`isinstance(value, str)`), and inside that branch `value` is narrowed to `str` for
`mypy`, same as the `if isinstance(...)` version. `case _:` is the wildcard —
matches anything not caught above, Python's equivalent of a `default:` in a
`switch`.

**Order matters here for a reason you've seen before**: `bool` is technically a
subclass of `int` in Python (a historical wart), so `case int():` would also match
`True`/`False` if it came first. Put the more specific `bool` case before the more
general `int` case — same "correctness bug from case ordering" category you fixed
in the TS lesson, different mechanism.

## Class-based discriminated unions — no "kind" tag needed

In TS, you gave every union member a shared literal `kind` field so `switch` could
tell them apart. In Python, `match` can distinguish union members by their actual
**class**, directly — no artificial tag field required:

```python
from dataclasses import dataclass

@dataclass
class Circle:
    radius: float

@dataclass
class Rectangle:
    width: float
    height: float

Shape = Circle | Rectangle

def area(shape: Shape) -> float:
    match shape:
        case Circle(radius=r):
            return 3.14159 * r ** 2
        case Rectangle(width=w, height=h):
            return w * h
```

`case Circle(radius=r):` does two things at once: checks `isinstance(shape,
Circle)`, **and** if that matches, binds the local name `r` to `shape.radius` —
this works automatically for any `@dataclass` because the decorator generates the
matching metadata (`__match_args__`) needed for pattern matching, no extra setup.
This is a direct consequence of Lesson 2's nominal typing: since every dataclass
has a real, distinct identity, `match` can key off that identity instead of
needing you to invent a shared tag field the way TS's structural types require.

## Exhaustiveness checking: `assert_never`

Python 3.11+ ships `typing.assert_never` — the direct equivalent of TS's
`never`-typed variable trick:

```python
from typing import assert_never

def area(shape: Shape) -> float:
    match shape:
        case Circle(radius=r):
            return 3.14159 * r ** 2
        case Rectangle(width=w, height=h):
            return w * h
        case _:
            assert_never(shape)
```

Same mechanism as TS: if every real case is handled, `shape`'s type at the
wildcard branch is narrowed down to nothing (`Never`), and `assert_never` only
type-checks when its argument is provably `Never`. Add a new shape to `Shape` and
forget a `case` for it, and `mypy` flags the `assert_never(shape)` line — same
signal, same idea, different spelling.

## Exercise

Fill in `exercise.py`. Check with `mypy`, run with
`python lessons/lesson03_unions_and_pattern_matching/exercise.py`.
