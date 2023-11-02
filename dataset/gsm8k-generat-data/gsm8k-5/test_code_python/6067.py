def solution():
    total_pets = 36  # Michael has 36 pets
    dogs = 0.25 * total_pets  # 25% of the pets are dogs
    cats = 0.5 * total_pets   # 50% of the pets are cats

    # Calculate the number of bunnies Michael has
    bunnies = total_pets - dogs - cats
    result = bunnies
    return result

print(solution())