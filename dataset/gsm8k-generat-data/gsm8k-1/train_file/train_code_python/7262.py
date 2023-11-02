def solution():
    """Sidney has 4 kittens and 3 adult cats. She has 7 cans of cat food. Each adult cat eats 1 can of food per day. Each kitten eats 3/4 of a can per day. How many additional cans of food does Sidney need to buy to feed all of her animals for 7 days."""
    num_kittens = 4
    num_adult_cats = 3
    total_animals = num_kittens + num_adult_cats
    cans_per_day = num_adult_cats + (num_kittens * 3/4)
    cans_needed = cans_per_day * 7
    
    additional_cans = cans_needed - 7
    
    result = additional_cans
    return result

print(solution())