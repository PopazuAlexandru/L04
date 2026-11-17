import os
import sqlite3
import subprocess

import pytest

import exercise4
from exercise4 import *


# bug report 1
def test_r1_admin_password_not_hardcoded():
    assert check_admin("admin123") == False


# bug report 2
def test_r2_find_user_sql_injection():
    import sqlite3
    db = sqlite3.connect(":memory:")
    db.execute("CREATE TABLE users (username TEXT)")
    db.execute("INSERT INTO users VALUES ('alice')")
    assert find_user(db, "' OR '1'='1") is None
