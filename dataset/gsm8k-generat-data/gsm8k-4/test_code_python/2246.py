def solution():
    """The lifespan of a hamster is 6 years less than that of a bat. The lifespan of a frog is 4 times that of a hamster. Altogether, the lifespan of the animals is 30 years. What is the lifespan of the bat?"""
    # Define the lifespan of the hamster and the frog
    hamster_lifespan = None
    frog_lifespan = None

    # Define the equation system:
    # h = b - 6
    # f = 4h
    # b + h + f = 30

    # Solve for the hamster's lifespan
    hamster_lifespan = ((-1) * 7 + (17)**(1/2)) / 2

    # Solve for the frog's lifespan
    frog_lifespan = 4 * hamster_lifespan

    # Solve for the bat's lifespan
    bat_lifespan = hamster_lifespan + 6

    result = bat_lifespan
    return result

print(solution())