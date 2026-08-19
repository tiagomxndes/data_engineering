"""
Week 3 — Sets, Tuples, .add(), .update()

Read each theory block, then fill in the exercise below it.
Don't look anything up — if you get stuck, write down what you
tried and where it broke, and send it back anyway.

Main goals this week:

    - Understand sets
    - Understand tuples
    - Know when to use a list vs set vs tuple
    - Practice .add()
    - Practice .update()
    - Practice converting between collections
    - Use sets to remove duplicates
    - Use tuples to return multiple values from a function
"""


# ============================================================
# PART 1 — THEORY + ISOLATED EXERCISES
# ============================================================


# ------------------------------------------------------------
# THEORY: Sets
# ------------------------------------------------------------
# A set is a collection of UNIQUE values.
#
# Unlike a list:
#
#     numbers = [1, 2, 2, 3, 3, 3]
#
# the set:
#
#     numbers = {1, 2, 2, 3, 3, 3}
#
# automatically becomes:
#
#     {1, 2, 3}
#
# Sets are useful when:
#
#     1. You care about uniqueness.
#     2. You want to quickly check whether something exists.
#     3. You want to compare collections.
#
# A set does NOT work like a list.
#
# You should not think:
#
#     "set = list but better"
#
# Think:
#
#     "list = ordered collection of items"
#     "set  = collection of unique items"
#
# An empty set must be created with:
#
#     set()
#
# NOT:
#
#     {}
#
# because {} creates an empty dictionary.


# 1. Create a set containing the numbers 1, 2, 3, and 4.
#    Print the set.


def create_number_set():
    number_set = {1, 2, 3, 4}
    print(number_set)


create_number_set()
print(40 * "-")
# ------------------------------------------------------------
# THEORY: .add()
# ------------------------------------------------------------
# .add() adds ONE item to a set.
#
# Example:
#
#     numbers = {1, 2, 3}
#     numbers.add(4)
#
#     print(numbers)
#
#     {1, 2, 3, 4}
#
# If you add something that already exists, nothing new happens:
#
#     numbers.add(3)
#
# The set is still:
#
#     {1, 2, 3, 4}
#
# This is one of the important differences between sets and lists:
#
#     list.append(x) -> adds one item, duplicates allowed
#     set.add(x)     -> adds one item, duplicates automatically ignored


# 2. Add the number 5 to this set.
numbers = {1, 2, 3, 4}

# YOUR CODE HERE
numbers.add(5)

print(numbers)
print(40 * "-")

# 3. Try adding the number 3 to the set above.
#    Print the result.

#    The goal is to observe what happens when you add a duplicate.


# YOUR CODE HERE
numbers.add(3)

print(numbers)

print(40 * "-")
# ------------------------------------------------------------
# THEORY: .update()
# ------------------------------------------------------------
# .update() adds MULTIPLE items to a set.
#
# Example:
#
#     numbers = {1, 2, 3}
#     numbers.update([4, 5, 6])
#
#     print(numbers)
#
#     {1, 2, 3, 4, 5, 6}
#
# The easiest way to remember it:
#
#     .add()    -> one item
#     .update() -> multiple items
#
# update() accepts another iterable, such as:
#
#     a list
#     a tuple
#     another set
#
# For example:
#
#     numbers.update([4, 5, 6])
#
# or:
#
#     numbers.update((4, 5, 6))
#
# or:
#
#     numbers.update({4, 5, 6})


# 4. Add 4, 5, and 6 to this set using .update().
numbers = {1, 2, 3}

# YOUR CODE HERE
numbers.update([4, 5, 6])

print(numbers)
print(40 * "-")

# 5. Add the following values using .update():
#
#       "python", "linux", "git"
#
# Start with an empty set.


# YOUR CODE HERE
empty_set = set()
empty_set.update(["python", "linux", "git"])
print(empty_set)

print(40 * "-")
# ------------------------------------------------------------
# THEORY: Lists vs Sets
# ------------------------------------------------------------
# Lists and sets both store multiple values, but they solve
# different problems.
#
# LIST:
#
#     numbers = [3, 1, 3, 2]
#
#     - keeps duplicates
#     - maintains order
#     - supports indexing
#
#     numbers[0]      -> 3
#
#
# SET:
#
#     numbers = {3, 1, 3, 2}
#
#     - removes duplicates
#     - does not provide normal list-style indexing
#     - useful for uniqueness and membership checks
#
#
# If you care about:
#
#     "What position is this item in?"
#
# use a list.
#
# If you care about:
#
#     "Have I already seen this item?"
#
# a set is often a better choice.


# 6. Given this list:
#
languages = ["Python", "Python", "Go", "Rust", "Go", "Python"]
#
# Convert it into a set and print the result.
set_languages = set(languages)
print(set_languages)

# YOUR CODE HERE

print(40 * "-")
# ------------------------------------------------------------
# THEORY: Tuples
# ------------------------------------------------------------
# A tuple is another collection type.
#
# Example:
#
#     person = ("Tiago", 28)
#
# Tuples are similar to lists because they:
#
#     - are ordered
#     - allow duplicates
#     - support indexing
#
# But tuples are IMMUTABLE.
#
# That means once created, you cannot modify their contents.
#
# List:
#
#     numbers = [1, 2, 3]
#     numbers[0] = 99       # allowed
#
# Tuple:
#
#     numbers = (1, 2, 3)
#     numbers[0] = 99       # NOT allowed
#
#
# A useful mental model:
#
#     list  -> collection I expect to modify
#     tuple -> collection I don't expect to modify
#
# Tuples are also very useful for returning multiple values
# from a function.


# 7. Create a tuple containing:
#
#       "Python"
#       "Linux"
#       "Git"
#
# Print the tuple.

languages_tuple = ("Python", "Linux", "Git")
print(languages_tuple)
print(type(languages_tuple))

print(40 * "-")
# YOUR CODE HERE


# 8. Access and print the second item from this tuple:
tools = ("Neovim", "Git", "Linux", "Python")

# YOUR CODE HERE
print(tools[1])
print(40 * "-")

# ------------------------------------------------------------
# THEORY: Tuple unpacking
# ------------------------------------------------------------
# Python lets you unpack a tuple into multiple variables.
#
# Example:
#
#     person = ("Tiago", 28)
#
#     name, age = person
#
# Now:
#
#     name -> "Tiago"
#     age  -> 28
#
# This is extremely common when working with functions that
# return multiple values.
#
# You can also do:
#
#     result = (10, 20)
#     x, y = result
#
# The number of variables must match the number of values.


# 9. Unpack this tuple into three variables and print each variable.
coordinates = (10, 20, 30)

# YOUR CODE HERE
x, y, z = coordinates

print(x, y, z)

print(40 * "-")

# ------------------------------------------------------------
# THEORY: Returning multiple values
# ------------------------------------------------------------
# Python functions can return multiple values.
#
# For example:
#
#     def get_user():
#         return "Tiago", 28
#
# This is actually returning a tuple:
#
#     ("Tiago", 28)
#
# You can then unpack it:
#
#     name, age = get_user()
#
# This is useful when a function needs to give you more than
# one related result.


# 10. Complete this function so that it returns the name
#     and age as a tuple.
#
#     Expected result:
#
#         ("Alice", 25)
#
#
def get_person():
    name = "Alice"
    age = 25

    # YOUR CODE HERE
    return name, age


print(get_person())
print(40 * "-")


# ============================================================
# PART 2 — EASY COMBINED EXERCISES
# ============================================================

# These start combining the concepts.
#
# Don't worry about making them complicated.
# The goal is to make the basic operations feel automatic.


# ------------------------------------------------------------
# A. Remove duplicates
# ------------------------------------------------------------
# Write a function remove_duplicates(items) that takes a list
# and returns a SET containing only unique values.
#
# Example:
#
#     remove_duplicates([1, 2, 2, 3, 3, 3])
#
# should return:
#
#     {1, 2, 3}


def remove_duplicates(items):
    return set(items)


print(remove_duplicates([1, 2, 2, 3, 3, 3]))
print(remove_duplicates(["python", "python", "linux", "git", "linux"]))
print(40 * "-")

# ------------------------------------------------------------
# B. Add several items to a set
# ------------------------------------------------------------
# Write a function add_tools(tools) that:
#
#     1. Starts with an empty set.
#     2. Adds "Python" using .add().
#     3. Adds "Linux" using .add().
#     4. Uses .update() to add:
#
#            "Git", "Neovim", "Bash"
#
#     5. Returns the final set.
#
# The important part here is deliberately using BOTH
# .add() and .update().


def add_tools(tools):

    new_set = set()
    new_set.add("Python")
    new_set.add("Linux")
    new_set.update(["Git", "Neovim", "Bash"])

    return new_set


print(add_tools([]))
print(40 * "-")

# ------------------------------------------------------------
# C. Return two values
# ------------------------------------------------------------
# Write a function get_min_max(numbers) that returns:
#
#     (smallest_number, largest_number)
#
# as a tuple.
#
# Example:
#
#     get_min_max([5, 2, 9, 1, 7])
#
# should return:
#
#     (1, 9)
#
# Hint:
#
#     You already know Python has min() and max().


def get_min_max(numbers):
    return min(numbers), max(numbers)


print(get_min_max([5, 2, 9, 1, 7]))
print(40 * "-")

# ============================================================
# PART 3 — BUILD FROM SCRATCH
# ============================================================

# Now stop being given the exact steps.
#
# Read the problem, decide what data structure makes sense,
# and build the function yourself.
#
# If you get stuck, DON'T immediately look it up.
# Think about:
#
#     1. What data do I need to store?
#     2. Do I need ordering?
#     3. Do I need uniqueness?
#     4. Am I modifying the collection?
#     5. Does my function need to return multiple things?


# ------------------------------------------------------------
# A. EASIEST — Unique tags
# ------------------------------------------------------------
# Write a function unique_tags(tags) that receives a list of
# tags and returns a SET containing only the unique tags.
#
# Example:
#
#     unique_tags([
#         "python",
#         "backend",
#         "python",
#         "linux",
#         "backend"
#     ])
#
# should produce:
#
#     {"python", "backend", "linux"}
#
# Do not manually check whether each tag already exists.
# Use the property of sets that makes duplicates disappear.


def unique_tags(tags):
    return set(tags)


print(
    unique_tags(
        [
            "python",
            "backend",
            "python",
            "linux",
            "backend",
        ]
    )
)

print(40 * "-")
# ------------------------------------------------------------
# B. EASY/MEDIUM — Track seen users
# ------------------------------------------------------------
# Write a function find_unique_users(users) that processes a
# list of usernames and returns a SET containing every unique
# username.
#
# Example:
#
#     users = [
#         "alice",
#         "bob",
#         "alice",
#         "charlie",
#         "bob",
#     ]
#
# Result:
#
#     {"alice", "bob", "charlie"}
#
# This time, try to solve it by:
#
#     1. Creating an empty set.
#     2. Looping through the users.
#     3. Adding each user with .add().
#
# Do NOT simply convert the list directly with set(users).
#
# The purpose is to practice .add().


def find_unique_users(users):
    new_set = set()
    for user in users:
        new_set.add(user)

    return new_set


print(
    find_unique_users(
        [
            "alice",
            "bob",
            "alice",
            "charlie",
            "bob",
        ]
    )
)

print(40 * "-")
# ------------------------------------------------------------
# C. MEDIUM — Combine groups
# ------------------------------------------------------------
# Write a function combine_tools(primary_tools, extra_tools).
#
# It should:
#
#     1. Start with a SET containing primary_tools.
#     2. Add every item from extra_tools using .update().
#     3. Return the final set.
#
# Example:
#
#     primary_tools = ["python", "git"]
#     extra_tools = ["linux", "python", "neovim"]
#
# Result should contain:
#
#     {"python", "git", "linux", "neovim"}
#
# Notice that "python" appears in both collections but should
# only exist once in the final set.


def combine_tools(primary_tools, extra_tools):
    set_primary = set(primary_tools)

    for tool in extra_tools:
        set_primary.add(tool)

    return set_primary


print(
    combine_tools(
        ["python", "git"],
        ["linux", "python", "neovim"],
    )
)

print(40 * "-")
# ------------------------------------------------------------
# D. MEDIUM — Analyse a list
# ------------------------------------------------------------
# Write a function analyse_numbers(numbers) that returns a tuple
# containing THREE things:
#
#     1. The smallest number
#     2. The largest number
#     3. The number of UNIQUE numbers
#
# Example:
#
#     analyse_numbers([4, 2, 7, 2, 4, 9])
#
# should return:
#
#     (2, 9, 4)
#
# Because:
#
#     smallest = 2
#     largest  = 9
#     unique   = {2, 4, 7, 9}
#     count    = 4
#
# Think carefully about which data structure is useful for
# calculating the number of unique values.


def analyse_numbers(numbers):

    if not numbers:
        return ()

    unique_nums = len(set(numbers))
    return min(numbers), max(numbers), unique_nums


print(analyse_numbers([4, 2, 7, 2, 4, 9]))
print(40 * "-")

# ------------------------------------------------------------
# E. HARD — Process records
# ------------------------------------------------------------
# You have a collection of records.
#
# Each record is a dictionary containing:
#
#     {
#         "user": "alice",
#         "status": "success"
#     }
#
# Write a function analyse_records(*records) that returns a tuple
# containing:
#
#     1. A SET of unique usernames
#     2. The number of successful records
#
# Example:
#
#     analyse_records(
#         {"user": "alice", "status": "success"},
#         {"user": "bob", "status": "error"},
#         {"user": "alice", "status": "success"},
#         {"user": "charlie", "status": "success"},
#     )
#
# should return something equivalent to:
#
#     ({"alice", "bob", "charlie"}, 3)
#
# Think about:
#
#     - What should be a set?
#     - What should be a normal integer counter?
#     - What should the function return?
#
# You should build this from scratch.


def analyse_records(*records):
    unique_usernames = set()
    successful_records = 0

    for record in records:
        username = record["user"]

        if username not in unique_usernames:
            unique_usernames.update([record.get("user")])

        if record["status"] == "success":
            successful_records += 1

    return unique_usernames, successful_records


print(
    analyse_records(
        {"user": "alice", "status": "success"},
        {"user": "bob", "status": "error"},
        {"user": "alice", "status": "success"},
        {"user": "charlie", "status": "success"},
    )
)

print(40 * "-")

# ------------------------------------------------------------
# F. HARDEST — Batch summary
# ------------------------------------------------------------
# Build this function completely from scratch:
#
#     batch_summary(*records)
#
# Each record looks like:
#
#     {
#         "id": 1,
#         "user": "alice",
#         "status": "success",
#         "category": "payment"
#     }
#
# The function should return a TUPLE containing:
#
#     1. A SET of unique users
#     2. A SET of unique categories
#     3. The number of successful records
#     4. The number of failed records
#
# Example:
#
#     batch_summary(
#         {
#             "id": 1,
#             "user": "alice",
#             "status": "success",
#             "category": "payment",
#         },
#         {
#             "id": 2,
#             "user": "bob",
#             "status": "error",
#             "category": "login",
#         },
#         {
#             "id": 3,
#             "user": "alice",
#             "status": "success",
#             "category": "login",
#         },
#     )
#
# should return something equivalent to:
#
#     (
#         {"alice", "bob"},
#         {"payment", "login"},
#         2,
#         1,
#     )
#
# IMPORTANT:
#
# Build this one without copying the structure from the previous
# exercises.
#
# Decide for yourself:
#
#     - What variables do you need?
#     - Which ones should be sets?
#     - Which ones should be integers?
#     - Where should .add() be used?
#     - How will you return all four results?
#
# This is the main exercise for this week.


def batch_summary(*records):
    unique_users = set()
    unique_categories = set()
    successful_status = 0
    failed_status = 0

    for record in records:
        user = record.get("user")
        category = record.get("category")
        record_status = record.get("status")

        if user not in unique_users:
            unique_users.update([user])

        if category not in unique_categories:
            unique_categories.update([category])

        if record_status == "error":
            failed_status += 1
        elif record_status == "success":
            successful_status += 1

    return unique_users, unique_categories, successful_status, failed_status


print(
    batch_summary(
        {
            "id": 1,
            "user": "alice",
            "status": "success",
            "category": "payment",
        },
        {
            "id": 2,
            "user": "bob",
            "status": "error",
            "category": "login",
        },
        {
            "id": 3,
            "user": "alice",
            "status": "success",
            "category": "login",
        },
    )
)
