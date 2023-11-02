def solution():
    total_animals = 21  # Brenda needs to spay 21 animals
    dogs = 2 * cats  # Brenda needs to spay twice as many dogs as cats

    # Solve for the number of cats
    cats = (total_animals / 3)  # Brenda needs to spay one-third of the animals as cats

    result = cats
    return result

print(solution())