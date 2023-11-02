def solution():
    total_businesses = 72
    fired_fraction = 1/2
    quit_fraction = 1/3

    # Calculate the total number of businesses fired from
    num_fired = total_businesses * fired_fraction

    # Calculate the total number of businesses quit from
    num_quit = total_businesses * quit_fraction

    # Calculate the total number of businesses Brandon can still apply to
    num_available = total_businesses - num_fired - num_quit
    result = num_available
    return result

print(solution())