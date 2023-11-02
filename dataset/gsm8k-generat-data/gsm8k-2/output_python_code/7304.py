def solution():
    """If the number of dogs in the neighborhood was originally half the number of cats in the neighborhood before twenty new dogs were born, and now there are twice as many dogs as cats, how many cats were in the neighborhood, to begin with, if there are 20 cats now?"""
    current_cats = 20
    new_dogs = 20
    current_dogs = 2 * current_cats - new_dogs
    original_cats = current_cats * 2 - new_dogs
    result = original_cats
    return result

print(solution())