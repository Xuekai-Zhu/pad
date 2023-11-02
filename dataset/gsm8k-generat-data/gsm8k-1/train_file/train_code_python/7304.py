def solution():
    """If the number of dogs in the neighborhood was originally half the number of cats in the neighborhood before twenty new dogs were born, and now there are twice as many dogs as cats, how many cats were in the neighborhood, to begin with, if there are 20 cats now?"""
    cats_now = 20
    dogs_now = 2 * cats_now
    new_dogs = 20
    dogs_before = dogs_now - new_dogs
    cats_before = 2 * dogs_before
    result = cats_before
    return result

print(solution())