def solution():
    
    total_flashcards = 800
    known_flashcards = total_flashcards * 0.2
    unknown_flashcards = total_flashcards - known_flashcards
    days_to_learn = 40
    words_to_learn_per_day = unknown_flashcards / days_to_learn
    result = words_to_learn_per_day
    return result

print(solution())