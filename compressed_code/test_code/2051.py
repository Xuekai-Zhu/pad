def solution():
    
    old_apartment_cost = 1200
    new_apartment_cost = old_apartment_cost * 1.4
    total_cost = new_apartment_cost / 3
    john_savings = old_apartment_cost - (total_cost)
    annual_savings = john_savings * 12
    result = annual_savings
    return result

print(solution())