def solution():
    miles_per_hour_1 = 30
    hours_1 = 3
    miles_1 = miles_per_hour_1 * hours_1
    miles_per_hour_2 = 25
    hours_2 = 4
    miles_2 = miles_per_hour_2 * hours_2
    days_per_week = 5
    total_miles = miles_1 + miles_2
    weekly_miles = total_miles * days_per_week
    result = weekly_miles
    return result

print(solution())