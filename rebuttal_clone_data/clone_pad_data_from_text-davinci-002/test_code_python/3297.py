def solution():
    days_in_year = 365
    days_cycled_30 = 183
    days_cycled_35 = days_in_year - days_cycled_30
    miles_30 = 30 
    miles_35 = 35 
    total_miles = (days_cycled_30 * miles_30) + (days_cycled_35 * miles_35)
    result = total_miles
    return result

print(solution())