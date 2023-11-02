def solution():
    """Jill can run up a hill at 9 feet/second and down a hill at 12 feet/second. How long does it take her to run up and down a 900 foot hill?"""
    uphill_speed = 9
    downhill_speed = 12
    hill_height = 900
    uphill_time = hill_height / uphill_speed
    downhill_time = hill_height / downhill_speed
    total_time = uphill_time + downhill_time
    result = total_time
    return result

print(solution())