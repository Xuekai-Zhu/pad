def solution():
    
    pack_price = 40.00
    rush_shipping = 0.3
    total_price = pack_price * (1 + rush_shipping)
    cost_per_type = total_price / 4
    result = cost_per_type
    return result

print(solution())