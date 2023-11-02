def solution():
    """Jerome is taking a 150-mile bicycle trip. He wants to ride 12 miles for 12 days. How long will he ride on the 13th day to finish his goal?"""
    total_miles = 150
    miles_per_day = 12
    days = 12
    miles_on_13th_day = total_miles - (miles_per_day * days)
    result = miles_on_13th_day
    return result

print(solution())