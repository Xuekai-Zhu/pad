def solution():
    """Mr. and Mrs. Hugo went on a road trip. On the first day, they traveled 200 miles. On the second day, they traveled 3/4 as far. On the third day, they traveled 1/2 as many miles as the first two days combined. How many miles did they travel for 3 days?"""
    first_day_miles = 200
    second_day_miles = 0.75 * first_day_miles
    combined_miles = first_day_miles + second_day_miles
    third_day_miles = 0.5 * combined_miles
    total_miles = first_day_miles + second_day_miles + third_day_miles
    result = total_miles
    return result

print(solution())