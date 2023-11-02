def solution():
    total_cards = 800
    known_words = total_cards * 0.2
    unknown_words = total_cards - known_words
    days_to_learn = 40
    words_per_day = unknown_words / days_to_learn
    result = words_per_day
    return result

print(solution())