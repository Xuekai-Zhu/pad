def solution():
    """Claire makes a 3 egg omelet every morning for breakfast. How many dozens of eggs will she eat in 4 weeks?"""
    eggs_per_omelet = 3
    omelets_per_day = 1
    days_per_week = 7
    weeks = 4
    eggs_per_dozen = 12
    total_eggs = eggs_per_omelet * omelets_per_day * days_per_week * weeks
    dozens_of_eggs = total_eggs / eggs_per_dozen
    result = dozens_of_eggs
    return result

print(solution())