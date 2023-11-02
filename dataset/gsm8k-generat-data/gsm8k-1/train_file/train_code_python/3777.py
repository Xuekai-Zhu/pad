def solution():
    """A highway is being extended from its current length of 200 miles up to 650 miles. 50 miles are built on the first day, and three times this amount are built on the second day. How many miles still need to be added to the highway to finish extending it?"""
    current_length = 200
    target_length = 650
    miles_built_day1 = 50
    miles_built_day2 = 3 * miles_built_day1
    total_miles_built = miles_built_day1 + miles_built_day2
    miles_left_to_build = target_length - (current_length + total_miles_built)
    result = miles_left_to_build
    return result

print(solution())