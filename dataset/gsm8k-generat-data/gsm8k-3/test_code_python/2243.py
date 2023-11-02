def solution():
    """Ginger owns a flower shop, where she sells roses, lilacs, and gardenias. On Tuesday, she sold three times more roses than lilacs, and half as many gardenias as lilacs.  If she sold 10 lilacs, what is the total number of flowers sold on Tuesday?"""
    # Define the number of lilacs sold
    lilacs = 10

    # Calculate the number of roses sold
    roses = lilacs * 3

    # Calculate the number of gardenias sold
    gardenias = lilacs / 2
    
    # Calculate the total number of flowers sold
    total_flowers = lilacs + roses + gardenias

    # Display the total number of flowers sold
    result = total_flowers
    return result

print(solution())