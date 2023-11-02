def solution():
    
    sale_prices = [157000, 499000, 125000]
    commission_rate = 0.02
    total_commission = sum([sale_price * commission_rate for sale_price in sale_prices])
    result = total_commission
    return result

print(solution())