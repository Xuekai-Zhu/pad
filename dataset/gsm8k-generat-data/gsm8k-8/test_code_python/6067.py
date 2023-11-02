def solution():
    # Calculate the number of dogs
    num_dogs = 0.25 * 36

    # Calculate the number of cats
    num_cats = 0.5 * 36

    # Calculate the total number of dogs and cats
    num_dogs_and_cats = num_dogs + num_cats

    # Calculate the number of bunnies
    num_bunnies = 36 - num_dogs_and_cats
    result = num_bunnies
    return result

print(solution())