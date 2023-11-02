def solution():
    total_time = 32  # total time for Jill to finish
    jack_first_half_time = 19
    jill_time = total_time + 7  # Jill finishes 7 seconds after Jack

    # Calculate the total time it took Jack to run up the hill
    jack_total_time = jill_time + jack_first_half_time

    # Calculate the time it took Jack to run up the second half of the hill
    jack_second_half_time = jack_total_time - jack_first_half_time - jill_time

    result = jack_second_half_time
    return result

print(solution())