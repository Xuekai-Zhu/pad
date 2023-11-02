def solution():
    
    eggs_per_dozen = 12
    store_1_eggs_per_day = 5 * eggs_per_dozen
    store_2_eggs_per_day = 30
    total_eggs_per_day = store_1_eggs_per_day + store_2_eggs_per_day
    eggs_per_week = total_eggs_per_day * 7
    result = eggs_per_week
    return result

print(solution())