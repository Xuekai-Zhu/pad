def solution():
    # Define the initial number of cats in the shelter
    initial_cats = 6

    # Subtract the three cats that were adopted
    remaining_cats = initial_cats - 3

    # Add the five kittens
    remaining_cats += 5

    # Subtract the cat that was picked up by its owner
    remaining_cats -= 1

    result = remaining_cats
    return result

print(solution())