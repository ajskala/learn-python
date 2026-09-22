# Lesson 1 — Python Basics & Type Hints

## Variables

No `let`/`const`/`var` — just assign. No declaration keyword at all:

```python
city = "Chicago"
population = 2700000
is_capital = False
```

Python is dynamically typed: a variable isn't locked to a type. `city = "Chicago"`
then later `city = 5` is legal to the *interpreter* — nothing stops you. This is
different from TS, where `let city = "Chicago"` permanently infers `city: string`.
Static type discipline in Python is opt-in, via type hints + `mypy` (below) — the
runtime itself enforces none of it.

## Type hints

Optional annotations, checked only by a separate tool (`mypy`), never by the
interpreter:

```python
age: int = 34
name: str = "AJ"
is_admin: bool = True
tags: list[str] = ["a", "b"]
pair: tuple[str, int] = ("x", 1)

def add(a: int, b: int) -> int:
    return a + b
```

Familiar shape from TS (`: type` after the name, `->` instead of TS's trailing
`: type` for return values on functions). The core primitive types: `int`, `float`,
`str`, `bool`, `None` (Python's `null`/`undefined` — there's only one).

`Any` (from the `typing` module, or implicit when unannotated under non-strict mode)
is Python's `any` — avoid it for the same reasons. Under `strict = True` in our
`mypy.ini`, every function needs full type hints or mypy will flag it.

## f-strings — string interpolation

```python
name = "AJ"
age = 34
print(f"{name} is {age} years old")
```

Equivalent to TS template literals (`` `${name} is ${age}` ``), just `f"..."`
instead of backticks and `{}` instead of `${}`.

## Core collections

```python
tags: list[str] = ["a", "b", "c"]        # like TS array
point: tuple[int, int] = (3, 4)          # like TS tuple — fixed length/types
person: dict[str, str] = {"name": "AJ"}  # like TS Record<string, string> / object
unique: set[int] = {1, 2, 3}             # no direct TS equivalent (closest: Set<number>)
```

## Functions

```python
def greet(name: str, excited: bool = False) -> str:
    if excited:
        return f"HI {name.upper()}!"
    return f"Hi {name}"
```

`excited: bool = False` is a default parameter value — same idea as TS's
`excited: boolean = false`.

## Control flow

```python
for tag in tags:
    print(tag)

for i in range(5):        # 0,1,2,3,4 — like a C-style for loop's index
    print(i)

i = 0
while i < 3:
    i += 1                 # no ++ operator in Python
```

No braces — indentation *is* the block structure. This trips up everyone coming
from a brace language at first; be deliberate about consistent indentation
(4 spaces is the near-universal convention, enforced by the `PEP 8` style guide).

## Exercise

Fill in `exercise.py` in this folder. Then, from the project root:

```
source .venv/bin/activate
mypy
python lessons/lesson01_basics_and_types/exercise.py
```
