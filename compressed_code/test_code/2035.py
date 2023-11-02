def solution():
    
    total_chickens = 46
    eggs_per_chicken_per_week = 6
    total_eggs_per_week = total_chickens * eggs_per_chicken_per_week
    dozens_per_week = total_eggs_per_week / 12
    price_per_dozen = 3
    total_money_in_8_weeks = dozens_per_week * price_per_dozen * 8
    result = total_money_in_8_weeks
    return result

print(solution())