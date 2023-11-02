def solution():
    """A flower shop sells bouquets of roses, which each contain 12 roses, and bouquets of daisies, which each contain an equal amount of daisies. The flower shop sells 20 bouquets today. 10 of these were rose bouquets and the remaining 10 bouquets were daisy bouquets. If the flower shop has sold 190 flowers in total today, how many daisies are in each bouquet of daisies?"""
    roses_sold = 10 * 12
    total_flowers_sold = 190
    daisies_sold = total_flowers_sold - roses_sold
    daisy_bouquets_sold = 10
    daisies_per_bouquet = daisies_sold / daisy_bouquets_sold
    result = daisies_per_bouquet
    return result

print(solution())