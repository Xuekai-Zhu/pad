def solution():
    
    sandwich_price = 5
    delivery_fee = 20
    total_sandwiches = 18
    total_price = (sandwich_price * total_sandwiches) + delivery_fee
    tip_percentage = 0.1
    tip_amount = total_price * tip_percentage
    total_amount = total_price + tip_amount
    result = total_amount
    return result

print(solution())