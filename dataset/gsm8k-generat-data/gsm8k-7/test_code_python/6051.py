def solution():
    num_puppies = 4
    puppy_weight = 7.5
    num_cats = 14
    cat_weight = 2.5

    # Calculate the total weight of all puppies
    total_puppy_weight = num_puppies * puppy_weight

    # Calculate the total weight of all cats
    total_cat_weight = num_cats * cat_weight

    # Calculate the difference in weight between cats and puppies
    weight_difference = total_cat_weight - total_puppy_weight
    result = weight_difference
    return result

print(solution())