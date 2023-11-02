def solution():
    """If Chester eats 3 eggs a day for 30 days and then increases it to 5 eggs a day for 30 days, how many dozens of eggs will Chester need for 60 days?"""
    eggs_per_day_first_30_days = 3
    eggs_per_day_second_30_days = 5
    total_days = 60
    total_eggs = (eggs_per_day_first_30_days * 30) + (eggs_per_day_second_30_days * 30)
    dozens_of_eggs = total_eggs / 12
    result = dozens_of_eggs
    return result

print(solution())