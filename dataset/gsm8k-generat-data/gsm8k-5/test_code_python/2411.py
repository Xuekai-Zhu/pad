def solution():
    total_flashcards = 800  # Bo has 800 flashcards
    known_percentage = 0.2  # Bo currently knows 20% of the words
    remaining_flashcards = total_flashcards * (1 - known_percentage)  # Bo needs to learn the remaining flashcards
    days_to_learn = 40  # Bo has 40 days to learn the remaining flashcards

    # Calculate the number of words Bo needs to learn per day
    words_per_day = remaining_flashcards / days_to_learn
    result = words_per_day
    return result

print(solution())