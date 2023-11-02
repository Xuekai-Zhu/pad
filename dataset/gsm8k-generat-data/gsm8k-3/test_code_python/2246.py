def solution():
    """The lifespan of a hamster is 6 years less than that of a bat. The lifespan of a frog is 4 times that of a hamster. Altogether, the lifespan of the animals is 30 years. What is the lifespan of the bat?"""
    # Let x be the lifespan of the bat
    x = 0

    # Calculate the lifespan of the hamster
    hamster_lifespan = x - 6

    # Calculate the lifespan of the frog
    frog_lifespan = 4 * hamster_lifespan

    # Calculate the total lifespan of the animals
    total_lifespan = x + hamster_lifespan + frog_lifespan

    # Check if the total lifespan is 30 years
    while total_lifespan != 30:
        # Increment x and recalculate the lifespans and total lifespan
        x += 1
        hamster_lifespan = x - 6
        frog_lifespan = 4 * hamster_lifespan
        total_lifespan = x + hamster_lifespan + frog_lifespan

    # Display the lifespan of the bat
    result = x
    return result

print(solution())