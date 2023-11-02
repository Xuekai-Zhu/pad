def solution():
    initial_cats = 12 / 2  # initial number of cats before the new ones arrived
    adopted_cats = 3
    kittens = 5
    missing_pet = 1

    # Calculate the current number of cats in the shelter
    current_cats = initial_cats + 12 - adopted_cats - kittens - missing_pet
    result = current_cats
    return result

print(solution())