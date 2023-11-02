def solution():
    """John collects peaches for 3 hours. He can collect 2 peaches a minute. How many peaches does he collect?"""
    hours = 3
    minutes = hours * 60
    peaches_per_minute = 2
    total_peaches = minutes * peaches_per_minute
    result = total_peaches
    return result

print(solution())