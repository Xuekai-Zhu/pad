def solution(): 
    total_cost = 500
    units_purchased = 18
    discount_percent = 20
    discount_amount = total_cost * (discount_percent / 100)
    original_price = total_cost + discount_amount
    result = original_price
    return result

print(solution())