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
    transformed_records = []

    for record in records:
        if config.get("multiplier"):
            multiplier = config["multiplier"]
            transformed_records.append(record["value"] * multiplier)

    if transformed_records:
        return transformed_records
    return records


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
    missing_fields = []
    for field in required_fields:
        if field not in row.keys():
            missing_fields.append(field)
    if missing_fields:
        return False, missing_fields
    return True


print(
    validate_schema("id", "timestamp", "value", id=1, timestamp="2024-01-01", value=42)
)
print(validate_schema("id", "timestamp", "value", id=1, value=42))  # missing timestamp


# ============================================================
# 3. build_pipeline_step — HARDEST
# ============================================================
# step_name is the name of this pipeline step.
#
# transforms is any number of transform names as strings (e.g. "clean", "dedupe"), applied inorder.

# Options may include "batch_size" and "retry_on_fail".
#


# Return a dict with: the step name, the list of transforms
# and a summary string noting the batch size (if given) and whether retries are enabled.
def build_pipeline_step(step_name, *transforms, **options):

    if options.get("batch_size"):
        summary = f"batch size {options['batch_size']}"
    else:
        summary = "no batch size specified"

    if not options.get("retry_on_fail"):
        summary += ", retries disabled"
    else:
        summary += ", retries enabled"

    new_dict = {
        "name": step_name,
        "transforms": list(transforms),
        "summary": summary,
    }
    return new_dict


print(
    build_pipeline_step("ingest", "clean", "dedupe", batch_size=500, retry_on_fail=True)
)
print(build_pipeline_step("export"))  # no transforms, no options

"""
Week 1 (closed-notes rebuild #2) — new scenarios, same core patterns
No test calls given — write your own based on what each function needs.
"""


# ============================================================
# 1. normalize_columns
# ============================================================
# column_names are original column strings (e.g. "first_nm", "amt", "dt").
# renames maps old names to new ones as keyword args (e.g. first_nm="first_name").
# Return a list of column names with renames applied where a mapping
# exists, and left unchanged otherwise.
def normalize_columns(*column_names, **renames):
    mapped_list = []

    for name in column_names:
        mapped_list.append(renames.get(name, name))

    return mapped_list


print(normalize_columns("first_nm", "amt", "dt", first_nm="first_name", amt="amount"))
# expect: ["first_name", "amount", "dt"]

print(normalize_columns("id", "value"))
# no renames given — expect: ["id", "value"] unchanged


# ============================================================
# 2. filter_records
# ============================================================
# Each record is a dict (e.g. {"status": "active", "region": "EU"}).
# filters are keyword conditions. A record only passes if it matches
# EVERY filter given (not just one). If no filters are given at all,
# return every record.
def filter_records(*records, **filters):

    filtered_records = []

    for record in records:
        matches = True
        for key, value in filters.items():
            if record.get(key) != value:
                matches = False
        if matches:
            filtered_records.append(record)

    return filtered_records


print(
    filter_records(
        {"status": "active", "region": "EU"}, {"status": "inactive", "region": "US"}
    )
)
# no filters given — expect: both records returned

print(
    filter_records(
        {"status": "active", "region": "EU"},
        {"status": "active", "region": "US"},
        {"status": "inactive", "region": "EU"},
        status="active",
        region="EU",
    )
)
"""
Extra practice — validation pattern (check multiple conditions, decide once)
Same shape every time: reset a flag/list once per item, only update it while
checking that item, decide what to do with it only AFTER all checks are done.
"""

print("\n")


# ============================================================
# 1. all_fields_present — simplest version, no records loop yet
# ============================================================
# row is keyword data (e.g. id=1, name="Sam", email=None).
# Return True if every value in row is NOT None. If any value IS None,
# return False and a list of which field names were null.
def all_fields_present(**row):

    fields_null = []

    for field in row:
        if row.get(field) is None:
            fields_null.append(field)

    if fields_null:
        return False, fields_null
    return True


print(all_fields_present(id=1, name="Sam", email="sam@x.com"))
# expect: True

print(all_fields_present(id=1, name="Sam", email=None))
# expect: False, ["email"]


# ============================================================
# 2. records_in_range — same flag pattern, now looping over records
# ============================================================
# Each record is a dict with a "value" field (e.g. {"id": 1, "value": 50}).
# bounds may include "min_value" and "max_value" as keyword args.
# A record only passes if it satisfies EVERY bound given. If a bound
# wasn't given at all, don't check it (e.g. no max_value means no upper
# limit). Return a list of the records that pass.
def records_in_range(*records, **bounds):
    passed_records = []
    for record in records:
        matches = True
        min_value = bounds.get("min_value")
        max_value = bounds.get("max_value")

        if min_value is not None and min_value > record["value"]:
            matches = False
        if max_value is not None and max_value < record["value"]:
            matches = False
        if matches:
            passed_records.append(record)

    return passed_records


print(
    records_in_range(
        {"id": 1, "value": 50},
        {"id": 2, "value": 150},
        {"id": 3, "value": -10},
        min_value=0,
        max_value=100,
    )
)
# expect: [{"id": 0, "value": 50}]  (2 is too high, 3 is too low)

print(records_in_range({"id": 1, "value": 50}, min_value=0))


# ============================================================
# 3. validate_batch — HARDEST, combines both patterns above
# ============================================================
# rules maps field name -> expected type (e.g. id=int, name=str).

# For each record (a dict), check every field named in rules:

# Does the record have that field, AND is it the right type?
# A record only fully passes if it satisfies every rule.

# Return a list of (record, list_of_problem_fields) ONLY for records that
# failed at least one rule.

# Records that pass everything aren't included at all.

"""
rules -> field name (id=int, name=str)

rules = {"id": int, "name": str}

records = {"id": 1, "name": "Sam"}, {"id": "two", "name": "Alex"}, {"id": 3},

"""
# Does the record have that field, AND is it the right type?


def validate_batch(*records, **rules):
    final_list = []

    for record in records:
        failed_fields = []

        for key, value in rules.items():
            field = record.get(key)

            if field is None or not isinstance(field, value):
                failed_fields.append(key)

        if failed_fields:
            final_list.append((record, failed_fields))

    return final_list


"""

Failed attempt

def validate_batch(*records, **rules):
    bad_records = []
    for record in records:
        list_of_problem_fields = []
        matches = True
        for key, value in rules.items():
            if record.get(key) is None:
                matches = False
                bad_records.append(record)
            if not isinstance(record.get(key), value):
                matches = False
            if matches:
                list_of_problem_fields.append(record)

    return list_of_problem_fields
"""

print(
    validate_batch(
        {"id": 1, "name": "Sam"},
        {"id": "two", "name": "Alex"},
        {"id": 3},
        id=int,
        name=str,
    )
)
# expect something like:
# [
#   ({"id": "two", "name": "Alex"}, ["id"]),       # id is wrong type
#   ({"id": 3}, ["name"])                          # name is missing
# ]


# ============================================================
# 3. count_by_field — HARDEST
# ============================================================
# field is a required argument naming which key to group by (e.g. "status").
# Loop through records
#   count how many times each value of that field appears

# return a dict like {"active": 3, "inactive": 1}.

# If options includes "top_n"
#   only return the top_n most frequent values.


def count_by_field(*records, field, **options):
    pass


# Test 1
print(
    count_by_field(
        {"name": "Alice", "status": "active"},
        {"name": "Bob", "status": "inactive"},
        {"name": "Charlie", "status": "active"},
        field="status",
    )
)
# Expected: {"active": 2, "inactive": 1}


# Test 2
print(
    count_by_field(
        {"status": "active"},
        {"status": "inactive"},
        {"status": "pending"},
        {"status": "active"},
        {"status": "pending"},
        {"status": "active"},
        field="status",
    )
)
# Expected: {"active": 3, "pending": 2, "inactive": 1}


# Test 3
print(
    count_by_field(
        {"name": "Alice", "role": "admin"},
        {"name": "Bob", "role": "user"},
        {"name": "Charlie", "role": "user"},
        {"name": "Dave", "role": "admin"},
        {"name": "Eve", "role": "user"},
        field="role",
    )
)
# Expected: {"user": 3, "admin": 2}


# Test 4 — top_n
print(
    count_by_field(
        {"status": "active"},
        {"status": "inactive"},
        {"status": "active"},
        {"status": "pending"},
        {"status": "active"},
        {"status": "inactive"},
        field="status",
        top_n=1,
    )
)
# Expected: {"active": 3}


# Test 5 — top_n=2
print(
    count_by_field(
        {"status": "active"},
        {"status": "inactive"},
        {"status": "active"},
        {"status": "pending"},
        {"status": "active"},
        {"status": "inactive"},
        {"status": "pending"},
        {"status": "pending"},
        field="status",
        top_n=2,
    )
)
# Expected: {"pending": 3, "active": 3}


# Test 6 — no records
print(count_by_field(field="status"))
# Expected: {}


def count_types(*values):
    type_dict = {
        "int": 0,
        "str": 0,
        "float": 0,
        "bool": 0,
    }

    if not values:
        return type_dict

    for value in values:
        if isinstance(value, bool):
            type_dict["bool"] += 1
        elif isinstance(value, int):
            type_dict["int"] += 1
        elif isinstance(value, str):
            type_dict["str"] += 1
        elif isinstance(value, float):
            type_dict["float"] += 1

    return type_dict


print(count_types(1, 2, "hello", 3.5, "world", True, 4))

"""
{
    int: 3,
    str: 2,
    float: 1,
    bool: 1
}
"""


def group_by_field(*records, field):
    new_dict = {}

    for record in records:
        field_value = record.get(field)

        if field_value not in new_dict:
            new_dict[field_value] = []
        new_dict[field_value].append(record)

    return new_dict


records = [
    {"name": "Alice", "role": "admin"},
    {"name": "Bob", "role": "user"},
    {"name": "Charlie", "role": "admin"},
    {"name": "Dave", "role": "user"},
]

print(group_by_field(*records, field="role"))

"""
{
    "admin": [
        {"name": "Alice", "role": "admin"},
        {"name": "Charlie", "role": "admin"},
    ],
    "user": [
        {"name": "Bob", "role": "user"},
        {"name": "Dave", "role": "user"},
    ],
}
"""
