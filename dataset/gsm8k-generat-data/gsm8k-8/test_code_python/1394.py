def solution():
    # Let x be the number of chickens
    # Jen has 10 more ducks than four times the number of chickens
    # Therefore, 150 = 4x + 10
    # Solving for x, we get x = 35
    x = 35

    # Jen has 10 more ducks than four times the number of chickens
    # Therefore, Jen has 4x + 10 ducks
    # Substituting x = 35, we get Jen has 4(35) + 10 ducks = 150 ducks
    # Total number of birds = number of ducks + number of chickens
    total_birds = 150 + x
    result = total_birds
    return result

print(solution())