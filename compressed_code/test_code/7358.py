def solution():
    
    total_money = 240
    samuel_percent = 3/4
    samuel_money = total_money * samuel_percent
    drinks_percent = 1/5
    drinks_cost = total_money * drinks_percent
    samuel_left = samuel_money - drinks_cost
    result = samuel_left
    return result

print(solution())