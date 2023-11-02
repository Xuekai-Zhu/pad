def solution():
    chickens = 8
    eggs_per_day = 3
    eggs_per_week = chickens * eggs_per_day
    eggs_per_month = eggs_per_week * 4
    price_per_dozen = 5
    dozens_of_eggs = eggs_per_month / 12
    money_made = dozens_of_eggs * price_per_dozen
    result = money_made
    
    return result

print(solution())