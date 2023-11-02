def solution():
    
    original_price = 2000
    bought_price = original_price * 0.75
    sold_price = original_price * 0.120
    discounted_price = sold_price - bought_price
    percentage_discount = (discounted_price / original_price) * 100
    result = percentage_discount
    return result

print(solution())