def solution():
    """Darma can eat 20 peanuts in 15 seconds. At this same rate, how many peanuts could she eat in 6 minutes?"""
    peanuts_per_time = 20 / 15
    seconds_in_minute = 60
    minutes = 6
    total_time = seconds_in_minute * minutes
    total_peanuts = peanuts_per_time * total_time
    result = total_peanuts
    return result

print(solution())