def solution():
    
    can_price = 0.25
    total_cans = 12 + (3 * 12) + 46 + 250
    total_money = total_cans * can_price
    savings = total_money / 2
    result = savings
    return result

print(solution())