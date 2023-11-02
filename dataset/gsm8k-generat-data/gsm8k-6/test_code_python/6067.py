def solution():
    # Calculate the number of dogs and cats Michael has
    dogs = 0.25 * 36
    cats = 0.5 * 36

    # Calculate the number of bunnies Michael has
    bunnies = 36 - dogs - cats
    result = bunnies
    return result

print(solution())