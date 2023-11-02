def solution():
    """A flower shop sells bouquets of roses, which each contain 12 roses, and bouquets of daisies, which each contain an equal amount of daisies. The flower shop sells 20 bouquets today. 10 of these were rose bouquets and the remaining 10 bouquets were daisy bouquets. If the flower shop has sold 190 flowers in total today, how many daisies are in each bouquet of daisies?"""
    # Define the number of bouquets sold for each type of flower
    rose_bouquets = 10
    daisy_bouquets = 10

    # Define the number of flowers in each rose bouquet
    roses_per_bouquet = 12

    # Calculate the number of daisies sold
    total_flowers = 190
    daisy_flowers = total_flowers - (rose_bouquets * roses_per_bouquet)

    # Calculate the number of daisies in each daisy bouquet
    daisies_per_bouquet = daisy_flowers // daisy_bouquets

    # Display the number of daisies in each daisy bouquet
    result = daisies_per_bouquet
    return result

print(solution())