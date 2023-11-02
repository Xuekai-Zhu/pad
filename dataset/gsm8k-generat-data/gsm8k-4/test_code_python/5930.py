def solution():
    """Marcy uses 6 ounces of pet cleaner to clean up a dog stain, 4 ounces to clean up a cat stain, and 1 ounce to clean up a rabbit stain. How much cleaner does she need to clean up after 6 dogs, 3 cats and 1 rabbit?"""
    # Define the amount of cleaner needed for each type of animal
    dog_cleaner = 6
    cat_cleaner = 4
    rabbit_cleaner = 1

    # Calculate the total amount of cleaner needed
    total_cleaner = (dog_cleaner * 6) + (cat_cleaner * 3) + rabbit_cleaner

    # return the result
    result = total_cleaner
    return result

print(solution())