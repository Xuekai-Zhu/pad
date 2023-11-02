def solution():
    dogs = 2
    cats = 3
    birds = 4
    dog_baths_per_month = 2
    cat_baths_per_month = 1
    bird_baths_per_month = 0.25
    total_baths = (dogs * dog_baths_per_month) + (cats * cat_baths_per_month) + (birds * bird_baths_per_month)
    result = total_baths
    return result

print(solution())