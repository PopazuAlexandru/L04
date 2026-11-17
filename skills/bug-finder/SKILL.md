---
name: bug-finder
description: Find all bugs in a numbered Python file and output strict Line/Problem/Example/Fix blocks.
---

Inspect EVERY function and global variable in the given Python file line by line against its docstring and security best practices. Report ONLY real bugs; do NOT invent edge-case bugs when the code already handles them properly (for example, `password == ADMIN_PASSWORD` already safely returns `False` for `None`).

CRITICAL FORMATTING RULES:
- Output ONLY plain text blocks with these exact 4 prefixes at the start of each line:
Line: <number>
Problem: <what is wrong and why>
Example: <concrete function call showing actual wrong output vs expected output>
Fix: <corrected single line of code>
- Separate multiple bug blocks with one empty line.
- NEVER use bold (**Line:**), bullets (- Line:), numbering (1.), or markdown code fences (```).
- NEVER write introductory or concluding text.

WHAT BUGS TO LOOK FOR:
1. Boundary errors: > instead of >=, < instead of <=, off-by-one limits.
2. Wrong operations or wrong arguments.
3. Unusual/edge inputs: empty list [], empty string "", 0, negative values.
4. Security vulnerabilities:
   - Hardcoded passwords/secrets (e.g., ADMIN_PASSWORD = "admin123" instead of os.environ.get("ADMIN_PASSWORD", "")).
   - SQL injection via f-strings or string formatting in db.execute() (must use parameterized query with ?).
   - eval(), exec(), shell=True, md5/sha1.

EXAMPLE OUTPUT:
Line: 4
Problem: ADMIN_PASSWORD is hardcoded to "admin123" instead of reading from environment variables.
Example: check_admin("admin123") returns True without ADMIN_PASSWORD set, expected False.
Fix: ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "")
