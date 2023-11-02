def solution():
    cost = 50
    markup = 30
    sale_discount = 10
    selling_price = cost + (cost * (markup / 100))
    discounted_price = selling_price - (selling_price * (sale_discount / 100))
    percent_profit = ((discounted_price - cost) / cost) * 100
    result = percent_profit
    
    return result

print(solution())