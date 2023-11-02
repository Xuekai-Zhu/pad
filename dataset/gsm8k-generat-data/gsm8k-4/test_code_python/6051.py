def solution():
    """Hartley has 4 puppies that each weigh 7.5 kilograms. The rescue center has 14 cats that each weigh 2.5 kilograms. How many kilograms more do the cats weigh than the puppies?"""
    # Define the weight of each puppy and cat
    PUPPY_WEIGHT = 7.5
    CAT_WEIGHT = 2.5

    # Calculate the total weight of the puppies
    puppy_total_weight = PUPPY_WEIGHT * 4

    # Calculate the total weight of the cats
    cat_total_weight = CAT_WEIGHT * 14

    # Calculate the difference in weight between cats and puppies
    weight_difference = cat_total_weight - puppy_total_weight

    # return the result
    result = weight_difference
    return result

print(solution())