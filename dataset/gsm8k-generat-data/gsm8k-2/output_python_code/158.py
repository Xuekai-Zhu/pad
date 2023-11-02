def solution():
    """Jerome is taking a 150-mile bicycle trip. He wants to ride 12 miles for 12 days. How long will he ride on the 13th day to finish his goal?"""
    total_distance = 150
    days_ridden = 12
    distance_per_day = 12
    distance_left = total_distance - (distance_per_day * days_ridden)
    distance_on_last_day = distance_left
    result = distance_on_last_day
    return result

print(solution())