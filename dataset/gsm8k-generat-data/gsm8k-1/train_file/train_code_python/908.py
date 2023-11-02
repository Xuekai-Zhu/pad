def solution():
    """In a compound, the number of cats is 20% less than the number of dogs. There are also twice
    as many frogs as the number of dogs in the compound. Calculate the total number of animals present
    in the compound if there are 160 frogs."""
    frogs = 160
    dogs = frogs / 2
    cats = dogs * 0.8
    total_animals = frogs + dogs + cats
    result = total_animals
    return result

print(solution())