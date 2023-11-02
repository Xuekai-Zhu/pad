def solution():
    # Calculate the total number of baths Bridgette gives in a year
    dog_baths = 2 * 12  # the dogs get bathed twice a month for 12 months
    cat_baths = 3 * 12  # the cats get bathed once a month for 12 months
    bird_baths = 4 * 3  # the birds get bathed once every 4 months for 12 months
    total_baths = dog_baths + cat_baths + bird_baths
    result = total_baths
    return result

print(solution())