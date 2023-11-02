def solution():
    """John takes a 10-minute shower every other day for 4 weeks. If his shower uses 2 gallons of water per minute. How much water does he use in those 4 weeks?"""
    shower_time = 10
    water_per_minute = 2
    days_per_week = 7
    showers_per_week = 3  # Every other day
    weeks = 4
    total_showers = showers_per_week * weeks
    total_minutes = total_showers * shower_time
    total_gallons = total_minutes * water_per_minute
    result = total_gallons
    return result

print(solution())