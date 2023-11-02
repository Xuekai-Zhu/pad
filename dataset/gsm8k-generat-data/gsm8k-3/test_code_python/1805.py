def solution():
    """Giselle had 20 female doves in a birdhouse. After a month, the doves laid 3 eggs each. If 3/4 of the eggs hatched, calculate the total number of doves Giselle has now."""
    # Calculate the number of eggs laid by the doves
    eggs_laid = 20 * 3

    # Calculate the number of eggs that hatched
    eggs_hatched = eggs_laid * 3/4

    # Calculate the total number of doves
    total_doves = 20 + eggs_hatched

    # Display the total number of doves
    result = total_doves
    return result

print(solution())