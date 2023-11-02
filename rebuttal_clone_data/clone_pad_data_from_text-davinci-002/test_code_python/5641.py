def solution():
    total_words = 1200
    words_per_hour1 = 400
    words_per_hour2 = 200
    hours_needed = total_words / words_per_hour1 + total_words / (words_per_hour1 + words_per_hour2)
    result = hours_needed
    return result

print(solution())