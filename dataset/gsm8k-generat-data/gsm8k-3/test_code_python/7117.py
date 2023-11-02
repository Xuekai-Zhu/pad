def solution():
    """Jack and Jill race up the hill to see who gets there fastest. Jack ran up the first half of the hill in 19 seconds. He finished running up the hill 7 seconds before Jill did. If Jill finished the race in 32 seconds, how long did it take Jack to run up the second half of the hill?"""
    # Calculate Jill's time for the first half of the hill
    jill_time_half1 = 32 / 2

    # Calculate Jack's time for the first half of the hill
    jack_time_half1 = 19

    # Calculate Jack's total time to run up the hill
    jack_total_time = jill_time_half1 + 7

    # Calculate Jack's time for the second half of the hill
    jack_time_half2 = jack_total_time - jack_time_half1

    # Display Jack's time for the second half of the hill
    result = jack_time_half2
    return result

print(solution())