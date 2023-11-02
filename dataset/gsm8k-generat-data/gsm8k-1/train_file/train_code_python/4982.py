def solution():
    """Violet is planning a hike through the desert with her dog. Violet needs 800 ml of water per hour hiked and her dog needs 400 ml of water per hour. If Violet can carry 4.8 L of water, how many hours can she and her dog spend hiking?"""
    violets_water_per_hour = 800
    dogs_water_per_hour = 400
    total_water_per_hour = violets_water_per_hour + dogs_water_per_hour
    max_hours = (4.8 * 1000) / total_water_per_hour
    result = max_hours
    return result

print(solution())