def solution():
    # Calculate the total number of roses sold based on lilacs sold
    roses_sold = 3 * 10  # Ginger sold three times more roses than lilacs
    # Calculate the total number of gardenias sold based on lilacs sold
    gardenias_sold = 10 / 2  # Ginger sold half as many gardenias as lilacs
    # Calculate the total number of flowers sold
    total_sold = roses_sold + 10 + gardenias_sold  # Ginger sold roses, lilacs, and gardenias
    result = total_sold
    return result

print(solution())