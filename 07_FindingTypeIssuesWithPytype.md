# Pytype

Pytype checks and infers types for your Python code - without requiring type
annotations.

* Lint plain Python code, flagging common mistakes such as mispelled attribute
names, incorrect function calls, and [much more][error-classes], even across
file boundaries.
* Enforce user-provided [type annotations][pep-484]. While annotations are
optional for pytype, it will check and apply them where present.
* Generate type annotations in standalone files ("[pyi files][pyi-stub-files]"),
which can be merged back into the Python source with a provided
[merge-pyi][merge-pyi] tool.

Pytype is a static analyzer, meaning it does not execute the code it runs on.

## Quickstart

To quickly get started with type-checking a file or directory, run the
following, replacing `file_or_directory` with your input:

```
pip install pytype
pytype file_or_directory
```

To set up pytype on an entire package, add the following to a `setup.cfg` file
in the directory immediately above the package, replacing `package_name` with
the package name:

```
[pytype]
inputs = package_name
```


Now you can run the no-argument command `pytype` to type-check the package. It's
also easy to add pytype to your automated testing; see this
[example][importlab-travis] of a GitHub project that runs pytype on Travis.

Finally, pytype generates files of inferred type information, located by default
in `.pytype/pyi`. You can use this information to type-annotate the
corresponding source file, replacing `module.py` with the file's import path:

```
merge-pyi -i module.py .pytype/pyi/module.pyi
```

## Usage

```
usage: pytype [options] input [input ...]

positional arguments:
  input                 file or directory to process
```

Common options:

* `-V, --python-version`: Python version (major.minor) of the target code.
  Defaults to `3.6`.
* `-o, --output`: The directory into which all pytype output goes, including
  generated .pyi files. Defaults to `.pytype`.
* `-d, --disable`. Comma separated list of error names to ignore. Detailed
  explanations of pytype's error names are in [this doc][error-classes].
  Defaults to empty.

For a full list of options, run `pytype --help`.

In addition to the above, you can direct pytype to use a custom typeshed
installation instead of its own bundled copy by setting `$TYPESHED_HOME`.

### Config File

For convenience, you can save your pytype configuration in a file. The config
file is an INI-style file with a `[pytype]` section; if an explicit config file
is not supplied, pytype will look for a `[pytype]` section in the first
`setup.cfg` file found by walking upwards from the current working directory.

Start off by generating a sample config file:

```
$ pytype --generate-config pytype.cfg
```

## Example #1: Type inference and checking

```python
import re

def GetUsername(email_address):
  match = re.match(r'([^@]+)@example\.com', email_address)
  return match.group(1)
```

Let’s see what happens when we use pytype to check it:
```python
% pytype get_username.py
Analyzing 1 sources with 0 dependencies
File "/.../get_username.py", line 5, in GetUsername: No attribute 'group' on None [attribute-error]
  In Optional[Match[str]]
```

Let’s fix the bug, by having the function return None for an invalid email address:

```python
import re
def GetUsername(email_address):
  match = re.match(r'([^@]+)@example\.com', email_address)
  if match is None:
    return None
  return match.group(1)  # <-- Here, match can't be None
```

## Example #2: Validation of type annotations

In Python 3, you can type-annotate (PEP 484) your code to help type-checking tools 
and other developers understand your intention. Pytype is able to alert when your 
type annotations have mistakes:

```python
import re
from typing import Match

def GetEmailMatch(email) -> Match:
  return re.match(r'([^@]+)@example\.com', email)
```

Let’s use `pytype` to check this code snippet:

```python
% pytype example.py
Analyzing 1 sources with 0 dependencies
File "/.../example.py", line 5, in GetEmailMatch: bad option in return type [bad-return-type]
  Expected: Match
  Actually returned: None
```

To fix this, we can use the `Optional` type annotation from the typing module:

```python
import re
from typing import Match, Optional

def GetEmailMatch(email) -> Optional[Match]:
  return re.match(r'([^@]+)@example\.com', email)
```

`Optional` means that the return value can be a `Match` object or `None`.
