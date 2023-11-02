def solution():
    """Bridgette has 2 dogs, 3 cats, and 4 birds. She gives the dogs a bath twice a month. She gives the cats a bath once a month. She gives the birds a bath once every 4 months. In a year, how many baths does she give?"""
    # Define the number of pets and their bathing frequency
    NUM_DOGS = 2
    DOG_BATHS_PER_MONTH = 2
    NUM_CATS = 3
    CAT_BATHS_PER_MONTH = 1
    NUM_BIRDS = 4
    BIRD_BATHS_PER_YEAR = 12 / 4

    # Calculate the total number of baths given in a year
    total_baths = (NUM_DOGS * DOG_BATHS_PER_MONTH * 12) + \
                  (NUM_CATS * CAT_BATHS_PER_MONTH * 12) + \
                  (NUM_BIRDS * BIRD_BATHS_PER_YEAR)

    # Display the total number of baths
    result = total_baths
    return result

print(solution())