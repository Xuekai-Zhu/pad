def solution():
    # Define the time it takes to pick the lock on each type of handcuff
    cheap_cuff_time = 6
    expensive_cuff_time = 8

    # Calculate the total time it will take to free all three friends
    total_time = cheap_cuff_time * 3 + expensive_cuff_time * 3

    result = total_time
    return result

print(solution())