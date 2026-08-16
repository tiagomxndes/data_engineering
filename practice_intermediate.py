"""
PYTHON PRACTICE — CALIBRATED SET
Covers everything in the two DataCamp courses (variables/types, data structures,
control flow, built-ins, modules/packages, pandas, functions, lambdas, error
handling) but combined into fewer, denser problems instead of one skill per drill.

Rules:
- No solutions included. Attempt each fully before moving to the next.
- Each exercise deliberately mixes 3+ topics — treat it like a mini feature,
  not a fill-in-the-blank.
- Run this file as you go (uncomment the calls at the bottom).
"""

import os
import string


# ============================================================
# EXERCISE 1 — Inventory report (types, dicts, loops, built-ins, f-strings)
# ============================================================
# You're given `inventory`, a dict of product -> (unit_price, quantity).
# Write `inventory_report(inventory)` that:
#   - skips any product with quantity == 0
#   - computes each product's total value (price * quantity)
#   - returns a dict {product: total_value}, sorted by total_value descending
#     (use sorted() with a key, not a manual sort)
#   - also prints a formatted line per product: "Widget: $450.00 (30 units)"
# No pandas here — pure Python dict/loop work.

inventory = {
    "widget": (15.0, 30),
    "gadget": (42.5, 0),
    "gizmo": (7.25, 100),
    "thingamajig": (99.99, 2),
}


def inventory_report(inventory):
    pass


# ============================================================
# EXERCISE 2 — Password policy validator (functions, args/kwargs, error handling)
# ============================================================
# Write `validate_password(password, min_length=8, require_digit=True,
# require_upper=True)` that:
#   - raises ValueError with a specific message for each failed rule
#     (don't just say "invalid" — say which rule failed)
#   - returns True if all checks pass
# Then write `check_passwords(*passwords, **policy)` that takes any number of
# password strings plus policy overrides as kwargs, calls validate_password on
# each, and returns a dict {password: "OK" or the error message} — catching
# the ValueError instead of letting it crash the loop.


def validate_password(password, min_length=8, require_digit=True, require_upper=True):
    pass


def check_passwords(*passwords, **policy):
    pass


# ============================================================
# EXERCISE 3 — Word frequency counter (string module, sets, lambdas, sorting)
# ============================================================
# Write `word_frequencies(text)` that:
#   - lowercases the text and strips out any character not in
#     string.ascii_lowercase or whitespace (use the string module, not regex)
#   - splits into words, builds a dict of word -> count
#   - returns the top 3 most frequent words as a list of (word, count) tuples,
#     sorted using sorted() + a lambda key
# Also write `unique_words(text)` that returns the set of unique words.

sample_text = "The quick brown fox jumps over the lazy dog. The dog barks!"


def word_frequencies(text):
    pass


def unique_words(text):
    pass


# ============================================================
# EXERCISE 4 — File system scanner (os module, error handling, list comprehension)
# ============================================================
# Write `scan_directory(path)` that:
#   - returns None and prints a clear message if `path` doesn't exist
#     (use os.path.exists, don't just try/except blindly)
#   - otherwise returns a dict with keys "files" and "folders", each a list
#     of names in that directory (use os.listdir + os.path.isfile/isdir)
#   - use a list comprehension for at least one of the two lists


def scan_directory(path):
    pass


# ============================================================
# EXERCISE 5 — Grade book (OOP-adjacent: dict of dicts, functions, control flow)
# ============================================================
# You're given `grades`, a dict of student -> list of scores.
# Write `class_summary(grades)` that returns a dict:
#   { student: {"average": ..., "grade": ..., "passed": True/False} }
# Rules: average = mean of scores (no manual sum loop — use built-ins).
# grade: "A" if avg >= 90, "B" if >= 80, "C" if >= 70, else "F".
# passed: True if avg >= 60.
# Then write `top_student(summary)` that returns the name with the highest
# average, using max() with a lambda key — not a manual loop.

grades = {
    "alice": [92, 88, 95],
    "bob": [61, 58, 70],
    "carol": [75, 82, 79],
    "dan": [40, 55, 50],
}


def class_summary(grades):
    pass


def top_student(summary):
    pass


# ============================================================
# EXERCISE 6 — Sales data with pandas (pandas, functions, lambdas)
# ============================================================
# Given the list of dicts below, build a pandas DataFrame from it.
# Write `sales_summary(records)` that:
#   - builds the DataFrame inside the function
#   - adds a "revenue" column (price * units) using a lambda with .apply(),
#     or a vectorized operation — try both and note which is better and why
#     in a comment
#   - returns the product name with the highest total revenue (group by
#     product, sum revenue, find max) as a string

sales_records = [
    {"product": "widget", "price": 15.0, "units": 30},
    {"product": "gizmo", "price": 7.25, "units": 100},
    {"product": "widget", "price": 15.0, "units": 10},
    {"product": "gadget", "price": 42.5, "units": 5},
]


def sales_summary(records):
    pass


# ============================================================
# EXERCISE 7 — Safe calculator (error handling, docstrings, arbitrary args)
# ============================================================
# Write `safe_calculate(operation, *numbers)` with a proper multi-line
# docstring (params, return, example). `operation` is one of:
# "sum", "average", "divide_chain" (divides numbers[0] by numbers[1] by
# numbers[2]...).
#   - raise ValueError for an unknown operation
#   - catch ZeroDivisionError inside divide_chain and return the string
#     "Division by zero encountered" instead of crashing
#   - raise ValueError if *numbers is empty


def safe_calculate(operation, *numbers):
    """
    TODO: write the docstring, then implement.
    """
    pass


# ============================================================
# EXERCISE 8 — Integration: mini CLI report tool
# ============================================================
# Combine everything above into one function `run_report(inventory, grades,
# text)` that:
#   - calls inventory_report, class_summary, and word_frequencies
#   - prints a clean multi-section report to the terminal, e.g.:
#       === INVENTORY ===
#       ...
#       === GRADES ===
#       ...
#       === TOP WORDS ===
#       ...
#   - wraps the whole thing in a try/except that catches any unexpected
#     exception and prints "Report failed: <reason>" instead of crashing
# This one has no single "right" structure — the goal is composing the
# functions you already wrote, cleanly.


def run_report(inventory, grades, text):
    pass


# ============================================================
# Uncomment to test as you complete each one.
# ============================================================

# print(inventory_report(inventory))
# print(check_passwords("abc12345", "ABCDEFGH", "Valid123", min_length=6))
# print(word_frequencies(sample_text))
# print(unique_words(sample_text))
# print(scan_directory(os.getcwd()))
# print(class_summary(grades))
# print(top_student(class_summary(grades)))
# print(sales_summary(sales_records))
# print(safe_calculate("divide_chain", 100, 5, 0))
# run_report(inventory, grades, sample_text)
