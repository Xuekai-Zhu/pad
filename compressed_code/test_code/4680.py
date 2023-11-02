def solution():
    
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