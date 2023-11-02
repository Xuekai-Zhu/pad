def solution():
    roses_per_bouquet = 12
    num_rose_bouquets = 10
    num_daisy_bouquets = 10
    total_bouquets = 20
    total_flowers = 190

    # Calculate the total number of roses sold
    total_roses_sold = num_rose_bouquets * roses_per_bouquet

    # Calculate the total number of daisies sold
    total_daisies_sold = total_flowers - total_roses_sold

    # Calculate the number of daisies in each daisy bouquet
    daisies_per_bouquet = total_daisies_sold / num_daisy_bouquets

    result = daisies_per_bouquet
    return result

print(solution())