def solution():
    # Let x be the lifespan of a bat
    # Then the lifespan of a hamster is x - 6
    # And the lifespan of a frog is 4 * (x - 6)

    # Total lifespan: x + (x - 6) + 4 * (x - 6) = 30
    # Simplifying: 6x = 54
    # Solving: x = 9

    bat_lifespan = 9
    result = bat_lifespan
    return result

print(solution())