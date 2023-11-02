def solution():
    # Calculate the time to chop the peppers and onions
    pepper_time = 3 * 4
    onion_time = 4 * 2

    # Calculate the time to grate cheese for all the omelets
    cheese_time = 1 * 5

    # Calculate the time to assemble and cook one omelet
    omelet_time = 5

    # Calculate the total time for all the omelets
    total_time = (pepper_time * 4) + (onion_time * 2) + cheese_time + (omelet_time * 5)

    result = total_time
    return result

print(solution())