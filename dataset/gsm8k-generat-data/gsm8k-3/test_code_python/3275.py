def solution():
    """A cake of 400 grams is divided into eight equal parts. Nathalie eats one-eighth of the cake, and Pierre eats double what Nathalie ate. How much did Pierre eat, in grams?"""
    # Define the weight of the cake and the number of parts it is divided into
    cake_weight = 400
    parts = 8

    # Calculate the weight of each part of the cake
    part_weight = cake_weight / parts

    # Calculate the weight that Nathalie ate
    nathalie_eats = part_weight

    # Calculate the weight that Pierre ate
    pierre_eats = nathalie_eats * 2

    # Display the weight that Pierre ate
    result = pierre_eats
    return result

print(solution())