def solution():
    
    aluminum_can_value = 2
    plastic_bottle_value = 3
    soda_cans_per_week = 3
    water_bottles_per_week = 5
    total_money_per_week = (aluminum_can_value * soda_cans_per_week) + (plastic_bottle_value * water_bottles_per_week)
    total_money_per_month = total_money_per_week * 4
    result = total_money_per_month
    return result

print(solution())