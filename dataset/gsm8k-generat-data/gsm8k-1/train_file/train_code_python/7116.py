def solution():
    """Jack and Jill race up the hill to see who gets there fastest. Jack ran up the first half of the hill in 19 seconds. He finished running up the hill 7 seconds before Jill did. If Jill finished the race in 32 seconds, how long did it take Jack to run up the second half of the hill?"""
    jill_time = 32
    jack_time = jill_time + 7
    half_time = jack_time / 2 - 19
    result = half_time
    return result

print(solution())