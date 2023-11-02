def solution():
    """Jenny is trying to convince her cat to walk on a leash. The cat spends twenty minutes resisting. Then Jenny coaxes the cat to walk 64 feet at a rate of 8 feet/minute. How many minutes does this whole process take?"""
    # Define the time spent resisting and the distance walked
    resistance_time = 20  # minutes
    distance_walked = 64  # feet

    # Calculate the time taken to walk the distance
    walking_time = distance_walked / 8  # minutes

    # Calculate the total time taken
    total_time = resistance_time + walking_time  # minutes

    result = total_time
    return result

print(solution())