# Lesson 2 — Classes, Dataclasses & Protocols

## The big contrast with TypeScript: Python classes are nominal, not structural

Lesson 2 of the TS course was largely about structural typing — any object with a
matching shape satisfies an interface, regardless of what it's named. Python's
`class` system, when checked by `mypy`, works the **opposite** way by default:
**nominal typing**. An object only satisfies a class type if it's actually an
instance of that class (or a subclass) — matching attributes alone isn't enough.
This is a real, important difference, not just a syntax change, and you'll prove
it to yourself in the exercise.

(Python's *runtime* has always been duck-typed — `obj.name` works on literally
anything with a `.name` attribute, no matter its class. `mypy`'s static nominal
checking is a separate, stricter layer on top, opt-in the moment you add type
hints — same relationship as `unknown` vs `any` was purely a static-checking
concept in TS.)

## Regular classes

```python
class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def distance_from_origin(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

p = Point(3, 4)
print(p.distance_from_origin())
```

`self` is Python's explicit `this` — every instance method takes it as the first
parameter, by convention named `self` (not a keyword, just overwhelming
convention — never deviate from it). `__init__` is the constructor. There's no
implicit "declare fields up top" like TS class properties — you declare and
assign an attribute in the same line, inside `__init__`, via `self.x = x`.

## Dataclasses — less boilerplate for "just data" classes

Writing `__init__` by hand for a class that's mostly just a bundle of fields is
repetitive. `@dataclass` generates it for you from type-hinted class attributes —
this is the closest Python equivalent to a TS `interface` used to type a plain
data object:

```python
from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    year: int
    isbn: str | None = None   # optional-with-default, like TS's `isbn?: string`

my_book = Book(title="Dune", author="Frank Herbert", year=1965)
print(my_book.title)   # attribute access, same as TS
```

`@dataclass` also auto-generates `__repr__` (nice printing) and `__eq__` (compares
by field values) for you — try `print(my_book)` and you'll see fields, not just
`<Book object at 0x...>`.

`str | None` is Python's optional-type syntax (equivalent to TS's `isbn?: string`,
which is really sugar for `string | undefined`). Python has no direct per-field
`readonly` — the closest equivalent is `@dataclass(frozen=True)`, which locks
**every** field on the whole object against reassignment after construction, not
one field at a time.

## Inheritance

```python
@dataclass
class EBook(Book):
    file_size_mb: float = 0.0
```

`class EBook(Book):` — the parent class goes in parentheses (Python's `extends`).
Note: with plain (non-frozen) dataclasses, any new field you add in a subclass
needs a default value if the parent class has fields without defaults — that's a
dataclass-specific rule about argument ordering, not a general Python rule.

## Protocols — bringing structural typing back, on purpose

If you specifically *want* TS-style "any object with this shape counts," Python's
`typing.Protocol` gives you that, opt-in:

```python
from typing import Protocol

class Shaped(Protocol):
    def area(self) -> float: ...

class Square:                 # note: no "class Square(Shaped)" — no inheritance!
    def __init__(self, side: float) -> None:
        self.side = side

    def area(self) -> float:
        return self.side ** 2

def print_area(shape: Shaped) -> None:
    print(shape.area())

print_area(Square(4))   # mypy accepts this — Square structurally satisfies Shaped
```

`Square` never mentions `Shaped` anywhere. `mypy` accepts it purely because it has
a matching `area(self) -> float` method — this is exactly TS's `implements`
behavior from Lesson 2, except here it's `Protocol` specifically that turns
structural checking back on, rather than it being the default for every class.

## Exercise

Fill in `exercise.py`. Check with `mypy`, run with
`python lessons/lesson02_classes_dataclasses_protocols/exercise.py`.
