def solution():
    """Pancho walks 20 miles a day. Except on weekends when he walks 10 miles. How many miles does he walk in a week?"""
    
    miles_weekdays = 20 * 5
    miles_weekends = 10 * 2
    total_miles = miles_weekdays + miles_weekends
    result = total_miles
    return result

print(solution())