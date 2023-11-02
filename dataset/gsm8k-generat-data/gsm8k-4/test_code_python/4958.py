def solution():
    """A flower shop sells bouquets of roses, which each contain 12 roses, and bouquets of daisies, which each contain an equal amount of daisies. The flower shop sells 20 bouquets today. 10 of these were rose bouquets and the remaining 10 bouquets were daisy bouquets. If the flower shop has sold 190 flowers in total today, how many daisies are in each bouquet of daisies?"""
    # Calculate the total number of roses sold
    roses_sold = 10 * 12

    # Calculate the total number of flowers sold
    total_sold = 190

    # Calculate the total number of daisies sold
    daisies_sold = total_sold - roses_sold

    # Calculate the number of daisies in each daisy bouquet
    daisies_per_bouquet = daisies_sold / 10

    # Return the result
    result = daisies_per_bouquet
    return result

print(solution())