def solution():
    
    total_budget = 20000
    license_fee = 500
    docking_fee = 3 * license_fee
    available_budget = total_budget - license_fee - docking_fee
    boat_price_per_foot = 1500
    max_boat_length = available_budget // boat_price_per_foot
    result = max_boat_length
    return result

print(solution())