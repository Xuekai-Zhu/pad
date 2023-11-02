def solution():
    """Tom dances 4 times a week for 2 hours at a time and does this every year for 10 years. How many hours did he dance?"""
    times_per_week = 4
    hours_per_time = 2
    weeks_per_year = 52
    years = 10
    total_hours = times_per_week * hours_per_time * weeks_per_year * years
    result = total_hours
    return result

print(solution())