def solution():
    lilacs_sold = 10

    # Calculate the number of roses sold (3 times the number of lilacs)
    roses_sold = 3 * lilacs_sold

    # Calculate the number of gardenias sold (half the number of lilacs)
    gardenias_sold = lilacs_sold / 2

    # Calculate the total number of flowers sold
    total_sold = lilacs_sold + roses_sold + gardenias_sold
    result = total_sold
    return result

print(solution())