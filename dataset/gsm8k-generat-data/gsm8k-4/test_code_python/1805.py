def solution():
    """Giselle had 20 female doves in a birdhouse. After a month, the doves laid 3 eggs each. If 3/4 of the eggs hatched, calculate the total number of doves Giselle has now."""
    # Define the initial number of doves
    doves = 20

    # Calculate the number of eggs laid
    eggs_laid = doves * 3

    # Calculate the number of eggs that hatched
    eggs_hatched = eggs_laid * (3/4)

    # Calculate the number of new doves
    new_doves = eggs_hatched

    # Calculate the total number of doves
    total_doves = doves + new_doves

    # Return the result
    result = total_doves
    return result

print(solution())