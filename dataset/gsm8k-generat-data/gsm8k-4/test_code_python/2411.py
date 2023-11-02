def solution():
    """Bo is learning words for the GRE. He got 800 flashcards. He knew 20% of the words on them. He has 40 days to learn the rest. How many words does he need to learn a day?"""
    # Define the total number of flashcards and the percentage of words that Bo already knows
    total_flashcards = 800
    known_percentage = 20

    # Calculate the number of flashcards that Bo still needs to learn
    unknown_flashcards = total_flashcards * (100 - known_percentage) / 100

    # Calculate the number of words Bo needs to learn per day to learn all the words in 40 days
    words_per_day = unknown_flashcards / 40

    result = words_per_day
    return result

print(solution())