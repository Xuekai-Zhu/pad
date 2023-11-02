def solution():
    """A cake of 400 grams is divided into eight equal parts. Nathalie eats one-eighth of the cake, and Pierre eats double what Nathalie ate. How much did Pierre eat, in grams?"""
    cake_weight = 400
    nathalie_share = cake_weight / 8
    pierre_share = nathalie_share * 2
    result = pierre_share
    return result

print(solution())