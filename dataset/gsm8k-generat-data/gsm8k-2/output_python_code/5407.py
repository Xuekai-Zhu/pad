def solution():
    """Darma can eat 20 peanuts in 15 seconds. At this same rate, how many peanuts could she eat in 6 minutes?"""
    peanuts_per_second = 20/15
    peanuts_per_minute = peanuts_per_second * 60
    total_peanuts = peanuts_per_minute * 6
    result = total_peanuts
    return result

print(solution())