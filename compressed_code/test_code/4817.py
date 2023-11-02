def solution():
    
    local_price = 3
    promo_price = 2
    weekly_chocolates = 2
    weeks = 3
    local_total = weekly_chocolates * weeks * local_price
    promo_total = weekly_chocolates * weeks * promo_price
    savings = local_total - promo_total
    result = savings
    return result

print(solution())