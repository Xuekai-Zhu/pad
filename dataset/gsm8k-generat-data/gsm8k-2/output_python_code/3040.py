def solution():
    """On a three-day trip, Wendy drove 125 miles on the first day, and 223 miles on the second day. How many miles did she drive on the third day, if the total miles that Wendy drove for the trip is 493 miles?"""
    total_miles = 493
    first_day_miles = 125
    second_day_miles = 223
    third_day_miles = total_miles - first_day_miles - second_day_miles
    result = third_day_miles
    return result

print(solution())