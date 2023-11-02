def solution():
    # Let's assign g to be the number of goats and c to be the number of chickens
    # We know that g = 4c and g = 4cows
    # Combining these two, we get 4c = 9g/4, which simplifies to c = 9g/16
    # We also know that g = 2c, so substituting, we get 2c = 9g/16
    # Combining these two equations, we can solve for c:

    c = 9/32 * g

    # Now, we know that the total number of animals is g + 9 + c.
    # Substituting for c, we get:

    total_animals = g + 9 + 9/32 * g

    # We don't know the actual number of animals, but we do know that it must be a whole number.
    # The only way this can be a whole number is if g is a multiple of 32.
    # Let's try some multiples:

    for g in range(32, 1000, 32):
        if total_animals == int(total_animals):
            break
        else:
            total_animals = g + 9 + 9/32 * g

    chickens = 9/32 * g
    result = chickens
    return result

print(solution())