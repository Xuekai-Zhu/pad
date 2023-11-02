def solution():
    """Hartley has 4 puppies that each weigh 7.5 kilograms. The rescue center has 14 cats that each weigh 2.5 kilograms. How many kilograms more do the cats weigh than the puppies?"""
    # Define the weight of each puppy and cat
    PUPPY_WEIGHT = 7.5
    CAT_WEIGHT = 2.5

    # Define the number of puppies and cats
    num_puppies = 4
    num_cats = 14

    # Calculate the total weight of the puppies
    puppy_weight = PUPPY_WEIGHT * num_puppies

    # Calculate the total weight of the cats
    cat_weight = CAT_WEIGHT * num_cats

    # Calculate the difference in weight between the cats and the puppies
    weight_diff = cat_weight - puppy_weight

    # Display the weight difference
    result = weight_diff
    return result

print(solution())