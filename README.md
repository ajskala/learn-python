# learn-python

Structured lessons, same format as `learn-ts-node`. Each lesson has a `README.md`
(concepts) and an `exercise.py` (TODOs you fill in).

## One-time setup (already done)

A virtualenv lives in `.venv` with `mypy` installed.

## Workflow for every lesson

```
cd ~/workspace/learn-python
source .venv/bin/activate      # once per terminal session
mypy                           # type-checks everything under lessons/ (reads mypy.ini)
python lessons/<lesson>/exercise.py   # runs a specific lesson's exercise
```

`mypy` is configured with `strict = True` — the closest Python equivalent to
TypeScript's `strict` compiler option. Python doesn't require type hints at all
(it's dynamically typed by default), but we'll use them from the start since you
already think in TS's type system — `mypy` plays the same role `tsc` did.

Lesson directories are named `lessonNN_topic` (not `NN-topic` like the TS project) —
every lesson has an `__init__.py`, turning `lessons/` into a real Python package so
`mypy` can tell same-named `exercise.py` files in different lessons apart. Package
names must be valid Python identifiers: no hyphens, and no leading digit — hence
`lesson01_...` instead of `01-...`.

Important difference from TS: Python's type hints are **never checked at runtime**
by the interpreter itself, under any circumstance — not even the partial checking
Node's type-stripping gave you. `mypy` is a fully separate, optional static
analysis tool. You can run `python file.py` with completely wrong type hints and it
will still execute — the hints are pure documentation to the interpreter. `mypy` is
what gives them teeth.
