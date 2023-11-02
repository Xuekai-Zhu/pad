def solution():
    miles_traveled = 180
    hours_traveled = 4
    additional_hours = 3
    rate_of_speed = miles_traveled / hours_traveled
    additional_miles = additional_hours * rate_of_speed
    result = additional_miles
    return result

print(solution())