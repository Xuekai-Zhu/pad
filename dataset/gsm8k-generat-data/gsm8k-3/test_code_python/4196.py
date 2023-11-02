def solution():
    """A gecko lays 30 eggs per year. 20 percent of them are infertile, and a third of the remaining eggs will not hatch due to calcification issues.  How many eggs actually hatch?"""
    # Calculate the number of infertile eggs
    infertile_eggs = 0.2 * 30

    # Calculate the number of fertile eggs
    fertile_eggs = 30 - infertile_eggs

    # Calculate the number of eggs that will not hatch due to calcification issues
    calcified_eggs = 1/3 * fertile_eggs

    # Calculate the number of eggs that will hatch
    hatching_eggs = fertile_eggs - calcified_eggs

    # Display the number of eggs that will hatch
    result = hatching_eggs
    return result

print(solution())