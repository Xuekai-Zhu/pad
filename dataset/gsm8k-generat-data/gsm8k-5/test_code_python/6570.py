def solution():
    time_per_space_marine = 20  # It takes 20 minutes to paint a space marine
    time_per_dreadnought = 70  # It takes 70 minutes to paint a dreadnought
    num_space_marines = 6  # James paints 6 space marines
    num_dreadnoughts = 2  # James paints 2 dreadnoughts

    # Calculate the total time spent painting
    total_time = (time_per_space_marine * num_space_marines) + (time_per_dreadnought * num_dreadnoughts)
    result = total_time
    return result

print(solution())