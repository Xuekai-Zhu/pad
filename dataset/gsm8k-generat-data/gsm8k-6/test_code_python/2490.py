def solution():
    # Calculate the number of cats, birds, and fish for sale
    cats = 6 / 2  # half as many cats as dogs
    birds = 6 * 2  # twice as many birds as dogs
    fish = 6 * 3  # thrice as many fish as dogs

    # Calculate the total number of animals for sale
    total_animals = cats + birds + fish + 6  # add the dogs to the total

    result = total_animals
    return result

print(solution())