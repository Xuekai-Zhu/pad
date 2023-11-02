def solution():
    # Define the number of eggs laid per year
    eggs_laid_per_year = 30

    # Calculate the number of infertile eggs
    infertile_eggs = eggs_laid_per_year * 0.2

    # Calculate the number of fertile eggs
    fertile_eggs = eggs_laid_per_year - infertile_eggs

    # Calculate the number of eggs that will not hatch due to calcification issues
    calcified_eggs = fertile_eggs / 3

    # Calculate the number of eggs that will actually hatch
    hatching_eggs = fertile_eggs - calcified_eggs

    result = hatching_eggs
    return result

print(solution())