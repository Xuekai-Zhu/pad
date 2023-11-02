def solution():
    apples_eaten_per_day = 6
    days_in_week = 7
    weekly_consumption = apples_eaten_per_day * days_in_week
    apples_picked_per_week =weekly_consumption + (weekly_consumption / 3)
    weeks = 6
    total_apples = apples_picked_per_week * weeks
    
    return total_apples

print(solution())