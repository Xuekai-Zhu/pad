def solution():
    # Calculate how many sets of 5 actors can perform in 1 hour
    sets_in_1_hour = 60 / 20

    # Calculate the total number of actors that can perform in 1 hour
    total_actors_in_1_hour = sets_in_1_hour * 5

    result = total_actors_in_1_hour
    return result

print(solution())