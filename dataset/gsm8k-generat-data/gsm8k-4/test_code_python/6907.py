def solution():
    """Bridgette has 2 dogs, 3 cats, and 4 birds. She gives the dogs a bath twice a month. She gives the cats a bath once a month. She gives the birds a bath once every 4 months. In a year, how many baths does she give?"""
    # Define the number of baths each pet receives
    dog_baths = 2 * 12
    cat_baths = 1 * 12
    bird_baths = 1 * (12 // 4)

    # Calculate the total number of baths
    total_baths = dog_baths + cat_baths + bird_baths

    # return the result
    result = total_baths
    return result

print(solution())