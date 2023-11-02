def solution():
    """A cake of 400 grams is divided into eight equal parts. Nathalie eats one-eighth of the cake, and Pierre eats double what Nathalie ate. How much did Pierre eat, in grams?"""
    # Define the weight of the cake and the number of equal parts
    cake_weight = 400
    equal_parts = 8

    # Calculate the weight of one equal part of the cake
    part_weight = cake_weight / equal_parts

    # Calculate how much Nathalie ate
    nathalie_ate = part_weight

    # Calculate how much Pierre ate
    pierre_ate = nathalie_ate * 2

    result = pierre_ate
    return result

print(solution())