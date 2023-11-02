def solution():
    """In a house, there are 16 cats. Two of them are white, and 25% of them are black. The rest of the cats are grey. How many grey cats are in this house?"""
    total_cats = 16
    white_cats = 2
    black_cats = total_cats * 0.25
    grey_cats = total_cats - white_cats - black_cats
    result = grey_cats
    return result

print(solution())