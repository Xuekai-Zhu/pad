def solution():
    """The lifespan of a hamster is 6 years less than that of a bat. The lifespan of a frog is 4 times that of a hamster. Altogether, the lifespan of the animals is 30 years. What is the lifespan of the bat?"""
    frog_lifespan = 4 * (bat_lifespan - 6)
    hamster_lifespan = frog_lifespan / 4
    total_lifespan = bat_lifespan + frog_lifespan + hamster_lifespan
    bat_lifespan = (30 - (hamster_lifespan + frog_lifespan)) / 2
    result = bat_lifespan
    return result

print(solution())