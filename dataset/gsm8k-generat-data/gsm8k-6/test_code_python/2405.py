def solution():
    words_per_cycle = 15 * 10  # Lily types 15 words per minute for 10 minutes before taking a break
    complete_cycles = 255 // words_per_cycle  # Calculate the number of complete cycles Lily types for
    remaining_words = 255 % words_per_cycle  # Calculate the remaining words after complete cycles
    time_taken = (complete_cycles * 10) + (remaining_words/15) + 2*(complete_cycles-1)  # Calculate the total time taken including breaks

    result = round(time_taken, 2)
    return result

print(solution())