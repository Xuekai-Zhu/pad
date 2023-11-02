def solution():
    """Violet is planning a hike through the desert with her dog. Violet needs 800 ml of water per hour hiked and her dog needs 400 ml of water per hour. If Violet can carry 4.8 L of water, how many hours can she and her dog spend hiking?"""
    violet_water_per_hour = 0.8
    dog_water_per_hour = 0.4
    total_water_per_hour = violet_water_per_hour + dog_water_per_hour
    total_water = 4.8
    total_hiking_hours = total_water / total_water_per_hour
    result = total_hiking_hours
    return result

print(solution())