def solution():
    # Let x be the lifespan of the bat
    # Then the lifespan of the hamster is x - 6
    # And the lifespan of the frog is 4(x - 6) = 4x - 24
    # The total lifespan is x + x - 6 + 4x - 24 = 6x - 30
    # Setting this to 30, we get 6x = 60, so x = 10
    lifespan_bat = 10
    result = lifespan_bat
    return result

print(solution())