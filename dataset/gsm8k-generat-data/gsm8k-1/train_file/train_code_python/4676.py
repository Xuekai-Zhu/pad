def solution():
    """For a fundraiser, Nellie needs to sell 45 rolls of gift wrap. So far, she has sold 1 roll to her grandmother, 10 rolls to her uncle, and 6 rolls to a neighbor. How many more rolls of gift wrap does Nellie need to sell?"""
    rolls_needed = 45
    rolls_sold = 1 + 10 + 6
    rolls_left = rolls_needed - rolls_sold
    result = rolls_left
    return result

print(solution())