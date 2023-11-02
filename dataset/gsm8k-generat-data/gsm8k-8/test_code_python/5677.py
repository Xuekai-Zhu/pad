def solution():
    words_per_page = 450
    typing_speed = 90  # words per minute
    pages_to_type = 10

    total_words = words_per_page * pages_to_type
    minutes_to_type = total_words / typing_speed
    result = minutes_to_type
    return result

print(solution())