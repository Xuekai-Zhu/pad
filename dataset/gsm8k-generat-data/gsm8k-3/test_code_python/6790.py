def solution():
    """Quentin, Skylar, and Colten have a total of 383 chickens.  Quentin has 25 more than double the chickens that Skylar has.  Skylar has 4 less than triple the number of chickens that Colten has.  How many chickens does Colten have?"""
    # Define the total number of chickens
    total_chickens = 383

    # Define the number of chickens that Skylar has
    skylar_chickens = (total_chickens - 25) / 7

    # Define the number of chickens that Quentin has
    quentin_chickens = 2 * skylar_chickens + 25

    # Define the number of chickens that Colten has
    colten_chickens = (skylar_chickens + 4) / 3

    # Display the number of chickens that Colten has
    result = colten_chickens
    return result

print(solution())