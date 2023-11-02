def solution():
    num_hens = 10
    egg_price_per_dozen = 3
    total_egg_sales = 120
    num_weeks = 4
    
    # Calculate the total number of dozens of eggs sold in 4 weeks
    total_dozen_eggs = total_egg_sales / egg_price_per_dozen
    
    # Calculate the total number of eggs sold in 4 weeks
    total_eggs = total_dozen_eggs * 12
    
    # Calculate the average number of eggs laid per hen per week
    eggs_per_week_per_hen = total_eggs / (num_hens * num_weeks)
    
    result = eggs_per_week_per_hen
    return result

print(solution())