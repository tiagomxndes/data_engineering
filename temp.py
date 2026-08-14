"""
Write a function classify_temperature(celsius) that:
Takes a temperature in Celsius (a number)
Returns the string "freezing" if it's ≤ 0
Returns "cold" if it's between 0 and 15 (exclusive of 0, inclusive of 15)
Returns "mild" if it's between 15 and 25 (exclusive of 15, inclusive of 25)
Returns "hot" if it's above 25
"""


def classify_temperature(celsius: float) -> str:
    if celsius <= 0:
        return "freezing"
    elif celsius <= 15:
        return "cold"
    elif celsius <= 25:
        return "mild"
    else:
        return "hot"


print(classify_temperature(-2))
print(classify_temperature(3))
print(classify_temperature(15))
print(classify_temperature(17))
print(classify_temperature(25))
print(classify_temperature(45))
