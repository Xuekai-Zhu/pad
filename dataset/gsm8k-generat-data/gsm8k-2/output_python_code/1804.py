def solution():
    """Giselle had 20 female doves in a birdhouse. After a month, the doves laid 3 eggs each. If 3/4 of the eggs hatched, calculate the total number of doves Giselle has now."""
    initial_doves = 20
    eggs_laid = initial_doves * 3
    hatch_rate = 0.75
    total_doves = initial_doves + (eggs_laid * hatch_rate)
    result = total_doves
    return result

print(solution())