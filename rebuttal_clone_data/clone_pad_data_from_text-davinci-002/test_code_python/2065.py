def solution():
    days_away = 7
    eggs_laid_per_day = 3
    total_eggs_laid = days_away * eggs_laid_per_day
    eggs_taken_by_neighbor = 12
    total_eggs = total_eggs_laid - eggs_taken_by_neighbor
    eggs_dropped = 5
    final_total = total_eggs - eggs_dropped
    result = final_total
    return result

print(solution())