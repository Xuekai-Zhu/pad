def solution():
    """John takes a 10-minute shower every other day for 4 weeks. If his shower uses 2 gallons of water per minute. How much water does he use in those 4 weeks?"""
    shower_time = 10
    shower_frequency = 0.5  # every other day
    weeks = 4
    water_per_minute = 2
    total_showers = weeks * 7 * shower_frequency
    total_water_used = total_showers * shower_time * water_per_minute
    result = total_water_used
    return result

print(solution())