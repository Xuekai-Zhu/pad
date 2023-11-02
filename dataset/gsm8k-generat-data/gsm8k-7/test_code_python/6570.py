def solution():
    space_marine_time = 20
    dreadnought_time = 70
    num_space_marines = 6
    num_dreadnoughts = 2

    # Calculate the total time spent painting space marines
    total_space_marine_time = space_marine_time * num_space_marines

    # Calculate the total time spent painting dreadnoughts
    total_dreadnought_time = dreadnought_time * num_dreadnoughts

    # Calculate the total time spent painting all figurines
    total_time = total_space_marine_time + total_dreadnought_time
    result = total_time
    return result

print(solution())