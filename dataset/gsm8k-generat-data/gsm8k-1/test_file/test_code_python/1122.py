def solution():
    """Alfie, the albatross, flies 400 kilometers every day. If the circumference of the earth is 40,000 kilometers, how many days will it take Alfie to fly a distance equal to half of the way around the earth?"""
    distance_around_earth = 40000
    half_distance = distance_around_earth / 2
    daily_distance = 400
    days_to_fly_half_distance = half_distance / daily_distance
    result = days_to_fly_half_distance
    return result

print(solution())