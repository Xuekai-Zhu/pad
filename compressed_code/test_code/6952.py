def solution():
    
    initial_hens = 10
    initial_eggs = 80
    initial_days = 10
    eggs_per_day_per_hen = initial_eggs / (initial_hens * initial_days)
    total_hens = initial_hens + 15
    total_days = 15
    total_eggs = eggs_per_day_per_hen * total_hens * total_days
    result = total_eggs
    return result

print(solution())