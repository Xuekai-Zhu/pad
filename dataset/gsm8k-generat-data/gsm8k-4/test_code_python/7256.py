def solution():
    """My 2 cats had 3 female kittens and 2 male kittens. How many cats do I have in total?"""
    # Define the number of cats per litter
    CATS_PER_LITTER = 5

    # Define the number of litters
    NUM_LITTERS = 1

    # Calculate the total number of kittens
    total_kittens = CATS_PER_LITTER * NUM_LITTERS

    # Calculate the total number of cats
    total_cats = 2 + total_kittens

    # return the result
    result = total_cats
    return result

print(solution())