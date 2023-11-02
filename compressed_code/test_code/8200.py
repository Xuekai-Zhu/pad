def solution():
    
    total_trip_miles = 493
    miles_on_first_day = 125
    miles_on_second_day = 223
    miles_on_third_day = total_trip_miles - miles_on_first_day - miles_on_second_day
    result = miles_on_third_day
    return result

print(solution())