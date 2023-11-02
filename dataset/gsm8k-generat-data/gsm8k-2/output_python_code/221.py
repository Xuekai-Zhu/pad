def solution():
    """Mira jogs every morning. She jogs 5 miles per hour. If she jogs for 2 hours every morning, how many miles can she jog for five days?"""
    speed = 5 # miles per hour
    time = 2 # hours per day
    days = 5
    total_distance = speed * time * days
    result = total_distance
    return result

print(solution())