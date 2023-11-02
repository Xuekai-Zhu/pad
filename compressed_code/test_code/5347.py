def solution():
    
    dog_baths_per_month = 2
    cat_baths_per_month = 1
    bird_baths_per_month = 1/4
    total_baths_per_month = (2 * dog_baths_per_month) + (3 * cat_baths_per_month) + (4 * bird_baths_per_month)
    total_baths_per_year = total_baths_per_month * 12
    result = total_baths_per_year
    return result

print(solution())