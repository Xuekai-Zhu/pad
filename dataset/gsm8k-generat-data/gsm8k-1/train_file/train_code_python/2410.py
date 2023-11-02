def solution():
    """Bo is learning words for the GRE. He got 800 flashcards. He knew 20% of the words on them. He has 40 days to learn the rest. How many words does he need to learn a day?"""
    total_flashcards = 800
    known_flashcards = total_flashcards * 0.2
    unknown_flashcards = total_flashcards - known_flashcards
    days_to_learn = 40
    words_to_learn_per_day = unknown_flashcards / days_to_learn
    result = words_to_learn_per_day
    return result

print(solution())