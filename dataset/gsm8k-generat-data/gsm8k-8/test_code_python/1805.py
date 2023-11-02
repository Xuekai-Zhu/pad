def solution():
    # Calculate the number of eggs laid by the doves
    eggs_laid = 20 * 3

    # Calculate the number of eggs that hatched
    hatched_eggs = eggs_laid * 3/4

    # Calculate the total number of new doves
    new_doves = hatched_eggs * 1/3

    # Calculate the total number of doves Giselle has now
    total_doves = 20 + new_doves
    result = total_doves
    return result

print(solution())