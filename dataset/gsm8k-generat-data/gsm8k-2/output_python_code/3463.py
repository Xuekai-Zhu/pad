def solution():
    """Lisa walks 10 meters each minute. Every day, she walks for an hour. How many meters will Lisa walk in two days?"""
    meters_per_minute = 10
    minutes_per_hour = 60
    hours_per_day = 24
    total_meters_per_day = meters_per_minute * minutes_per_hour
    total_meters_per_two_days = total_meters_per_day * 2
    result = total_meters_per_two_days
    return result

print(solution())