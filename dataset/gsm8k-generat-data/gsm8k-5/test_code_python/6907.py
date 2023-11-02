def solution():
    num_dog_baths = 2 * 12  # Bridgette gives the dogs a bath twice a month, so 24 baths per year
    num_cat_baths = 3 * 12  # Bridgette gives the cats a bath once a month, so 36 baths per year
    num_bird_baths = 4 * (12 // 4)  # Bridgette gives the birds a bath once every 4 months, so 3 baths per year
    total_baths = num_dog_baths + num_cat_baths + num_bird_baths  # Calculate the total number of baths
    result = total_baths
    return result

print(solution())