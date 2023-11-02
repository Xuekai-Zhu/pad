def solution():
    """Every morning, Jason eats an omelet made using three eggs. How many eggs will Jason consume in two weeks?"""
    eggs_per_omelet = 3
    days_in_two_weeks = 14
    eggs_per_day = eggs_per_omelet * 1
    total_eggs = eggs_per_day * days_in_two_weeks
    result = total_eggs
    return result

print(solution())