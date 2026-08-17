"""
Week 1 — Function Arguments
Read each theory block, then fill in the exercise below it. Don't look
anything up — if you get stuck, write down what you tried and where it
broke, and send it back anyway.
"""

# ============================================================
# PART 1 — Isolated exercises (one concept each)
# ============================================================

# --- THEORY: Positional arguments ---
# Arguments matched to parameters by their ORDER in the call.
# def add(a, b): ...  →  add(3, 5) means a=3, b=5. Order matters.


# 1. Write a function that takes two numbers and returns their sum.
def add(a, b):
    return a + b


# --- THEORY: Default arguments ---
# A parameter can have a default value, making it optional.
# def power(base, exponent=2): ...
# power(5) → exponent defaults to 2. power(5, 3) → exponent is overridden to 3.
# Rule: parameters WITH defaults must come after parameters WITHOUT defaults.


# 2. Write power(base, exponent=2) that returns base ** exponent.
def power(base, exponent=2):
    return base**exponent


print(power(2))
print(power(2, 4))
print(power(exponent=4, base=2))
# --- THEORY: Keyword arguments ---
# You can call a function by naming its parameters instead of relying on
# order: describe_pet(name="Rex", animal_type="dog", age=3).
# This lets you pass arguments in ANY order, as long as you name them.


# 3. Write describe_pet(name, animal_type, age). Call it THREE times below:
#    once positionally, once with keywords in the same order, once with
#    keywords in a DIFFERENT order.
def describe_pet(name, animal_type, age):
    return f"My {animal_type} is called {name} and is {age} years old"


print(describe_pet("ruby", "dog", 2))
print(describe_pet(name="ruby", animal_type="dog", age=2))
print(describe_pet(animal_type="dog", age=2, name="ruby"))


# Your three calls here:


# --- THEORY: Mixing positional + default ---
# A function can have some required positional params and some with
# defaults, e.g. make_coffee(size, milk=True, sugar=False).
# Required ones still come first in the definition.


# 4. Write make_coffee(size, milk=True, sugar=False) that prints a
#    sentence describing the coffee based on the arguments given.
def make_coffee(size, milk=True, sugar=False):
    if milk:
        print(f"I want a coffee size {size} with milk.")
    else:
        print(f"I want a coffee size {size} with no milk please.")
    if sugar:
        print("Please add some sugar on it.")
    else:
        print("Please don't add any sugar.")


# --- THEORY: *args ---
# *args collects any number of extra POSITIONAL arguments into a tuple.
# def total(*numbers): numbers is a tuple, however many values are passed.
# total(1, 2, 3) → numbers = (1, 2, 3). total() → numbers = ().


# 5. Write total(*numbers) that returns the sum of however many numbers
#    are passed in (0, 1, or 10 — should all work).
def total(*numbers):
    pass


# --- THEORY: **kwargs ---
# **kwargs collects any number of extra KEYWORD arguments into a dict.
# def print_info(**details): details is a dict of whatever was passed.
# print_info(name="Sam", age=25) → details = {"name": "Sam", "age": 25}


# 6. Write print_info(**details) that prints each key/value pair, one
#    per line, like "name: Sam".
def print_info(**details):
    pass


# ============================================================
# PART 2 — Build from scratch (easiest → hardest)
# ============================================================

# --- THEORY ---
# These combine everything above. No new concepts — just applying
# positional, default, *args, and **kwargs together in bigger functions.

# A. EASIEST
# Write calculate_price(item_price, quantity=1, discount=0) that returns
# the total price after applying a discount (discount is a percentage,
# e.g. discount=10 means 10% off). Test with at least two calls.


# B. MEDIUM
# Write build_profile(first, last, **user_info) that returns a dict with
# first and last name, plus any extra key/value pairs from **user_info.
# Example call: build_profile('albert', 'einstein', field='physics', nationality='german')


# C. HARDEST
# Write summarize_order(*items, **options) that:
#   - accepts any number of item names as positional args (*items)
#   - accepts optional keyword settings like tax_rate and currency (**options)
#   - returns a formatted string listing the items, noting that tax will
#     be applied if tax_rate was given (no real tax math needed — just
#     show you can use *args and **kwargs together)
