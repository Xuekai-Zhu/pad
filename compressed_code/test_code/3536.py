def solution():
    
    days_until_birthday = 22
    money_saved_per_day = 2
    flower_price = 4
    total_money_saved = days_until_birthday * money_saved_per_day
    total_flowers = total_money_saved // flower_price
    result = total_flowers
    return result

print(solution())