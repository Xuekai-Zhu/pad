def solution():
    
    chickens = 8
    eggs_per_chicken = 3
    eggs_per_day = chickens * eggs_per_chicken
    dozen_per_day = eggs_per_day / 12
    price_per_dozen = 5
    dozens_per_week = dozen_per_day * 7
    total_dozens = dozens_per_week * 4
    money_made = total_dozens * price_per_dozen
    result = money_made
    return result

print(solution())