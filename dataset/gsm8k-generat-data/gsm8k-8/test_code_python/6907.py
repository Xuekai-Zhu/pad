def solution():
    total_dog_baths_per_month = 2 * 2 # 2 dogs, 2 baths each
    total_cat_baths_per_month = 3 * 1 # 3 cats, 1 bath each
    total_bird_baths_per_month = 4 * (1/4) # 4 birds, 1 bath every 4 months
    total_baths_per_month = total_dog_baths_per_month + total_cat_baths_per_month + total_bird_baths_per_month
    total_baths_per_year = total_baths_per_month * 12 # multiply by 12 months in a year
    result = total_baths_per_year
    return result

print(solution())