def solution():
    # Calculate the net rate of filling the pool
    net_rate = 1.6 - 0.1  # rate of water filling the pool minus rate of water leaking from the pool

    # Calculate the time required to fill the pool
    time_in_minutes = 60 / net_rate  # time = amount of water / net rate of filling
    result = time_in_minutes
    return result

print(solution())