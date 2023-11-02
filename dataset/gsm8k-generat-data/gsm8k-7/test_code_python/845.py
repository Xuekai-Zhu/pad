def solution():
    # Calculate how many sets of 5 actors can perform in an hour
    num_sets_in_hour = 60 // 20  # 60 minutes in an hour, 20 minutes per set (15+5)

    # Calculate the total number of actors that can perform in an hour
    total_actors_in_hour = num_sets_in_hour * 5
    result = total_actors_in_hour
    return result

print(solution())