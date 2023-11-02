def solution():
    """The lifespan of a hamster is 6 years less than that of a bat. The lifespan of a frog is 4 times that of a hamster. Altogether, the lifespan of the animals is 30 years. What is the lifespan of the bat?"""
    lifespan_frog = 4 * (x - 6) # the lifespan of the hamster is being represented by x
    lifespan_hamster = x - 6
    lifespan_bat = lifespan_hamster + 6
    total_lifespan = lifespan_frog + lifespan_hamster + lifespan_bat
    total_lifespan = 30
    x = 8 # solving for x
    bat_lifespan = lifespan_bat
    result = bat_lifespan
    return result

print(solution())