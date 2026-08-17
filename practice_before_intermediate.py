"""
REFRESHER DRILLS — one concept at a time, feeding into exercises 3-8.
These are deliberately tiny and isolated. Do these first, then go back to
the real exercises — the pieces should click faster once you've drilled
each one on its own.

No solutions included. Attempt each, then move to the next.
"""

import os
import string


# ============================================================
# DRILL A — string module (feeds Exercise 3: word_frequencies)
# ============================================================
# 1. Print string.ascii_lowercase. What does it actually contain?
# 2. Write a one-liner: given a single character `c`, how do you check
#    if `c` is in string.ascii_lowercase (i.e. is it a lowercase letter)?
# 3. Given `raw = "Hi! there... 123"`, build a new string containing ONLY
#    the characters that are in string.ascii_lowercase or are a space,
#    by looping through raw.lower() character by character.
#    (This is the exact filtering step word_frequencies needs.)

raw = "Hi! there... 123"
print(string.ascii_lowercase)  # 1
one_liner = "c"  # 2

if one_liner in string.ascii_lowercase:
    print(True)

new_string = ""
for char in raw.lower():
    if char in string.ascii_lowercase or char == " ":
        new_string += char

print(new_string)

# ============================================================
# DRILL B — sets (feeds Exercise 3: unique_words)
# ============================================================
# 1. Given `words = ["cat", "dog", "cat", "bird", "dog"]`, turn it into a
#    set. What happened to the duplicates?
# 2. Given two sets `a = {"cat", "dog"}` and `b = {"dog", "bird"}`, what's
#    the difference between `a | b`, `a & b`, and `a - b`? Print all three.

# 1. The duplicates will be removed as sets don't accept duplicated values.
words = ["cat", "dog", "cat", "bird", "dog"]
a = {"cat", "dog"}
b = {"dog", "bird"}
print(a | b)  # Returns the set elements that are in A and in B
print(a & b)  # Returns the element that is in A and B
print(a - b)  # This one i have no clue
# print(set(words))

# ============================================================
# DRILL C — sorted() + lambda, but for "top N" (feeds Exercise 3 and 5)
# ============================================================
# Given `counts = {"the": 5, "dog": 2, "fox": 1, "over": 1}`
# 1. Sort it by value descending (you already did this in Exercise 1 —
#    reuse the same pattern).
# 2. Now take only the top 2 entries from that sorted result. What Python
#    syntax lets you grab "the first N items" of a list? (Think about
#    what you use to grab "the first 3 elements" of a list — same idea.)

counts = {"the": 5, "dog": 2, "fox": 1, "over": 1}
print(sorted(counts.items(), key=lambda pair: pair[0:2], reverse=True))

# ============================================================
# DRILL D — os module basics (feeds Exercise 4: scan_directory)
# ============================================================
# 1. Print os.getcwd() — what does it return?
# 2. Use os.path.exists(...) to check if a path you know exists (like
#    os.getcwd()) returns True, and a made-up path like "not_a_real_folder"
#    returns False.
# 3. Use os.listdir(os.getcwd()) — what type of object does it return, and
#    what's inside it (just names, or full paths)?
# 4. For one item from that listdir() result, use os.path.isfile(...) and
#    os.path.isdir(...) to check what it is. Note: these need the FULL
#    path, not just the name — how would you build the full path from a
#    directory + a name? (There's an os.path function for joining paths —
#    look up os.path.join)


# ============================================================
# DRILL E — list comprehension (feeds Exercise 4)
# ============================================================
# 1. Given `nums = [1, 2, 3, 4, 5, 6]`, write a list comprehension that
#    returns only the even numbers.
# 2. Rewrite DRILL A #3 (the character filter) as a list comprehension
#    instead of a manual loop, then join it back into a string with
#    "".join(...)

nums = [1, 2, 3, 4, 5, 6]
even_nums = [num for num in nums if num % 2 == 0]

new_string = ""
for char in raw.lower():
    if char in string.ascii_lowercase or char == " ":
        new_string += char


rw = [char for char in raw.lower() if char in string.ascii_lowercase or char == " "]
print(new_string)

# ============================================================
# DRILL F — mean / built-ins without manual loops (feeds Exercise 5)
# ============================================================
# Given `scores = [92, 88, 95]`
# 1. Compute the average using only sum() and len() — no loop, no import.
# 2. Now do the same thing using the `statistics` module's `mean()`
#    function instead. Which do you prefer and why?

scores = [92, 88, 95]


# ============================================================
# DRILL G — max() with a lambda key (feeds Exercise 5: top_student)
# ============================================================
# Given `people = {"alice": 92, "bob": 61, "carol": 79}`
# Use max() with a key=lambda to find the NAME with the highest value.
# (Hint: max() over a dict by default iterates its keys — you need to
# tell it to compare by looking up each key's value.)

people = {"alice": 92, "bob": 61, "carol": 79}


# ============================================================
# DRILL H — pandas basics (feeds Exercise 6: sales_summary)
# ============================================================
# import pandas as pd
# 1. Build a DataFrame from this list of dicts:
records = [{"product": "a", "price": 10}, {"product": "b", "price": 20}]
# 2. Add a new column "double_price" two ways:
#    a) df["double_price"] = df["price"].apply(lambda x: x * 2)
#    b) df["double_price"] = df["price"] * 2   (vectorized, no lambda)
#    Confirm both give the same result. Which one runs faster on large
#    data, and why might that be? (Think about what .apply() has to do
#    under the hood — call a Python function once per row — versus what
#    the vectorized version does.)
# 3. Use df.groupby("product")["price"].sum() — what does this return,
#    and what type is it?
# 4. From that groupby result, how would you find the product with the
#    MAX total price? (Hint: the result is like a dict/Series — think
#    about .idxmax(), or converting to a plain dict and reusing your
#    max()+lambda trick from Drill G.)


# ============================================================
# DRILL I — *args (feeds Exercise 7: safe_calculate)
# ============================================================
# 1. Write a function `add_all(*numbers)` that returns the sum of however
#    many numbers are passed in (0, 1, or 10 — any amount).
# 2. Inside that function, what TYPE is `numbers`? Print type(numbers) to
#    confirm — this matters for how you'd loop over it or index into it.


def add_all(*numbers):
    pass


# ============================================================
# DRILL J — catching a SPECIFIC exception type (feeds Exercise 7)
# ============================================================
# 1. Write a function `divide(a, b)` with NO error handling that just
#    does `return a / b`. Call divide(10, 0) and read the exact exception
#    type Python raises (not just "an error" — the specific class name).
# 2. Now wrap that same division in a try/except that catches ONLY that
#    specific exception type (not a bare `except:`), and returns a
#    friendly message instead of crashing.
# 3. Why is catching the SPECIFIC exception type (e.g. ZeroDivisionError)
#    better practice than a bare `except:`? (Think about what a bare
#    except would silently swallow that you might NOT want to hide —
#    like a typo causing a NameError.)


def divide(a, b):
    pass


# ============================================================
# DRILL K — docstrings, for real this time (feeds Exercise 7)
# ============================================================
# Write a multi-line docstring for this function (don't implement the
# function itself, just the docstring) describing:
#   - what it does in one sentence
#   - Args: each parameter and its type
#   - Returns: what it gives back and its type
#   - Example: one line showing a sample call and output
def convert_temperature(value, from_unit, to_unit):
    pass


# ============================================================
# Uncomment as you go.
# ============================================================

# print(string.ascii_lowercase)
# print(add_all(1, 2, 3))
# print(divide(10, 0))
