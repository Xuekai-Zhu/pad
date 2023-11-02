def solution():
    """Savannah is wrapping presents for her friends and family for Christmas. She has bought 3 rolls of wrapping paper to wrap 12 gifts. If it takes 1 roll to wrap 3 gifts and 1 roll to wrap 5 other gifts, if there is no wrapping paper leftover after Savannah wraps the rest of the gifts, how many gifts did she wrap with the third roll of paper?"""
    # Define the number of gifts wrapped with each roll of wrapping paper
    ROLL_1_GIFTS = 3
    ROLL_2_GIFTS = 5

    # Define the number of rolls of wrapping paper purchased
    NUM_ROLLS = 3

    # Define the total number of gifts to be wrapped
    TOTAL_GIFTS = 12

    # Calculate the number of gifts wrapped with the first two rolls of paper
    gifts_wrapped = ROLL_1_GIFTS + ROLL_2_GIFTS

    # Calculate the number of gifts left to be wrapped
    gifts_left = TOTAL_GIFTS - gifts_wrapped

    # Calculate the number of gifts that can be wrapped with the third roll of paper
    gifts_with_third_roll = gifts_left / NUM_ROLLS

    # Display the number of gifts wrapped with the third roll of paper
    result = gifts_with_third_roll
    return result

print(solution())