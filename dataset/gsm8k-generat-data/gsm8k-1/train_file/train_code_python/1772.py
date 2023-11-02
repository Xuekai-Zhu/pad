def solution():
    """Savannah is wrapping presents for her friends and family for Christmas. She has bought 3 rolls of wrapping paper to wrap 12 gifts. If it takes 1 roll to wrap 3 gifts and 1 roll to wrap 5 other gifts, if there is no wrapping paper leftover after Savannah wraps the rest of the gifts, how many gifts did she wrap with the third roll of paper?"""
    total_gifts = 12
    gifts_wrapped_with_first_two_rolls = 3*1 + 5*1
    gifts_wrapped_with_third_roll = total_gifts - gifts_wrapped_with_first_two_rolls
    result = gifts_wrapped_with_third_roll
    return result

print(solution())