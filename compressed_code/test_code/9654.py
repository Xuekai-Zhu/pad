def solution():
    
    saly_eggs = 10
    ben_eggs = 14
    ked_eggs = ben_eggs / 2
    eggs_needed_per_week = saly_eggs + ben_eggs + ked_eggs
    eggs_needed_per_month = eggs_needed_per_week * 4
    result = eggs_needed_per_month
    
    return result

print(solution())