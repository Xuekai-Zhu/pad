def solution():
    # Time taken to get in shape
    time_get_in_shape = 2 

    # Time taken to learn mountain climbing
    time_learn_climbing = 2 * time_get_in_shape 

    # Time taken to climb all seven summits
    time_climb_summits = 7 * 5 

    # Time taken to learn diving and explore caves
    time_learn_diving = 13 
    time_dive = 2 * 12 

    # Total time taken to complete all goals
    total_time = time_get_in_shape + time_learn_climbing + time_climb_summits + time_learn_diving + time_dive
    result = total_time
    return result

print(solution())