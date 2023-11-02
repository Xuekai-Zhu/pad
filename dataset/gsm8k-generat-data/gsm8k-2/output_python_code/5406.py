def solution():
    """Jill has a difficult test to study for. She decides to study one day for 2 hours. The next day she doubles this amount, and the day after that she studies one hour less than the previous day. How many minutes does Jill study over the 3 days?"""
    day1_minutes = 2 * 60
    day2_minutes = 2 * day1_minutes
    day3_minutes = day2_minutes - 60
    total_minutes = day1_minutes + day2_minutes + day3_minutes
    result = total_minutes
    return result

print(solution())