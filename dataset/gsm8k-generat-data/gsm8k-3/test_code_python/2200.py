def solution():
    """Farmer Brown fed 7 chickens and 5 sheep. How many total legs were there among the animals he fed?"""
    # Define the number of legs for each type of animal
    CHICKEN_LEGS = 2
    SHEEP_LEGS = 4

    # Define the number of each type of animal
    num_chickens = 7
    num_sheep = 5

    # Calculate the total number of legs
    total_legs = (num_chickens * CHICKEN_LEGS) + (num_sheep * SHEEP_LEGS)

    # Display the total number of legs
    result = total_legs
    return result

print(solution())