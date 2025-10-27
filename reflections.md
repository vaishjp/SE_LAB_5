1. Easiest vs. Hardest Issues to Fix

Easiest fixes:

Style violations from Flake8 (like missing blank lines, line too long, missing newline at end of file) were very easy to resolve because they only required simple formatting changes.

Adding docstrings and renaming functions to follow snake_case convention were also straightforward.

Hardest fixes:

Replacing the bare except: with specific exception handling required deeper understanding of what errors the code might actually raise.

Removing the use of eval() was trickier because it required redesigning that part of the logic in a safe way while preserving functionality.

Eliminating global variables and rewriting file handling using context managers took a bit more time and testing to ensure nothing broke.

2. False Positives from Static Analysis Tools

One mild false positive came from Bandit flagging a low-severity issue for a simple except block that was already handling a harmless case.

Some Pylint warnings about using global or missing docstrings were not technically harmful to execution, but still valuable to fix for long-term maintainability.

Overall, most of the reports were legitimate and helpful.

3. Integrating Static Analysis into Development Workflow

Local Development:

Run flake8, bandit, and pylint locally before committing code to catch issues early.

Use a pre-commit hook to automatically reject commits with security or style violations.

Continuous Integration (CI):

Add these tools to a GitHub Actions or GitLab CI/CD pipeline to run automatically on every push or pull request.

Configure thresholds (for example, fail CI if Pylint score < 9.0 or Bandit reports any medium/high issues).

Generate and store HTML reports for review in the CI dashboard.

4. Tangible Improvements Observed

Code Quality: The final version is cleaner, follows PEP 8 standards, and uses descriptive names and proper logging.

Readability: Consistent formatting, proper indentation, and docstrings make the code easier to read and maintain.

Security & Robustness: Removing eval() and unsafe except blocks eliminated potential vulnerabilities.

Maintainability: Using with open() and avoiding global variables made the program more modular and less error-prone.

Professionalism: The overall structure now aligns with industry best practices and would integrate smoothly into a CI/CD workflow.