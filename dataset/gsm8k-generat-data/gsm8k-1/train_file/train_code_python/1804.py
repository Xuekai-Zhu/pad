def solution():
    """Giselle had 20 female doves in a birdhouse. After a month, the doves laid 3 eggs each. If 3/4 of the eggs hatched, calculate the total number of doves Giselle has now."""
    female_doves = 20
    eggs_laid = female_doves * 3
    hatched_eggs = eggs_laid * (3/4)
    total_doves = female_doves + (hatched_eggs * 2)
    result = total_doves
    return result

print(solution())