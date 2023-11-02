def solution():
    
    cost = 50
    markup_percent = 30
    sale_percent = 10
    selling_price = cost + (cost * markup_percent/100)
    discounted_price = selling_price - (selling_price * sale_percent/100)
    profit = discounted_price - cost
    profit_percent = profit/cost * 100
    result = round(profit_percent)
    return result

print(solution())