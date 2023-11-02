def solution():
    total_words = 1000
    words_per_half_hour = 300
    current_words = 200

    words_left = total_words - current_words
    half_hours_needed = words_left / words_per_half_hour

    minutes_needed = half_hours_needed * 30
    result = minutes_needed
    return result

print(solution())