def solution():
    """Savannah is wrapping presents for her friends and family for Christmas. She has bought 3 rolls of wrapping paper to wrap 12 gifts. If it takes 1 roll to wrap 3 gifts and 1 roll to wrap 5 other gifts, if there is no wrapping paper leftover after Savannah wraps the rest of the gifts, how many gifts did she wrap with the third roll of paper?"""
    total_gifts = 12
    roll_1_gifts = 3
    roll_2_gifts = 5
    roll_1_count = total_gifts // roll_1_gifts
    roll_2_count = total_gifts // roll_2_gifts
    roll_3_gifts = total_gifts - (roll_1_count * roll_1_gifts) - (roll_2_count * roll_2_gifts)
    result = roll_3_gifts
    return result

print(solution())