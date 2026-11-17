# Bug reports for exercise2.py

Line: 3
Problem: is_passing uses > 5 instead of >= 5, so grades of exactly 5 return False instead of True.
Example: is_passing(5) returns False, expected True.
Fix: return grade >= 5

Line: 13
Problem: clamp uses max(low, min(x, low)) which simplifies to max(low, low) = low, so it always returns low regardless of x.
Example: clamp(10, 0, 5) returns 0, expected 5.
Fix: return max(low, min(x, high))
