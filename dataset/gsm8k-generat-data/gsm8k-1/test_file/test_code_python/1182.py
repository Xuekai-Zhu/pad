def solution():
    """Sam ran 3 miles on Monday, Wednesday and Friday. On Tuesday and Thursday, Sam ran 5 miles. How many miles did Sam run this week?"""
    miles_per_day = [3, 5, 3, 5, 3]
    total_miles = sum(miles_per_day)
    result = total_miles
    return result

print(solution())