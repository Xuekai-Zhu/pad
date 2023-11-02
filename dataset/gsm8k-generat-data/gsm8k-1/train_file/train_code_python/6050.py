def solution():
    """Hartley has 4 puppies that each weigh 7.5 kilograms. The rescue center has 14 cats that each weigh 2.5 kilograms. How many kilograms more do the cats weigh than the puppies?"""
    puppy_weight = 7.5
    cat_weight = 2.5
    num_puppies = 4
    num_cats = 14
    total_puppy_weight = puppy_weight * num_puppies
    total_cat_weight = cat_weight * num_cats
    weight_difference = total_cat_weight - total_puppy_weight
    result = weight_difference
    return result

print(solution())