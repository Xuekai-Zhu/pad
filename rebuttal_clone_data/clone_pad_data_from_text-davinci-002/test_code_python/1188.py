def solution():
    sandwich_price = 5
    delivery_fee = 20
    sandwich_quantity = 18
    tip_percentage = 10
    tip_amount = (sandwich_quantity * sandwich_price + delivery_fee) * (tip_percentage / 100)
    total_received = sandwich_quantity * sandwich_price + delivery_fee + tip_amount
    result = total_received
    
    return result

print(solution())