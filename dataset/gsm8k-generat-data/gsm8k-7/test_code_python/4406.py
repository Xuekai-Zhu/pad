def solution():
    collin_flowers = 25
    ingrid_flowers = 33
    petal_per_flower = 4

    # Calculate the number of flowers Ingrid gives to Collin
    ingrid_gives = ingrid_flowers / 3

    # Calculate the total number of flowers Collin has
    total_flowers = collin_flowers + ingrid_gives

    # Calculate the total number of petals Collin has
    total_petals = total_flowers * petal_per_flower
    result = total_petals
    return result

print(solution())