def solution():
    collin_flowers = 25  # Collin has 25 flowers
    ingrid_flowers = 33 / 3  # Ingrid gives Collin a third of her 33 flowers
    total_flowers = collin_flowers + ingrid_flowers  # Total number of flowers Collin has

    # Calculate the total number of petals Collin has
    total_petals = total_flowers * 4

    result = total_petals
    return result

print(solution())