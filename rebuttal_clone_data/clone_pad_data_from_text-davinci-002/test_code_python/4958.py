def solution():
     total_bouquets = 20
     rose_bouquets = 10
     daisy_bouquets = total_bouquets - rose_bouquets
     roses_sold = rose_bouquets * 12
     total_flowers_sold = roses_sold + daisy_bouquets
     daisies_sold = total_flowers_sold - roses_sold
     daisies_per_bouquet = daisies_sold / daisy_bouquets
     result = daisies_per_bouquet
     return result

print(solution())