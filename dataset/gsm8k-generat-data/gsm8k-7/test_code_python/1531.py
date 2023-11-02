def solution():
    time_to_get_in_shape = 2  # years
    time_to_learn_climbing = 4  # twice the time to get in shape
    time_to_climb_each_mountain = 5  # months per mountain
    time_to_dive_and_explore_caves = 24 + 13  # 2 years to dive, plus 13 months of training

    # Calculate the total time it took to climb all the mountains
    time_to_climb_all_mountains = time_to_climb_each_mountain * 7  # 7 summits to climb

    # Calculate the total time it took to complete all goals
    total_time = time_to_get_in_shape + time_to_learn_climbing + time_to_climb_all_mountains + time_to_dive_and_explore_caves
    result = total_time
    return result

print(solution())