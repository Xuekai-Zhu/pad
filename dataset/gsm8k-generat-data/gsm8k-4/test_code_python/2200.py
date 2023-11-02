def solution():
    """Farmer Brown fed 7 chickens and 5 sheep. How many total legs were there among the animals he fed?"""
    # Define the number of legs for each animal
    CHICKEN_LEGS = 2
    SHEEP_LEGS = 4

    # Calculate the total number of chicken legs
    chicken_legs = 7 * CHICKEN_LEGS

    # Calculate the total number of sheep legs
    sheep_legs = 5 * SHEEP_LEGS

    # Calculate the total number of legs among all animals
    total_legs = chicken_legs + sheep_legs

    result = total_legs
    return result

print(solution())