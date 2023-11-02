def solution():
    initial_wpm = 212
    reduced_wpm = initial_wpm - 40
    total_words = 3440
    minutes_to_type = total_words / reduced_wpm
    result = minutes_to_type
    return result

print(solution())