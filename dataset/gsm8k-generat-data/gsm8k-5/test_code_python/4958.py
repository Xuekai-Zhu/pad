def solution():
    roses_per_bouquet = 12  # Each bouquet of roses contains 12 roses
    total_bouquets = 20  # The flower shop sells 20 bouquets in total today
    rose_bouquets = 10  # The flower shop sells 10 bouquets of roses today
    daisy_bouquets = total_bouquets - rose_bouquets  # The remaining 10 bouquets are daisy bouquets

    # Calculate the total number of flowers sold today
    total_flowers = 190
    roses_sold = roses_per_bouquet * rose_bouquets
    daisies_sold = total_flowers - roses_sold

    # Calculate the number of daisies in each bouquet of daisies
    daisies_per_bouquet = daisies_sold / daisy_bouquets
    result = daisies_per_bouquet
    return result

print(solution())