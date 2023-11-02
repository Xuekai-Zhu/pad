def solution():
    """Jill has a difficult test to study for. She decides to study one day for 2 hours. The next day she doubles this amount, and the day after that she studies one hour less than the previous day. How many minutes does Jill study over the 3 days?"""
    day1_hours = 2
    day2_hours = day1_hours * 2
    day3_hours = day2_hours - 1
    total_hours = day1_hours + day2_hours + day3_hours
    minutes_per_hour = 60
    total_minutes = total_hours * minutes_per_hour
    result = total_minutes
    return result

print(solution())