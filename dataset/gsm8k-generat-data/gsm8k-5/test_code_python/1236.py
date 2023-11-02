def solution():
    total_cats = 16 # There are 16 cats in the house
    white_cats = 2 # Two cats are white
    black_cats = total_cats * 0.25 # 25% of the cats are black
    grey_cats = total_cats - white_cats - black_cats # The rest of the cats are grey

    result = grey_cats
    return result

print(solution())