def solution():
    frogs = 160
    dogs = frogs / 2  # There are twice as many frogs as dogs
    cats = 0.8 * dogs  # The number of cats is 20% less than the number of dogs

    # Calculate the total number of animals in the compound
    total_animals = cats + dogs + frogs
    result = total_animals
    return result

print(solution())