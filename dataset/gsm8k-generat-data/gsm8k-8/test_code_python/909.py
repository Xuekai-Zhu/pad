def solution():
    # Calculate the number of dogs in the compound
    no_of_frogs = 160
    no_of_dogs = no_of_frogs / 2

    # Calculate the number of cats in the compound
    no_of_cats = 0.8 * no_of_dogs

    # Calculate the total number of animals in the compound
    total_animals = no_of_dogs + no_of_cats + no_of_frogs
    result = total_animals
    return result

print(solution())