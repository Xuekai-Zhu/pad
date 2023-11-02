def solution():
    # Calculate the total time it took Jack to run up the whole hill
    total_time_jack = 32 + 7

    # Calculate the time it took Jack to run up the first half
    time_first_half_jack = 19

    # Calculate the time it took Jack to run up the second half
    time_second_half_jack = total_time_jack - time_first_half_jack

    result = time_second_half_jack
    return result

print(solution())