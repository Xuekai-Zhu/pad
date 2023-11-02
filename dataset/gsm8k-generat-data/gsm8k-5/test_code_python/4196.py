def solution():
    eggs_per_year = 30  # A gecko lays 30 eggs per year
    infertile_percentage = 0.2  # 20% of the eggs are infertile
    fertile_eggs = eggs_per_year - (eggs_per_year * infertile_percentage)  # Calculate the number of fertile eggs
    unhatchable_percentage = 1 / 3  # A third of the remaining eggs are unhatchable due to calcification issues
    hatching_eggs = fertile_eggs - (fertile_eggs * unhatchable_percentage)  # Calculate the number of hatching eggs
    result = hatching_eggs
    return result

print(solution())