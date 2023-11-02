def solution():
    
    chickens = 10
    eggs_per_week = 6
    dozen_per_week = (chickens * eggs_per_week) / 12
    total_dozen = dozen_per_week * 2
    price_per_dozen = 2
    total_money = total_dozen * price_per_dozen
    result = total_money
    return result

print(solution())