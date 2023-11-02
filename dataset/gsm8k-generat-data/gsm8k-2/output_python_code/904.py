def solution():
    """Sue works in a factory and every 30 minutes, a machine she oversees produces 30 cans of soda. How many cans of soda can one machine produce in 8 hours?"""
    cans_per_30_minutes = 30
    minutes_per_hour = 60
    hours = 8
    cans_per_hour = (cans_per_30_minutes * minutes_per_hour) / 30
    total_cans = cans_per_hour * hours
    result = total_cans
    return result

print(solution())