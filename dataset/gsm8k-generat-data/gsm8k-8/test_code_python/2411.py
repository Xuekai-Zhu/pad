def solution():
    # Define the total number of flashcards and the percentage Bo already knows
    total_flashcards = 800
    known_percent = 0.2

    # Calculate the number of flashcards Bo needs to learn
    unknown_flashcards = total_flashcards - (total_flashcards * known_percent)

    # Calculate the number of flashcards Bo needs to learn per day
    flashcards_per_day = unknown_flashcards / 40
    result = flashcards_per_day
    return result

print(solution())