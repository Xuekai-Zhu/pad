def solution():
    """A highway is being extended from its current length of 200 miles up to 650 miles. 50 miles are built on the first day, and three times this amount are built on the second day. How many miles still need to be added to the highway to finish extending it?"""
    current_length = 200
    target_length = 650
    first_day_miles = 50
    second_day_miles = 3 * first_day_miles
    total_miles_built = first_day_miles + second_day_miles
    miles_left = target_length - (current_length + total_miles_built)
    result = miles_left
    return result

print(solution())