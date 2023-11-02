def solution():
    """In a compound, the number of cats is 20% less than the number of dogs. There are also twice as many frogs as the number of dogs in the compound. Calculate the total number of animals present in the compound if there are 160 frogs."""
    # Define the number of frogs
    frogs = 160

    # Calculate the number of dogs
    dogs = frogs / 2

    # Calculate the number of cats
    cats = dogs * 0.8

    # Calculate the total number of animals
    total_animals = frogs + dogs + cats

    # return the result
    result = total_animals
    return result

print(solution())