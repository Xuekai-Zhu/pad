def solution():
    
    total_eggs_per_day = 8 * 3
    total_eggs_per_week = total_eggs_per_day * 7
    total_eggs_per_four_weeks = total_eggs_per_week * 4
    dozens_of_eggs = total_eggs_per_four_weeks / 12
    total_income = dozens_of_eggs * 5
    result = total_income
    return result

print(solution())