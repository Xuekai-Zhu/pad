def solution():
    # Find Tina's mile time
    tina_time = 6  # given in the problem
    tom_time = tina_time / (1/3)  # Tom is 3 times faster than Tina
    tony_time = tina_time / 2  # Tony is twice as fast as Tina

    # Add all three mile times together
    total_time = tina_time + tom_time + tony_time
    result = total_time
    return result

print(solution())