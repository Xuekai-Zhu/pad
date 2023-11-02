def solution():
    """A gecko lays 30 eggs per year. 20 percent of them are infertile, and a third of the remaining eggs will not hatch due to calcification issues. How many eggs actually hatch?"""
    total_eggs = 30
    infertile_eggs = total_eggs * 0.2
    viable_eggs = total_eggs - infertile_eggs
    uncalcified_eggs = viable_eggs * (2/3)
    hatchlings = viable_eggs - uncalcified_eggs
    result = hatchlings
    return result

print(solution())