def solution():
    # Define the number of lilacs sold
    lilacs_sold = 10

    # Calculate the number of roses sold
    roses_sold = 3 * lilacs_sold

    # Calculate the number of gardenias sold
    gardenias_sold = 0.5 * lilacs_sold

    # Calculate the total number of flowers sold
    total_sold = lilacs_sold + roses_sold + gardenias_sold
    result = total_sold
    return result

print(solution())