---
name: bug-finder
description: Find all bugs in a numbered Python file and output strict Line/Problem/Example/Fix blocks.
---

Inspect EVERY function in the given Python file line by line and compare its implementation against its docstring and security best practices. Do not stop after the first bug; check every single function in the file.

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
2. Wrong operations or wrong arguments (e.g., passing low instead of high, + instead of -).
3. Unusual/edge inputs: empty list [], empty string "", 0, None, negative values.
4. Security issues: eval(), exec(), shell=True, hardcoded passwords/secrets, SQL string formatting, md5/sha1.

EXAMPLE OUTPUT:
Line: 3
Problem: is_adult uses > 18 instead of >= 18, so 18 returns False instead of True.
Example: is_adult(18) returns False, expected True.
Fix: return age >= 18
