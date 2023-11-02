def solution():
    
    roses_sold = 10 * 12
    total_flowers_sold = 190
    daisies_sold = total_flowers_sold - roses_sold
    daisy_bouquets_sold = 10
    daisies_per_bouquet = daisies_sold / daisy_bouquets_sold
    result = daisies_per_bouquet
    return result

print(solution())