"""
Week 2 — While Loops
Read each theory block, then fill in the exercise below it. Don't look
anything up — if you get stuck, write down what you tried and where it
broke, and send it back anyway.
"""

# ============================================================
# PART 1 — Isolated exercises (one concept each)
# ============================================================

# --- THEORY: Basic while loop ---
# A while loop repeats as long as its condition is True. Unlike a for
# loop, YOU are responsible for making the condition eventually become
# False — otherwise it runs forever (an infinite loop).
# count = 0
# while count < 3:
#     print(count)
#     count += 1   # without this line, the loop never ends


# 1. Write a while loop that prints numbers 1 through 5 (inclusive).
def count_up_to_five():
    count = 1

    while count < 6:
        print(count)
        count += 1


count_up_to_five()


# --- THEORY: break ---
# break immediately exits the loop entirely, regardless of the condition.
# Useful when you want to stop early based on something happening INSIDE
# the loop, not just the original condition.


# 2. Write a while loop that keeps doubling a number starting at 1,
#    printing each value, and stops (using break) as soon as the value
#    exceeds 100.
def double_until_over_100():
    start = 1

    while True:
        print(start)
        start *= 2

        if start > 100:
            break


double_until_over_100()


# --- THEORY: continue ---
# continue skips the rest of the current iteration and jumps back to
# re-check the while condition — it does NOT exit the loop, just skips
# ahead to the next round.

print(40 * "-")


# 3. Write a while loop that goes from 1 to 10, but SKIPS printing any
#    even number (use continue for the even ones).
def print_odds_only():
    start = 0

    while start != 10:
        start += 1
        if start % 2 == 0:
            continue

        print(start)


print_odds_only()


# --- THEORY: Sentinel-controlled loops ---
# A common pattern: loop "until a specific value shows up" rather than a
# fixed number of times. Often used with input() in real programs, but
# here we'll simulate it with a list standing in for a sequence of
# "inputs" you consume one at a time.


# 4. Write a while loop that processes items from the list below ONE AT
#    A TIME (using .pop(0) each iteration) and stops as soon as it pops
#    the value "STOP" — do not process "STOP" itself, just stop there.
def process_until_stop():
    data = ["a", "b", "c", "STOP", "d", "e"]

    while True:
        item = data.pop(0)
        if item == "STOP":
            break

    return data


print(process_until_stop())


# --- THEORY: Infinite loop with a real exit condition ---
# Sometimes you write `while True:` on purpose, with the actual exit
# condition living inside the loop via break. This is common when the
# stopping condition is easier to check partway through the loop body
# than at the top.


# 5. Write a while True loop that starts a counter at 0, increments it
#    each pass, prints it, and breaks out once the counter reaches 4.
def infinite_with_break():
    counter = 0
    while True:
        if counter == 4:
            break
        print(counter)
        counter += 1


infinite_with_break()


# ============================================================
# PART 2 — Build from scratch (easiest → hardest)
# ============================================================

# --- THEORY ---
# These combine everything above. No new concepts — just applying basic
# while loops, break, continue, and sentinel patterns together.

# A. EASIEST
# Write a function countdown(start) that uses a while loop to print
# numbers from `start` down to 1, then prints "Liftoff!" at the end.
# Test with countdown(5).
print(40 * "-")


def countdown(start):
    while start > 0:
        print(start)
        start -= 1
    print("Liftoff!")


print(countdown(5))


# B. MEDIUM
# Write a function find_first_negative(numbers) that uses a while loop
# (with an index, not a for loop) to walk through the list `numbers` and
# return the first negative number it finds. If there are none, return
# None. Use break once it's found — don't keep scanning after.
# Test with find_first_negative([4, 7, 2, -3, 9, -1]) and
# find_first_negative([1, 2, 3]).

print(40 * "-")


def find_first_negative(numbers):

    while numbers:
        popped_number = numbers.pop(0)

        if popped_number < 0:
            break

    if popped_number < 0:  # this is dead code
        return popped_number
    return None


def find_first_negative_2(numbers):
    i = 0
    while i < len(numbers):
        if numbers[i] < 0:
            return numbers[i]
        i += 1
    return None


print(find_first_negative([4, 7, 2, -3, 9, -1]))
print(find_first_negative([1, 2, 3]))
print(find_first_negative([1, -2, 3]))
print(find_first_negative([0, 0, 0]))

print(find_first_negative2([4, 7, 2, -3, 9, -1]))
print(find_first_negative_2([1, 2, 3]))
print(find_first_negative_2([1, -2, 3]))
print(find_first_negative_2([0, 0, 0]))
# C. HARDEST — data engineering flavored
# Write a function drain_queue(*records) that simulates processing a
# queue of records one at a time using a while loop (not a for loop).
# Convert `records` to a list first so you can pop from it. For each
# record (a dict with a "status" field):
#   - if status is "error", stop processing immediately (break) and
#     return two things: the list of records successfully processed so
#     far, and the record that caused the stop
#   - otherwise, add it to the processed list and continue
# If the queue empties without hitting an error, return the processed
# list and None (no error record).
# Test with:
#   drain_queue({"id": 1, "status": "ok"}, {"id": 2, "status": "ok"},
#               {"id": 3, "status": "error"}, {"id": 4, "status": "ok"})
