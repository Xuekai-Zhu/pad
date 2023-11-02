def solution():
    """Weng earns $12 an hour for babysitting. Yesterday, she just did 50 minutes of babysitting. How much did she earn?"""
    hourly_rate = 12
    minutes_worked = 50
    hourly_equivalent = minutes_worked / 60
    total_earned = hourly_rate * hourly_equivalent
    result = total_earned
    return result

print(solution())