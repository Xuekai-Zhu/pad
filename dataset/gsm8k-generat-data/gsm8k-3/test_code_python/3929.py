def solution():
    """Matthew, Patrick and Alvin are eating dinner together. Matthew eats three times as many egg rolls as Patrick eats. Patrick eats half as many egg rolls as Alvin eats. If Alvin ate 4 egg rolls, how many did Matthew eat?"""
    # Define the number of egg rolls Alvin ate
    alvin_egg_rolls = 4

    # Calculate the number of egg rolls Patrick ate
    patrick_egg_rolls = alvin_egg_rolls * 0.5

    # Calculate the number of egg rolls Matthew ate
    matthew_egg_rolls = patrick_egg_rolls * 3

    # Display the number of egg rolls Matthew ate
    result = matthew_egg_rolls
    return result

print(solution())