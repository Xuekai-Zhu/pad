def solution():
    """If the number of dogs in the neighborhood was originally half the number of cats in the neighborhood before twenty new dogs were born, and now there are twice as many dogs as cats, how many cats were in the neighborhood, to begin with, if there are 20 cats now?"""
    # Define the current number of cats and dogs
    current_cats = 20
    current_dogs = 2 * current_cats

    # Define the number of cats and dogs before the new dogs were born
    original_cats = current_cats - 20
    original_dogs = 0.5 * original_cats + 20

    # Calculate the original number of cats
    original_cats = original_cats + original_dogs - current_dogs

    # Display the original number of cats
    result = original_cats
    return result

print(solution())