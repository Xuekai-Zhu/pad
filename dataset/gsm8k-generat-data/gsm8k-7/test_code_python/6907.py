def solution():
    num_dogs = 2
    dog_baths_per_month = 2

    num_cats = 3
    cat_baths_per_month = 1

    num_birds = 4
    bird_baths_per_year = 3  # Once every 4 months

    # Calculate the total number of baths for dogs in a year
    dog_baths_per_year = num_dogs * dog_baths_per_month * 12

    # Calculate the total number of baths for cats in a year
    cat_baths_per_year = num_cats * cat_baths_per_month * 12

    # Calculate the total number of baths for birds in a year
    bird_baths_per_year = (num_birds * bird_baths_per_year)

    # Calculate the total number of baths
    total_baths = dog_baths_per_year + cat_baths_per_year + bird_baths_per_year
    result = total_baths
    return result

print(solution())