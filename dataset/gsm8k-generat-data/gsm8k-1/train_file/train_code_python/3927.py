def solution():
    """If it takes 20 minutes to paint a house, how many houses can you paint in 3 hours?"""
    time_per_house = 20  # in minutes
    hours_available = 3
    houses_painted = (hours_available * 60) // time_per_house
    result = houses_painted
    return result

print(solution())