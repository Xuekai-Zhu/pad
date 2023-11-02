def solution():
    """Madison makes 30 paper boats and sets them afloat. 20% are eaten by fish and Madison shoots two of the others with flaming arrows. How many boats are left?"""
    # Define the initial number of boats
    initial_boats = 30

    # Calculate the number of boats eaten by fish
    fish_boats = initial_boats * 0.2

    # Calculate the number of boats shot by Madison
    shot_boats = 2

    # Calculate the number of boats left
    remaining_boats = initial_boats - fish_boats - shot_boats

    # return the result
    result = remaining_boats
    return result

print(solution())