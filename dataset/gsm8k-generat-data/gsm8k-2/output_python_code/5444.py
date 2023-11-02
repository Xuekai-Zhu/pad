def solution():
    """Kennedy’s car can drive 19 miles per gallon of gas. She was able to drive 15 miles to school, 6 miles to the softball park, 2 miles to a burger restaurant, 4 miles to her friend’s house, and 11 miles home before she ran out of gas. How many gallons of gas did she start with?"""
    total_miles = 15 + 6 + 2 + 4 + 11
    miles_per_gallon = 19
    gallons_used = total_miles / miles_per_gallon
    gallons_start = gallons_used
    result = gallons_start
    return result

print(solution())