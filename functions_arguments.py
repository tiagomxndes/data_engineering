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
    return sum(numbers)


print(total())
print(total(2, 5, 6, 67, 8))

# --- THEORY: **kwargs ---
# **kwargs collects any number of extra KEYWORD arguments into a dict.
# def print_info(**details): details is a dict of whatever was passed.
# print_info(name="Sam", age=25) → details = {"name": "Sam", "age": 25}


# 6. Write print_info(**details) that prints each key/value pair, one
#    per line, like "name: Sam".
def print_info(**details):

    for key, value in details.items():
        print(f"{key}: {value}")


print_info(city="Cork", job="developer")
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


def calculate_price(item_price, quantity=1, discount=0):
    return (item_price * quantity) - (item_price * quantity * (discount / 100))


print(calculate_price(10, 2, 10))
print(calculate_price(10, 2, 50))
print(calculate_price(quantity=2, item_price=3, discount=0))
# B. MEDIUM
# Write build_profile(first, last, **user_info) that returns a dict with
# first and last name, plus any extra key/value pairs from **user_info.
# Example call: build_profile('albert', 'einstein', field='physics', nationality='german')


def build_profile(first, last, **user_info):
    profile = {"first_name": first, "last_name": last}

    for key, value in user_info.items():
        profile[key] = value

    return profile


print(build_profile("albert", "einstein", field="physics", nationality="german"))


# C. HARDEST
# Write summarize_order(*items, **options) that:
#   - accepts any number of item names as positional args (*items)
#   - accepts optional keyword settings like tax_rate and currency (**options)
#   - returns a formatted string listing the items, noting that tax will
#     be applied if tax_rate was given (no real tax math needed — just
#     show you can use *args and **kwargs together)
#


def summarize_order(*items, **options):
    contains_no_tax = ""
    contains_tax = ""
    for item in items:
        if "tax_rate" in options:
            tax_rate = options["tax_rate"]
            contains_tax += f"{item} contains {tax_rate} tax"
        else:
            contains_no_tax += f"{item} contains no tax"

    if contains_no_tax and contains_tax:
        return contains_no_tax, contains_tax
    elif contains_tax:
        return contains_tax
    else:
        return contains_no_tax


print(summarize_order("coffee", "muffin", tax_rate=8, currency="EUR"))

"""
Write summarize_flight(*passengers, **options):

Accepts any number of passenger names as positional args
Accepts optional keyword settings, including baggage_fee
Builds up a result as it loops over passengers:
    - if baggage_fee was given, note that the fee applies;
    - if not, note that it's baggage-free
Returns only the relevant piece(s) — no empty strings tagging along, same as before
Single return, outside the loop
"""


def summarize_flight(*passengers, **options):
    has_fee = ""
    has_not_fee = ""
    for passenger in passengers:
        if "baggage_fee" in options:
            baggage_fee = options["baggage_fee"]
            has_fee += f"{baggage_fee} applies for {passenger}\n"
        else:
            has_not_fee += f"{passenger} has no fee\n"

    if has_fee and has_not_fee:
        return has_fee, has_not_fee
    elif has_fee:
        return has_fee
    else:
        return has_not_fee


print(summarize_flight("Alice", "Bob", baggage_fee=25, airline="Ryanair"))

"""
Week 1 (extra reps) — Data-engineering-flavored function/args practice
Theory already covered — go straight to writing these.
"""


# ============================================================
# 1. process_records — mini ETL step
# ============================================================
# Simulates a transform step. Each positional arg is a dict representing
# a row (e.g. {"id": 1, "value": 100}). config may include "multiplier"
# and "source". If "multiplier" was given, apply it to each record's
# "value" field; otherwise leave records unchanged. Return a list of the
# transformed records.
def process_records(*records, **config):
    pass


print(
    process_records(
        {"id": 1, "value": 100}, {"id": 2, "value": 200}, multiplier=1.1, source="api"
    )
)
print(process_records({"id": 1, "value": 50}))  # no multiplier given


# ============================================================
# 2. validate_schema — data quality check
# ============================================================
# required_fields are field names that must be present (e.g. "id",
# "timestamp"). row is the actual data, passed as keyword args. Return
# True if every required field is present in row, False otherwise — and
# if any are missing, also return which ones are missing.
def validate_schema(*required_fields, **row):
    pass


print(
    validate_schema("id", "timestamp", "value", id=1, timestamp="2024-01-01", value=42)
)
print(validate_schema("id", "timestamp", "value", id=1, value=42))  # missing timestamp


# ============================================================
# 3. build_pipeline_step — HARDEST
# ============================================================
# step_name is the name of this pipeline step. transforms is any number
# of transform names as strings (e.g. "clean", "dedupe"), applied in
# order. options may include "batch_size" and "retry_on_fail". Return a
# dict with: the step name, the list of transforms, and a summary string
# noting the batch size (if given) and whether retries are enabled.
def build_pipeline_step(step_name, *transforms, **options):
    pass


print(
    build_pipeline_step("ingest", "clean", "dedupe", batch_size=500, retry_on_fail=True)
)
print(build_pipeline_step("export"))  # no transforms, no options
