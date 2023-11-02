def solution():
    
    adult_cat_food_per_day = 1
    kitten_food_per_day = 3/4
    total_cats = 4 + 3
    total_food_per_day = (adult_cat_food_per_day * 3) + (kitten_food_per_day * 4)
    cans_needed_per_day = total_food_per_day * 7
    cans_already_have = 7
    additional_cans_needed = cans_needed_per_day - cans_already_have
    result = additional_cans_needed
    return result

print(solution())