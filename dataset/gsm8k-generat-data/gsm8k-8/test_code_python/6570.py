def solution():
    # Define the time it takes to paint a space marine and a dreadnought
    space_marine_time = 20
    dreadnought_time = 70

    # Define the number of space marines and dreadnoughts
    num_space_marines = 6
    num_dreadnoughts = 2

    # Calculate the total time spent painting
    total_time = num_space_marines * space_marine_time + num_dreadnoughts * dreadnought_time
    result = total_time
    return result

print(solution())