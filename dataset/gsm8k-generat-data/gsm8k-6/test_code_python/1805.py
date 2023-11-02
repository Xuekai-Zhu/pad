def solution():
    # Calculate the number of eggs laid by the doves
    eggs_laid = 20 * 3  # each dove lays 3 eggs

    # Calculate the number of eggs that hatched
    hatched_eggs = (3/4) * eggs_laid

    # Calculate the total number of doves Giselle has now
    total_doves = 20 + hatched_eggs

    result = total_doves
    return result

print(solution())