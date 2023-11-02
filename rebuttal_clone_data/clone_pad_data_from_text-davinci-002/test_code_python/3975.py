def solution():
    hours_away = 3
    miles_per_hour = 2
    miles_away = hours_away * miles_per_hour
    hours_returning = 3
    miles_returning = hours_returning * miles_per_hour
    total_miles = miles_away + miles_returning
    result = total_miles
    return result

print(solution())