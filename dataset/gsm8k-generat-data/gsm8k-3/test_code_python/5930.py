def solution():
    """Marcy uses 6 ounces of pet cleaner to clean up a dog stain, 4 ounces to clean up a cat stain, and 1 ounce to clean up a rabbit stain. How much cleaner does she need to clean up after 6 dogs, 3 cats and 1 rabbit?"""
    # Define the amount of cleaner needed for each type of pet
    DOG_CLEANER = 6
    CAT_CLEANER = 4
    RABBIT_CLEANER = 1

    # Define the number of pets Marcy needs to clean up after
    num_dogs = 6
    num_cats = 3
    num_rabbits = 1

    # Calculate the total amount of cleaner needed
    total_cleaner = (DOG_CLEANER * num_dogs) + (CAT_CLEANER * num_cats) + (RABBIT_CLEANER * num_rabbits)

    # Display the total amount of cleaner needed
    result = total_cleaner
    return result

print(solution())