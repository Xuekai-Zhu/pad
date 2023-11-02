def solution():
    """A pipe is clogged so that only 2 ounces of cleaner can run through the pipe per minute. After fifteen minutes, the cleaner has unclogged it enough that 3 ounces can run through per minute. Ten minutes later, the clog is cleared enough for 4 ounces to run through per minute. How many ounces of cleaner were used after 30 minutes?"""
    first_phase = 2 * 15
    second_phase = 3 * 10
    third_phase = 4 * 5
    total_cleaner = first_phase + second_phase + third_phase
    result = total_cleaner
    return result

print(solution())