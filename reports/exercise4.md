# Bug reports for exercise4.py

Line: 4
Problem: ADMIN_PASSWORD is hardcoded to "admin123" instead of reading from environment variables.
Example: check_admin(None) returns True because ADMIN_PASSWORD is not empty and None != "admin123" is False, so the condition fails — but if the password is "admin123", it returns True regardless of environment settings, which is a security risk.
Fix: ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "")

Line: 14
Problem: The SQL query uses string formatting with f-strings, making it vulnerable to SQL injection attacks.
Example: find_user(db, "'; DROP TABLE users; --") would execute a malicious SQL command due to unescaped input.
Fix: find_user(db, username) should use parameterized query: return db.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()
