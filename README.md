# learn-python

Structured, self-checking lessons for learning Python, written from the
perspective of someone who already knows TypeScript — each lesson draws direct
comparisons to TS concepts. Each lesson has a `README.md` (concepts) and an
`exercise.py` (TODOs you fill in yourself). Your work is checked two ways: `mypy`
for type-correctness, and actually running the file to see real output.

## Prerequisites

- **Python 3.11 or later** (built and verified on 3.14.7). Lesson 3 uses
  `typing.assert_never`, added in 3.11; `match`/`case` (also Lesson 3) needs 3.10+.
  Check your version with `python3 --version`. If you need to install or upgrade,
  get it from [python.org](https://www.python.org/downloads/), via
  [pyenv](https://github.com/pyenv/pyenv), or `brew install python` on macOS.

## Setup

```
git clone https://github.com/ajskala/learn-python.git
cd learn-python

python3 -m venv .venv           # create a virtual environment
source .venv/bin/activate        # macOS/Linux — on Windows: .venv\Scripts\activate

pip install --upgrade pip
pip install -r requirements.txt  # installs mypy, pinned to the version this was built with

mypy                              # should report "no issues found" — confirms setup works
```

## Workflow for every lesson

```
source .venv/bin/activate                     # once per new terminal session
mypy                                            # type-checks everything under lessons/
python lessons/<lesson-folder>/exercise.py      # runs one lesson's exercise
```

Read a lesson's `README.md` first, then fill in the `TODO`s in its `exercise.py`.
Iterate with `mypy` until it's clean, then run the file to see the actual output.

`mypy` is configured with `strict = True` in `mypy.ini` — the closest Python
equivalent to TypeScript's `strict` compiler option. Python doesn't require type
hints at all by default (it's dynamically typed); these lessons use them from the
start since they're written for someone coming from TS, and `mypy` plays the same
role `tsc` does there.

**Important difference from TS**: Python's type hints are *never* checked at
runtime by the interpreter itself, under any circumstance — not even the partial
checking Node's type-stripping gives TS. `mypy` is a fully separate, optional
static analysis tool. `python file.py` will happily run with completely wrong type
hints; the hints are pure documentation to the interpreter. `mypy` is what gives
them teeth.

## A note on the lesson directory names

Lesson directories are named `lessonNN_topic` (e.g. `lesson01_basics_and_types`),
each with an `__init__.py`, turning `lessons/` into a real Python package. This is
required for `mypy` to tell same-named `exercise.py` files in different lessons
apart — without it, `mypy` throws a "duplicate module" error. Python package names
must be valid identifiers (no hyphens, no leading digit), which is why it's
`lesson01_...` rather than `01-...`.

## Lessons

1. **`lesson01_basics_and_types`** — variables, type hints, f-strings,
   collections, functions, control flow, and narrowing with `isinstance`.
2. **`lesson02_classes_dataclasses_protocols`** — classes, `@dataclass`,
   inheritance, and the big contrast with TS: Python classes are **nominal**
   typed by default, with `typing.Protocol` as the opt-in way to get
   TS-style structural typing back.
3. **`lesson03_unions_and_pattern_matching`** — union types, `match`/`case`
   structural pattern matching, class-based discriminated unions (no "kind" tag
   needed), and exhaustiveness checking with `typing.assert_never`.
