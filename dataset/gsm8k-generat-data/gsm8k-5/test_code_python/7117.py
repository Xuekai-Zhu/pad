def solution():
    total_time = 32  # Jill finished the race in 32 seconds
    jack_first_half_time = 19  # Jack ran up the first half of the hill in 19 seconds
    time_difference = 7  # Jack finished 7 seconds before Jill

    # Calculate Jill's time for the second half of the hill by subtracting Jack's first half time and the time difference from her total time
    jill_second_half_time = total_time - jack_first_half_time - time_difference

    # Calculate Jack's time for the second half of the hill by subtracting his first half time from the total time he took to finish the race
    jack_second_half_time = total_time - jack_first_half_time

    result = jack_second_half_time
    return result

print(solution())