def solution():
    """A cake of 400 grams is divided into eight equal parts. Nathalie eats one-eighth of the cake, and Pierre eats double what Nathalie ate. How much did Pierre eat, in grams?"""
    cake_weight = 400
    parts = 8
    nathalie_eats = cake_weight / parts
    pierre_eats = 2 * nathalie_eats
    result = pierre_eats
    return result

print(solution())