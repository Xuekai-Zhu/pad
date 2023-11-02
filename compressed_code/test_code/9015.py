def solution():
    
    
    total_budget = 20000
    license_fee = 500
    docking_fee = license_fee * 3
    available_budget = total_budget - (license_fee + docking_fee)
    cost_per_foot = 1500
    longest_boat_length = available_budget // cost_per_foot
    result = longest_boat_length
    return result

print(solution())