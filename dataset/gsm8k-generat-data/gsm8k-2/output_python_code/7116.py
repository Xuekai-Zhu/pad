def solution():
    """Jack and Jill race up the hill to see who gets there fastest. Jack ran up the first half of the hill in 19 seconds. He finished running up the hill 7 seconds before Jill did. If Jill finished the race in 32 seconds, how long did it take Jack to run up the second half of the hill?"""
    total_time = 32
    first_half_time = 19
    jack_total_time = total_time - 7
    jack_second_half_time = jack_total_time - first_half_time
    result = jack_second_half_time
    return result

print(solution())