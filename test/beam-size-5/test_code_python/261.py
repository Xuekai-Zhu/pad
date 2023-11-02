def solution():
    
    budget = 400000
    property_price = 350000
    brokerage_fee = 0.05 * property_price
    transfer_fee = 0.12 * property_price
    total_price = property_price + brokerage_fee + transfer_fee
    difference = budget - total_price
    result = difference
    return result

print(solution())