def solution():
    """A gecko lays 30 eggs per year. 20 percent of them are infertile, and a third of the remaining eggs will not hatch due to calcification issues. How many eggs actually hatch?"""
    total_eggs = 30
    infertile_eggs = 0.2 * total_eggs
    fertile_eggs = total_eggs - infertile_eggs
    uncalcified_eggs = fertile_eggs - (fertile_eggs / 3)
    hatched_eggs = fertile_eggs - uncalcified_eggs
    result = hatched_eggs
    return result

print(solution())