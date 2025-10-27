| **Category**                   | **Issue Detected**                                            | **Tool / Code**                          | **Fix Applied**                                                                            | **Status** |
| ------------------------------ | ------------------------------------------------------------- | ---------------------------------------- | ------------------------------------------------------------------------------------------ | ---------- |
| **Exception Handling**         | Bare `except:` block (no exception type specified)            | Bandit B110 / Flake8 E722 / Pylint W0702 | Replaced with specific exception types (`except KeyError:` / `except FileNotFoundError:`). | ✅ Fixed    |
| **Insecure Function Usage**    | Use of `eval()` detected                                      | Bandit B307 / Pylint W0123               | Removed `eval()`; replaced with normal print statement and safer logic.                    | ✅ Fixed    |
| **Naming Convention**          | Functions not in `snake_case` (`addItem`, `removeItem`, etc.) | Pylint C0103                             | Renamed functions to `add_item`, `remove_item`, `get_qty`, etc.                            | ✅ Fixed    |
| **Missing Docstrings**         | Functions missing descriptions                                | Pylint C0116                             | Added short docstrings for all functions.                                                  | ✅ Fixed    |
| **Missing Module Docstring**   | No module-level documentation                                 | Pylint C0114                             | Added module docstring at the top explaining purpose of the script.                        | ✅ Fixed    |
| **Dangerous Default Argument** | Mutable default argument (`logs=[]`)                          | Pylint W0102                             | Removed mutable default list, replaced with safe initialization.                           | ✅ Fixed    |
| **Resource Handling**          | Files opened without context manager                          | Pylint R1732 / W1514                     | Replaced `open()` with `with open(..., encoding="utf-8")`.                                 | ✅ Fixed    |
| **Unused Import**              | `import logging` unused                                       | Flake8 F401 / Pylint W0611               | Integrated proper logging usage for key operations.                                        | ✅ Fixed    |
| **Style (PEP8)**               | Missing blank lines between functions                         | Flake8 E302 / E305                       | Added consistent blank lines as per PEP 8.                                                 | ✅ Fixed    |
| **Line Length**                | Line exceeded 79 characters                                   | Flake8 E501                              | Broke long lines into multiple lines.                                                      | ✅ Fixed    |
| **Final Newline Missing**      | No newline at end of file                                     | Flake8 W292 / Pylint C0304               | Added newline at EOF.                                                                      | ✅ Fixed    |
| **Global Statement Usage**     | Use of `global` keyword                                       | Pylint W0603                             | Removed global mutation; replaced with return-based or modular handling.                   | ✅ Fixed    |
| **Logging and Output**         | Direct `print()` used for critical operations                 | Code Quality                             | Integrated Python’s `logging` module for consistent output and severity levels.            | ✅ Fixed    |










✅ Final Quality Scores
Tool	Result
Flake8	0 issues
Bandit	0 security warnings
Pylint	9.8–10 / 10