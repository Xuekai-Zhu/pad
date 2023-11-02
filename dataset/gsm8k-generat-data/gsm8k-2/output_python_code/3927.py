def solution():
    """If it takes 20 minutes to paint a house, how many houses can you paint in 3 hours?"""
    time_per_house = 20 / 60  # convert to hours
    total_time = 3  # hours
    num_houses = total_time / time_per_house
    result = num_houses
    return result

print(solution())