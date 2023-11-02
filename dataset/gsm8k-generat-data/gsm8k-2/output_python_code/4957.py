def solution():
    """A flower shop sells bouquets of roses, which each contain 12 roses, and bouquets of daisies, which each contain an equal amount of daisies. The flower shop sells 20 bouquets today. 10 of these were rose bouquets and the remaining 10 bouquets were daisy bouquets. If the flower shop has sold 190 flowers in total today, how many daisies are in each bouquet of daisies?"""
    rose_bouquets = 10
    daisy_bouquets = 10
    total_bouquets = 20
    total_flowers = 190
    rose_flowers = rose_bouquets * 12
    daisy_flowers = total_flowers - rose_flowers
    daisies_per_bouquet = daisy_flowers / daisy_bouquets
    result = daisies_per_bouquet
    return result

print(solution())