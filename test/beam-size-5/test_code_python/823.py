def solution():
    
    book_weight = 4
    book_cost = 32
    miles_to_return = 20
    shipping_price_per_pound = 0.35
    miles_to_refund = miles_to_return * 0.08
    total_cost = book_weight * book_cost + miles_to_refund * shipping_price_per_pound
    refund_amount = total_cost * 0.75
    loss = book_cost - refund_amount
    result = loss
    return result

print(solution())