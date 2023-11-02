def solution():
    
    sweater_price = 30
    scarf_price = 20
    num_sweaters = 6
    num_scarves = 6
    total_cost = (sweater_price * num_sweaters) + (scarf_price * num_scarves)
    remaining_savings = 500 - total_cost
    result = remaining_savings
    return result

print(solution())