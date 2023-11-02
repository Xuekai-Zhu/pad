def solution():
    
    house_prices = [157000, 499000, 125000]
    commission_rate = 0.02
    total_commission = sum([price * commission_rate for price in house_prices])
    result = total_commission
    return result

print(solution())