def solution():
    
    eggs_per_day = 252
    dozens_per_day = eggs_per_day / 12
    price_per_dozen = 2
    eggs_per_week = dozens_per_day * eggs_per_dozen * 7
    result = eggs_per_week
    return result

print(solution())