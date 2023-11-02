def solution():
    """Ginger owns a flower shop, where she sells roses, lilacs, and gardenias. On Tuesday, she sold three times more roses than lilacs, and half as many gardenias as lilacs. If she sold 10 lilacs, what is the total number of flowers sold on Tuesday?"""
    # Define the number of lilacs sold
    lilacs_sold = 10

    # Calculate the number of roses sold (three times the number of lilacs)
    roses_sold = lilacs_sold * 3

    # Calculate the number of gardenias sold (half the number of lilacs)
    gardenias_sold = lilacs_sold / 2

    # Calculate the total number of flowers sold
    total_sold = lilacs_sold + roses_sold + gardenias_sold

    #return the result
    result = total_sold
    return result

print(solution())