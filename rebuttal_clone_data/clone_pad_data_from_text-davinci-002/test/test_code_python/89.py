def solution():
    
    price_paid = 18
    percent_increase = 50
    increase_amount = price_paid * (percent_increase / 100)
    weekend_price = price_paid + increase_amount
    result = weekend_price
    
    return result

print(solution())