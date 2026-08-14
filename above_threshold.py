"""
Exercise 2 — Lists & loops

Write a function average_above_threshold(numbers, threshold) that:
Takes a list of numbers and a threshold value
Returns the average of only the numbers greater than the threshold
If no numbers are above the threshold, return 0
Example: average_above_threshold([10, 20, 30, 40], 15) → average of [20, 30, 40] → 30.0
"""


def average_above_threshold(numbers, threshold) -> float:
    above = [num for num in numbers if num > threshold and numbers != []]
    if above:
        return sum(above) / len(above)
    else:
        return 0


print(average_above_threshold([10, 20, 30, 40], 15))
