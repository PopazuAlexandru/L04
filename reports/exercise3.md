# Bug reports for exercise3.py

Line: 3
Problem: average function divides by len(numbers), which will cause a ZeroDivisionError if the list is empty. The docstring says an empty list has average 0, but the function does not handle that case.
Example: average([]) raises ZeroDivisionError, expected 0.
Fix: return sum(numbers) / len(numbers) if numbers else 0

Line: 8
Problem: first_word uses split()[0] which will raise IndexError if the text is empty or has no words, but the docstring says it returns "" if the text is empty.
Example: first_word("") returns IndexError, expected "".
Fix: return text.split()[0] if text.split() else ""

Line: 12
Problem: percent function divides by total, which will cause ZeroDivisionError if total is 0. The docstring says the result is 0 if total is 0, but the function does not handle that case.
Example: percent(5, 0) raises ZeroDivisionError, expected 0.
Fix: return part / total * 100 if total else 0
