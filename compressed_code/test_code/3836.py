def solution():
    
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