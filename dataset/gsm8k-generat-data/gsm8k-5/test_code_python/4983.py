def solution():
    water_per_hour_violet = 800  # Violet needs 800 ml of water per hour hiked
    water_per_hour_dog = 400  # Her dog needs 400 ml of water per hour hiked
    total_water_carried = 4800  # Violet can carry 4.8 L of water, which is equivalent to 4800 ml of water

    # Calculate how many hours they can hike with the water Violet carries
    hours_hiked = total_water_carried / (water_per_hour_violet + water_per_hour_dog)
    result = hours_hiked
    return result

print(solution())