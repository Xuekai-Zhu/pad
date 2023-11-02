def solution():
    """Mona bikes 30 miles each week to stay fit. This week, she biked on Monday, Wednesday, and Saturday. On Wednesday, she biked 12 miles. On Saturday, she biked twice as far as on Monday. How many miles did she bike on Monday?"""
    total_miles = 30
    wednesday_miles = 12
    saturday_miles = 2 * monday_miles
    monday_miles = (total_miles - wednesday_miles - saturday_miles) / 3
    result = monday_miles
    return result

print(solution())