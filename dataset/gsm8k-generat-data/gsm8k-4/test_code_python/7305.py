def solution():
    """If the number of dogs in the neighborhood was originally half the number of cats in the neighborhood before twenty new dogs were born, and now there are twice as many dogs as cats, how many cats were in the neighborhood, to begin with, if there are 20 cats now?"""
    # Define the number of cats currently in the neighborhood
    cats_now = 20

    # Calculate the total number of dogs in the neighborhood currently
    dogs_now = 2 * cats_now

    # Calculate the number of dogs in the neighborhood before the new dogs were born
    dogs_before = dogs_now - 20

    # Calculate the number of cats in the neighborhood before the new dogs were born
    cats_before = 2 * dogs_before

    result = cats_before
    return result

print(solution())