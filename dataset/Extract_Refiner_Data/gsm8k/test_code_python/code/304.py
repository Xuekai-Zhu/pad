def solution():
    
    ice_cream_price = 13
    milk_price = 11
    ice_cream_discount = ice_cream_price - 11
    milk_discount = milk_price * 0.5
    ice_cream_total_price = ice_cream_price * 2
    milk_total_price = milk_discount * 4
    total_savings = ice_cream_total_price - milk_total_price
    result = total_savings
    return result

print(solution())