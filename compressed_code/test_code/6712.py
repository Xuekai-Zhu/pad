def solution():
    
    sandwich_price = 5
    delivery_fee = 20
    num_sandwiches = 18
    total_price = (sandwich_price * num_sandwiches) + delivery_fee
    tip_percent = 10
    tip_amount = total_price * (tip_percent / 100)
    total_received = total_price + tip_amount
    result = total_received
    return result

print(solution())