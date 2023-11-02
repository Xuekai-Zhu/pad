def solution():
    
    peaches_price = 0.4
    peaches_quantity = 400
    total_peaches_price = peaches_price * peaches_quantity
    discount_amount = (int(total_peaches_price / 10)) * 2
    final_price = total_peaches_price - discount_amount
    result = final_price
    return result

print(solution())