def solution():
    # Define the time spent resisting and the distance and rate of walking
    resist_time = 20
    distance = 64
    rate = 8

    # Calculate the time it takes to walk the given distance at the given rate
    walk_time = distance / rate

    # Calculate the total time spent
    total_time = resist_time + walk_time
    result = total_time
    return result

print(solution())