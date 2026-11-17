# Bug reports for exercise1.py

Line: 3
Problem: is_even returns True for odd numbers because it checks n % 2 == 1, which is incorrect; the docstring says it should return True for even numbers.
Example: is_even(2) returns False, expected True.
Fix: return n % 2 == 0

Line: 8
Problem: rectangle_area returns the sum of width and height instead of the product, which violates the docstring that specifies "area of a rectangle".
Example: rectangle_area(4, 5) returns 9, expected 20.
Fix: return width * height

Line: 12
Problem: double returns n + 2 instead of twice the number (n * 2), which contradicts the docstring "twice the number n".
Example: double(3) returns 5, expected 6.
Fix: return n * 2
