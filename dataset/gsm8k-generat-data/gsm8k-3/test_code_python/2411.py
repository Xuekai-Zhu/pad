def solution():
    """Bo is learning words for the GRE.  He got 800 flashcards.  He knew 20% of the words on them.  He has 40 days to learn the rest. How many words does he need to learn a day?"""
    # Define the total number of flashcards and the percentage of words Bo already knows
    total_flashcards = 800
    percentage_known = 0.2

    # Calculate the number of flashcards Bo needs to learn
    flashcards_to_learn = total_flashcards - (total_flashcards * percentage_known)

    # Calculate the number of flashcards Bo needs to learn each day
    flashcards_per_day = flashcards_to_learn / 40

    # Display the number of flashcards Bo needs to learn each day
    result = flashcards_per_day
    return result

print(solution())