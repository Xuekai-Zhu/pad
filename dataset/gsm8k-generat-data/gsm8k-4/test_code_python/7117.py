def solution():
    """Jack and Jill race up the hill to see who gets there fastest. Jack ran up the first half of the hill in 19 seconds. He finished running up the hill 7 seconds before Jill did. If Jill finished the race in 32 seconds, how long did it take Jack to run up the second half of the hill?"""
    # Define variables for the time it took Jack to run the second half and the total time it took Jill to run the whole hill
    jack_second_half_time = None
    jill_total_time = 32

    # Calculate the time it took Jack to run the whole hill based on the information given
    jack_total_time = jill_total_time + 7 + 19

    # Calculate the time it took Jack to run the second half of the hill
    jack_second_half_time = jack_total_time / 2 - 19

    result = jack_second_half_time
    return result

print(solution())