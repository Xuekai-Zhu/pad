def solution():
    singing_time = 6
    practicing_time_per_singing_minute = 3
    tantrum_time_per_singing_minute = 5

    # Calculate the total time spent practicing for the entire performance
    total_practice_time = singing_time * practicing_time_per_singing_minute

    # Calculate the total time spent throwing tantrums for the entire performance
    total_tantrum_time = singing_time * tantrum_time_per_singing_minute

    # Calculate the total combined time spent in the final performance
    total_time = singing_time + total_practice_time + total_tantrum_time
    result = total_time
    return result

print(solution())