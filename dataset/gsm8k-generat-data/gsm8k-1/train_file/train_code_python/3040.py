def solution():
    """On a three-day trip, Wendy drove 125 miles on the first day, and 223 miles on the second day. How many miles did she drive on the third day, if the total miles that Wendy drove for the trip is 493 miles?"""
    total_trip_miles = 493
    miles_on_first_day = 125
    miles_on_second_day = 223
    miles_on_third_day = total_trip_miles - miles_on_first_day - miles_on_second_day
    result = miles_on_third_day
    return result

print(solution())