def solution():
    walk_time = 2  # in hours
    bike_time = 1  # in hours
    num_walks = 3
    num_bikes = 2

    # Calculate the total time Roque spends walking to and from work
    total_walk_time = 2 * walk_time * num_walks

    # Calculate the total time Roque spends riding his bike to and from work
    total_bike_time = 2 * bike_time * num_bikes

    # Calculate the total time Roque spends getting to and from work each week
    total_time = total_walk_time + total_bike_time
    result = total_time
    return result

print(solution())