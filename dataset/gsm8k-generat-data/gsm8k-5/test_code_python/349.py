def solution():
    # Let's use variables to represent the number of goats, cows, and pigs respectively
    # We can represent the number of cows in terms of the number of goats
    # And we know the number of pigs is twice the number of cows
    # So we can set up an equation using the total number of animals
    # goats + cows + pigs = 56
    # cows = goats + 4
    # pigs = 2 * cows

    # Substituting the equations for cows and pigs into the total equation
    # goats + (goats + 4) + (2 * (goats + 4)) = 56
    # Simplifying the equation
    # 5 * goats + 12 = 56
    # Solving for goats
    goats = (56 - 12) / 5
    result = goats
    return result

print(solution())