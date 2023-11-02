def solution():
    paul_time = 4
    total_alligator_time = paul_time + 2  # 2 more hours for the return journey
    num_alligators = 6

    # Calculate the total time for all alligators to walk back to the River Nile
    total_alligator_time *= (1 / (num_alligators + 1))  # including Paul
    total_time = paul_time + total_alligator_time
    result = total_time
    return result

print(solution())