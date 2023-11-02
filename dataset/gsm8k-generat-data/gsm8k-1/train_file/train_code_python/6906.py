def solution():
    """Bridgette has 2 dogs, 3 cats, and 4 birds. She gives the dogs a bath twice a month. She gives the cats a bath once a month. She gives the birds a bath once every 4 months. In a year, how many baths does she give?"""
    dogs = 2
    cats = 3
    birds = 4
    dog_baths_per_month = 2
    cat_baths_per_month = 1
    bird_baths_per_four_months = 1
    total_dog_baths_per_year = dogs * dog_baths_per_month * 12
    total_cat_baths_per_year = cats * cat_baths_per_month * 12
    total_bird_baths_per_year = (birds * bird_baths_per_four_months) // 4 * 12
    total_baths_per_year = total_dog_baths_per_year + total_cat_baths_per_year + total_bird_baths_per_year
    result = total_baths_per_year
    return result

print(solution())