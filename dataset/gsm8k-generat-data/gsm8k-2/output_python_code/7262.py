def solution():
    """Sidney has 4 kittens and 3 adult cats. She has 7 cans of cat food. Each adult cat eats 1 can of food per day. Each kitten eats 3/4 of a can per day. How many additional cans of food does Sidney need to buy to feed all of her animals for 7 days?"""
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