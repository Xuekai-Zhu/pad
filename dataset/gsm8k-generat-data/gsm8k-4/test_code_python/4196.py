def solution():
    """A gecko lays 30 eggs per year. 20 percent of them are infertile, and a third of the remaining eggs will not hatch due to calcification issues. How many eggs actually hatch?"""
    # Define the number of eggs laid by the gecko
    eggs_laid = 30

    # Calculate the number of infertile eggs
    infertile_eggs = eggs_laid * 0.2

    # Calculate the number of fertile eggs
    fertile_eggs = eggs_laid - infertile_eggs

    # Calculate the number of eggs that will not hatch due to calcification issues
    calcification_eggs = fertile_eggs / 3

    # Calculate the number of eggs that will actually hatch
    hatching_eggs = fertile_eggs - calcification_eggs

    # return the result
    result = hatching_eggs
    return result

print(solution())