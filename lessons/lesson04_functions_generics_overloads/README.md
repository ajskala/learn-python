# Lesson 4 — Functions In Depth: Defaults, `*args`, Generics, Overloads

## Default parameters (recap) and keyword-only parameters

You've used default parameters since Lesson 1 (`isbn: str | None = None`). Python
adds something TS doesn't have: **keyword-only parameters**, marked by a bare `*`
in the signature:

```python
def describe_item(name: str, quantity: int = 1, *, note: str | None = None) -> str:
    base = f"{quantity}x {name}"
    return f"{base} ({note})" if note else base

describe_item("widget")
describe_item("widget", 5)
describe_item("widget", 5, note="backordered")   # note MUST be passed by name
describe_item("widget", 5, "backordered")          # ERROR — note is keyword-only
```

Everything after the bare `*` can only be passed as `name=value`, never
positionally. There's no TS equivalent — the closest you could get in TS is
accepting an options object (`{ note?: string }`) instead of a plain parameter.
Keyword-only params are common in Python for parameters where positional use
would be error-prone or unclear at the call site.

## `*args` — Python's rest parameter

```python
def total(*nums: int) -> int:
    return sum(nums)

total(1, 2, 3)   # nums = (1, 2, 3), a tuple
total()           # nums = ()
```

Same idea as TS's `...nums: number[]`, one difference: `*args` collects into a
`tuple`, not a `list`.

(There's also `**kwargs` for collecting arbitrary *keyword* arguments into a
`dict` — no direct TS equivalent, since TS has no concept of unlimited named
parameters. Not used in this lesson, but you'll see it constantly in real Python
code, especially in framework/library APIs.)

## Generic functions (PEP 695 syntax, Python 3.12+)

```python
def first_element[T](items: list[T]) -> T | None:
    return items[0] if items else None

first_element([1, 2, 3])     # T inferred as int
first_element(["a", "b"])     # T inferred as str
```

`[T]` right after the function name declares the type parameter — Python's
answer to TS's `<T>`. Same deal: `mypy` infers `T` from the argument, you almost
never spell it out explicitly.

## Generic constraints

```python
from collections.abc import Sized

def get_length[T: Sized](item: T) -> int:
    return len(item)

get_length("hello")
get_length([1, 2, 3])
```

`[T: Sized]` constrains `T` to types that satisfy `Sized` — same job as TS's
`<T extends { length: number }>`. `Sized` comes from `collections.abc` and,
despite being usable as a base class, is defined for static-checking purposes as
structural (like `Protocol` from Lesson 2) — anything with a `__len__` method
(strings, lists, dicts, sets...) satisfies it, no inheritance required. This is
the same structural-checking idea from `Protocol`, just pre-built into the
standard library for the extremely common "has a length" shape.

## Generic classes (PEP 695 syntax)

```python
class Box[T]:
    def __init__(self, contents: T) -> None:
        self.contents = contents

    def get_contents(self) -> T:
        return self.contents

string_box = Box("hello")   # Box[str], inferred from the constructor arg
number_box = Box(42)         # Box[int]
```

Direct parallel to TS's `class Box<T>`.

## Overloads — `@typing.overload`

```python
from typing import overload

@overload
def combine(a: str, b: str) -> str: ...
@overload
def combine(a: int, b: int) -> int: ...
def combine(a: str | int, b: str | int) -> str | int:
    if isinstance(a, str) and isinstance(b, str):
        return a + b
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    raise TypeError("Arguments must both be str or both be int")

combine("a", "b")   # OK, str
combine(1, 2)        # OK, int
combine("a", 1)       # mypy ERROR — no overload matches
```

Same shape as TS's overloads, same reason to reach for it: a single `a: str |
int, b: str | int` signature with no overloads would let `combine("a", 1)` type-
check even though it's nonsense for this function. The `@overload`-decorated
signatures are `...`-bodied (same ellipsis trick as `Protocol` methods in Lesson
2 — "signature only, no implementation") and are what callers actually see; the
final undecorated `def combine(...)` is the real implementation, matching the
same "narrow public surface, looser internals" idea as TS overloads.

## Exercise

Fill in `exercise.py`. Check with `mypy`, run with
`python lessons/lesson04_functions_generics_overloads/exercise.py`.
