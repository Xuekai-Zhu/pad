def solution():
    """Mona bikes 30 miles each week to stay fit. This week, she biked on Monday, Wednesday, and Saturday. On Wednesday, she biked 12 miles. On Saturday, she biked twice as far as on Monday. How many miles did she bike on Monday?"""
    total_miles = 30
    miles_wednesday = 12
    miles_saturday = 2 * miles_monday
    miles_monday = (total_miles - miles_wednesday - miles_saturday) / 3
    result = miles_monday
    return result

print(solution())