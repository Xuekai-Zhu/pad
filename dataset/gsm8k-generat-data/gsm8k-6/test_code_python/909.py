def solution():
    # Calculate the number of dogs in the compound
    num_frogs = 160
    num_dogs = num_frogs / 2  # twice as many frogs as the number of dogs
    # Calculate the number of cats in the compound
    num_cats = 0.8 * num_dogs  # number of cats is 20% less than the number of dogs
    # Calculate the total number of animals in the compound
    total_animals = num_dogs + num_cats + num_frogs
    result = total_animals
    return result

print(solution())