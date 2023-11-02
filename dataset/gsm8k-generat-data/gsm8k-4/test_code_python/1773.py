def solution():
    """Savannah is wrapping presents for her friends and family for Christmas. She has bought 3 rolls of wrapping paper to wrap 12 gifts. If it takes 1 roll to wrap 3 gifts and 1 roll to wrap 5 other gifts, if there is no wrapping paper leftover after Savannah wraps the rest of the gifts, how many gifts did she wrap with the third roll of paper?"""
    # Define the number of gifts wrapped with 1 roll of paper
    gifts_per_roll1 = 3

    # Define the number of gifts wrapped with the second roll of paper
    gifts_per_roll2 = 5

    # Define the total number of gifts
    total_gifts = 12

    # Calculate the number of gifts wrapped with the first 2 rolls of paper
    gifts_with_first_2_rolls = (1 * gifts_per_roll1) + (1 * gifts_per_roll2)

    # Calculate the number of gifts wrapped with the third roll of paper
    gifts_with_third_roll = total_gifts - gifts_with_first_2_rolls

    # return the result
    result = gifts_with_third_roll
    return result

print(solution())