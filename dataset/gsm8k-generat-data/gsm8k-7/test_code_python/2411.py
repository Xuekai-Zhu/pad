def solution():
    total_flashcards = 800
    known_flashcards_percent = 0.20  # 20% known
    unknown_flashcards = total_flashcards - (total_flashcards * known_flashcards_percent)
    num_days = 40

    # Calculate how many words Bo needs to learn in total
    total_words_to_learn = unknown_flashcards

    # Calculate how many words Bo needs to learn per day
    words_per_day = total_words_to_learn / num_days
    result = words_per_day
    return result

print(solution())